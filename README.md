
# CVE INFORMATION WEBSITE USING FLASK 



   Instructions on how to get a copy of the project up and running on your local machine for development
## UI Screenshots
#### CVE TABLE PAGE 
![detailPage](website/static/detail-page.png)
#### CVE DETAILS PAGE
![detailPage](website/static/detail-page.png)

## Functional Approach
### Project Overview:
- The project appears to be a web application for managing Common Vulnerabilities and Exposures (CVE) data.
- It involves fetching CVE data from an external API, storing it in a local database, and presenting it to users through a web interface.
#### User Stories:
- Define user stories based on the functionality provided by the application, such as:
  - As a user, I want to view a list of CVE entries.
  - As a user, I want to see details of a specific CVE entry.
  - As a user, I want to synchronize the CVE data with the latest updates.
#### Feature Breakdown:
- View CVE List: Display a paginated list of CVE entries.
- View CVE Details: Show detailed information about a specific CVE entry.
- Data Synchronization: Periodically fetch and update CVE data from the external API.
#### User Interface (UI):
- Design a user-friendly interface for browsing CVE entries and viewing details.
- Implement pagination for the CVE list page to handle large datasets effectively.
#### Backend Functionality:
- Implement Flask routes to serve the frontend views and handle API requests.
- Develop functions to fetch CVE data from the external API and store it in the local database.
- Implement data retrieval functions to fetch CVE entries and details from the database.

## Database approach

#### Database Design:
- Define a MongoDB database schema to store CVE data.
- Design collections to represent different entities such as CVE entries and details.
#### Data Access Layer:
- Implement database access functions using PyMongo to perform CRUD operations.
- Ensure proper error handling and data validation to maintain data integrity.
#### Data Validation:
- Validate incoming data before storing it in the database to prevent errors and ensure consistency.


## API Reference

#### To interact with the National Vulnerability Database (NVD) API and store CVE data in MongoDB

```http
  https://services.nvd.nist.gov/rest/json/cves/2.0
```

## Prerequisites



List of software and dependencies required to run the project.
```
MongoDB
flask 
pymongo
schdule
requests

```
## Installation

#### Install CVE project in your local machine (python shell) or any IDE


Install MongoDB and compus  for the local server 
```
https://www.mongodb.com/products/self-managed/community-edition
```

Run the below code to setup the project 

```bash
  python setup.py sdist
```
    