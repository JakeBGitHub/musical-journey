from utils.connect2database import *

import datetime
import time


def main():

    print("--- Start Time: ", datetime.datetime.now().strftime("%H:%M:%S"))
    start_time = time.time()

    conn = connect_to_database()

    ## Query 1
    conn.execute(E_QUERY1)
    print("Success! Query 1 complete.")
    ## Query 2
    conn.execute(E_QUERY2)
    print("Success! Query 2 complete.")
    ## Query 3
    conn.execute(E_QUERY3)
    print("Success! Query 3 complete.")

    print("--- Script Execution Time: %s seconds ---" % (time.time() - start_time))
    print("--- End Time: {} ---".format(datetime.datetime.now().strftime("%H:%M:%S")))


if __name__ == "__main__":
    main()
