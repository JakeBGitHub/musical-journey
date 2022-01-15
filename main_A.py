from utils.connect2database import *

import datetime
import time


def main():

    print("--- Start Time: ", datetime.datetime.now().strftime("%H:%M:%S"))
    start_time = time.time()

    conn = connect_to_database()

    ## Query 1
    conn.execute(A1_QUERY1)
    print("Success! A1_QUERY1 complete.")
    ## Query 2
    conn.execute(A1_QUERY2)
    print("Success! A1_QUERY2 complete.")
    ## Query 3
    conn.execute(A2_QUERY1)
    print("Success! A2_QUERY1 complete.")
    ## Query 4
    conn.execute(A2_QUERY2)
    print("Success! A2_QUERY2 complete.")
    # ## Query 5
    # conn.execute(A3_QUERY1)
    # print("Success! A3_QUERY1 complete.")
    # ## Query 6
    # conn.execute(A3_QUERY2)
    # print("Success! A3_QUERY2 complete.")

    print("--- Script Execution Time: %s seconds ---" % (time.time() - start_time))
    print("--- End Time: {} ---".format(datetime.datetime.now().strftime("%H:%M:%S")))


if __name__ == "__main__":
    main()
