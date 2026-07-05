import sqlite3, sys, logging
from datetime import datetime
#
#         Specifi logging object
#
log = logging.getLogger("WebRecon")


#
#         Creating a function to initialize a table.
#
def init_db(connect):
    query = """
    CREATE TABLE IF NOT EXISTS recon_result (
        domain TEXT UNIQUE,
        status INTEGER,
        last_seen TEXT
    )
    """
    cursor = connect.cursor()
    try:
        cursor.execute(query)
    except Exception as err:
        log.error(f"An error has occured: {err}")
        sys.exit(12)

    log.info(f"The database has been initialised")

#
#         Creating a function to insert or update info in table
#
def update_db(cur, action: str, data: dict):
    insert_query = "INSERT INTO recon_result (domain, status, last_seen) VALUES (:url, :status, :time)"
    update_query = "UPDATE recon_result SET status = :status, last_seen = :time WHERE domain = :url"
    try:
        if action == "update":
            cur.execute(update_query, data)

        if  action == "insert":
            cur.execute(insert_query, data)
            
    except Exception as err:
        log.error(f"An error has occured: {err}")
        sys.exit(12)

        
#   
#         Creating a function to retrieve data from a table
#
# current_results = [{'url': 'google.com', 'status': 200}, {'url': 'ukr.net', 'status': 200}, {'url': 'gmail.com', 'status': 200}, {'url': 'steamdb.info', 'status': 0}, {'url': 'youtube.com', 'status': 200}]

def get_new_discoveries(conn, current_results):
    updates = []
    get_query = "SELECT status FROM recon_result WHERE domain = ?"
    cursor = conn.cursor()

    log.info(f"The current results are checked and changes are made to the database")
    for item in current_results:
        action = None
        # Checking data in table
        try:
            cursor.execute(get_query, (item['url'], ))
        except Exception as err:
            log.error(f"An error has occured: {err}")
            sys.exit(12)
        status_answ = cursor.fetchone()

        # Defining the action we need to perform on the database
        if not status_answ:
            action = "insert"
        elif status_answ[0] != item['status']:
            action = "update"

        #  Creating the required data type and perform the specified action
        if action:
            payload = {
                'url': item['url'],
                'status': item['status'],
                'time': datetime.now()
            } 
            update_db(cursor, action, payload)
            item['action'] = action
            if action == "update":
                item['stored_status'] = status_answ[0]
            updates.append(item)

    # Confirm all database updated and return results
    conn.commit() 
    log.info(f"The database has been updated")             
    return updates



