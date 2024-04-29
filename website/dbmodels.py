import requests  # Importing the requests module for making HTTP requests
from pymongo import MongoClient  # Importing the MongoClient class from pymongo for interacting with MongoDB


class Database:
    """
    A class to interact with the National Vulnerability Database (NVD) API and store CVE data in MongoDB.

    Attributes:
        api_url (str): The base URL of the NVD API.
        mongo_client (pymongo.MongoClient): The MongoClient instance for connecting to MongoDB.
        db_name (pymongo.database.Database): The name of the MongoDB database.
        cve_collection (pymongo.collection.Collection): The collection in the MongoDB database for storing CVE data.
    """

    def __init__(self):
        """
        Initializes the Database class with necessary attributes.
        """
        self.api_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
        self.mongo_client = MongoClient('mongodb://localhost:27017')
        self.db_name = self.mongo_client['SecurinProject']
        self.cve_collection = self.db_name['cveTable']

    def fetch_total_no_of_records(self):
        """
        Fetches the total number of CVE records available in the NVD database.

        Returns:
            int: The total number of CVE records.
        """
        response = requests.get(self.api_url)
        if response.status_code == 200:
            res = response.json()
            return res["totalResults"]
        else:
            print(f"Unable to fetch the API response. Status code: {response.status_code}")

    def default_max_response(self):
        """
        Fetches the default maximum number of CVE records per page from the NVD API.

        Returns:
            int: The default maximum number of CVE records per page.
        """
        response = requests.get(self.api_url)
        if response.status_code == 200:
            res = response.json()
            return res["resultsPerPage"]
        else:
            print(f"Unable to fetch the API response. Status code: {response.status_code}")

    def fetch_data_from_api(self, start=0):
        """
        Fetches CVE data from the NVD API and inserts it into the MongoDB database.

        Args:
            start (int, optional): The index from which to start fetching records. Defaults to 0.
        """
        no_of_records = self.fetch_total_no_of_records()
        resultPerPage = self.default_max_response()

        for startIndex in range(start, no_of_records, resultPerPage):
            response = requests.get(f"{self.api_url}/?startIndex={startIndex}")
            if response.status_code == 200:
                self.insert_in_db(response.json())
            else:
                print(f"Error: Unable to fetch data. Status code: {response.status_code}, chunk no: {startIndex}")

    def insert_in_db(self, data):
        """
        Inserts CVE data into the MongoDB database.

        Args:
            data (dict): The CVE data to be inserted into the database.
        """
        for cve_item in data['vulnerabilities']:
            self.cve_collection.insert_one(cve_item['cve'])

    def total_records_in_db(self):
        """
        Retrieves the total number of CVE records stored in the MongoDB database.

        Returns:
            int: The total number of CVE records stored in the database.
        """
        return self.cve_collection.count_documents({})


