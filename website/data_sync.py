import schedule  # Importing the schedule library for scheduling tasks
from . import dbmodels  # Importing the dbmodels module containing the Database class
import time  # Importing the time module for time-related operations


def data_synchronization():
    """
    Synchronizes data from an API periodically using the schedule library.

    This function schedules the fetching of data from an API using the Database class
    from the dbmodels module. It runs continuously and periodically fetches data from
    the API according to the specified schedule.

    Note:
        The schedule is set to fetch data every hour.

    Raises:
        Exception: An error occurred in calling the API.
    """
    try:
        # Getting the total number of records already present in the database
        start_records = dbmodels.Database().total_records_in_db()

        # Scheduling a task to fetch data from the API every hour
        schedule.every().minute.do(dbmodels.Database().fetch_data_from_api(start_records))

        # Running the schedule continuously
        while True:
            schedule.run_pending()  # Running pending scheduled tasks
            time.sleep(1)  # Delaying execution for 1 second
    except Exception as e:
        # Handling exceptions raised during API calls
        print("An error occurred in calling API:", e)
