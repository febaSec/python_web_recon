#!python3 3.12

import argparse, os, sys, subprocess, sqlite3
from dotenv import load_dotenv
from src import init_db, run_subfinder, run_scanner, get_new_discoveries, send_tg
from src import  setup_logging, print_banner
from rich.console import Console

#
#                            Printing banner
#
print_banner()

#
#                         Configure rich console object
#
console = Console()

#
#                        Working with pathes                                                  
#
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "recon.db")
LOG_FILE = os.path.join(BASE_DIR, "recon.log")

#
#                        Enable variables from .env
#
load_dotenv()
token = os.getenv("TG_TOKEN")
chat_id = os.getenv("TG_CHAT_ID")

#
#                           Work with flags
#
parser = argparse.ArgumentParser(description="Domains recon tool v1.0")
parser.add_argument("-d", "--domain", type=str, help="Specify the domain", required=True)
parser.add_argument("-t", "--threads", type=int, default=10)
parser.add_argument("-o", "--output", required=False)
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()

#
#                          Specified logging
#
log = setup_logging(args.verbose, LOG_FILE)

#
#                       Check whether Subfinder is installed on the system
#
try:
    subprocess.run(['subfinder', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
except Exception:
    print(f"The important tool [subfinder] is not installed on the system.")
    sys.exit(3)

#
#                         Activate database connection and initialisation of database
#
conn = sqlite3.connect(DB_PATH)
init_db(conn)

#
#                          Main logic
# 
try:
    # Starting work with discover subdomains
    with console.status("[cyan]The search for subdomains is ongoing (Subfinder)...", spinner="earth"):
        subdomains = run_subfinder(args.domain)

    # Сhecking whether we’ve found any subdomains, and if so, check whether they respond
    current_subdomains = []
    if subdomains:
        with console.status("[cyan]The subdomain scan is in progress...", spinner="earth"):
            current_subdomains = run_scanner(subdomains, args.threads)

    # Check whether we are already aware of the analysed subdomains. If not, add them to the database
    updates = get_new_discoveries(conn, current_subdomains)
except KeyboardInterrupt:
    log.warning("The process was interrupted by the user")
    sys.exit(0)
    
# Sending results to telegram chat
send_tg(token, chat_id, updates)

# Closing database connection
conn.close()
