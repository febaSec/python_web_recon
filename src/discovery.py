import subprocess, sys, logging
#
#         Specifi logging object
#
log = logging.getLogger("WebRecon")


def run_subfinder(domain):
    log.info(f"Subfinder has started the search")
    try:
        result = subprocess.run(["subfinder", "-d", domain, "-silent"], capture_output=True, text=True).stdout
        if result:
            result = result.strip().split("\n")
        else:
            result = None
        return result
    except Exception as err:
        log.error(f"An error has occured: {err}")
        sys.exit(10)
