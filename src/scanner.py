import requests, sys, logging
from concurrent.futures import ThreadPoolExecutor
#
#         Specifi logging object
#
log = logging.getLogger("WebRecon")


#
#        Creating a "worker" function
#
def check_url(url):
    # Creating the variables required for the function 
    is_alive_url = {}
    is_alive_url["url"] = url
    link = f"https://{url}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64; rv:151.0) "
            "Gecko/20100101 Firefox/151.0"
        )
    }
    # Checking domain
    try:
        response = requests.get(link, headers=headers, timeout=3)
        is_alive_url["status"] = response.status_code
    except Exception as err:
        is_alive_url["status"] = 0
    # Returning results
    return is_alive_url


#
#        Creating "organize" function
#
#subdomains = ["google.com", "ukr.net", "gmail.com", "steamdb.info", "youtube.com"]
def run_scanner(subdomains, threads_count):
    log.info(f"Scanning was started")
    with ThreadPoolExecutor(max_workers=threads_count) as executor:
        domains_result = list(executor.map(check_url, subdomains))

    if not domains_result:
        domains_result = None

    log.info(f"Scanning has been ended")
    return domains_result
  
