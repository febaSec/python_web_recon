import logging, sys
from art import text2art
from rich.console import Console

#
#                        Configure logging function
#
def setup_logging(verbose: bool, filename: str):
    # Creating a logger object and defining the filtering level
    logger = logging.getLogger("WebRecon")
    logger.setLevel(logging.DEBUG)

    # Defining logging format
    log_format = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)s', 
        datefmt='%H:%M:%S'
    )

    # Creating file handler
    file_handler = logging.FileHandler(filename, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(log_format)

    # Creating console handler
    console_handler = logging.StreamHandler(sys.stdout)
    if verbose:
        console_handler.setLevel(logging.INFO)
    else:
        console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(log_format)

    # Adding handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Returning configured logger object to main file
    return logger




#
#                   Configure art (banner) function
#
console = Console()
def print_banner():
    banner = text2art("Python Web Recon", font="mini")
    console.print(f"[bold cyan]{banner}[/]")
    console.print("[dim]v1.1.0 | Created by Feba[/]\n")
    console.rule(style="dim")
