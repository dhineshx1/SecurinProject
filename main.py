from website import create_app
from website import data_sync
import threading

app = create_app()


def run_flask():
    app.run(debug=True)


def run_data_sync():
    """
        Function to run the data synchronization process.

        This function initiates the data synchronization process defined in the data_sync module.
    """
    data_sync.data_synchronization()


if __name__ == '__main__':

    run_flask()

    # Creating a new thread to run the data synchronization process concurrently
    t1 = threading.Thread(target=run_data_sync)
    t1.start()
