from flask import Blueprint, render_template, request
from . import dbmodels, datacleansing

# Creating a Blueprint named 'views'
views = Blueprint("views", __name__)

# Accessing the MongoDB collection through the Database class
collection = dbmodels.Database().cve_collection


@views.route('/')
def index():
    """
    Renders the CVE list page.

    Retrieves CVE data from the database, applies pagination, and renders the CVE list template.

    Returns:
        str: Rendered HTML template for the CVE list page.
    """
    # Retrieving page number and items per page from the request query parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Counting total number of CVE records in the database
    total_count = collection.count_documents({})

    # Retrieving CVE data from the database with pagination
    data = list(collection.find().skip((page - 1) * per_page).limit(per_page))

    # Transforming data to required format for rendering
    cve_list = []
    for document in data:
        cve_list.append({
            "id": document["id"],
            "sourceIdentifier": document["sourceIdentifier"],
            "published": datacleansing.date_format_changer(document["published"]),
            "lastModified": datacleansing.date_format_changer(document["lastModified"]),
            "vulnStatus": document["vulnStatus"]
        })

    # Rendering the CVE list template with the transformed data
    return render_template('index.html', cve_list=cve_list, page=page, per_page=per_page, total_count=total_count)


@views.route('/cve/<cve_id>')
def cve_details(cve_id):
    """
    Renders the CVE details page for a specific CVE ID.

    Retrieves CVE details from the database based on the provided CVE ID and renders the CVE details template.

    Args:
        cve_id (str): The ID of the CVE.

    Returns:
        str: Rendered HTML template for the CVE details page.
    """
    # Retrieving CVE details from the database based on the provided CVE ID
    cve = collection.find_one({"id": cve_id})

    # If CVE details exist, render the CVE details template with the data
    if cve:
        # Extracting English description from the CVE details
        english_description = next((desc['value'] for desc in cve['descriptions'] if desc['lang'] == 'en'), None)

        # Extracting CVSS metrics from the CVE details
        cvss_metrics = cve["metrics"].get("cvssMetricV2", [{}])[0]
        cvss_data = cvss_metrics.get("cvssData", {})

        # Extracting other relevant CVE details for rendering
        severity = cvss_metrics.get("baseSeverity", "")
        baseScore = cvss_data.get("baseScore", 0)
        accessVector = cvss_data.get("accessVector", "")
        accessComplexity = cvss_data.get("accessComplexity", "")
        authentication = cvss_data.get("authentication", "")
        confidentialityImpact = cvss_data.get("confidentialityImpact", "")
        integrityImpact = cvss_data.get("integrityImpact", "")
        availabilityImpact = cvss_data.get("availabilityImpact", "")
        vectorString = cvss_data.get("vectorString", "")
        impactScore = cvss_metrics.get("impactScore", 0)
        exploitabilityScore = cvss_metrics.get("exploitabilityScore", 0)

        # Extracting CPE details from the CVE details
        configurations = cve.get("configurations", [])
        cpe = []
        for configuration in configurations:
            nodes = configuration.get("nodes", [])
            for node in nodes:
                cpe_match = node.get("cpeMatch", [])
                for item in cpe_match:
                    cpe.append({
                        "criteria": item.get("criteria", ""),
                        "matchCriteriaId": item.get("matchCriteriaId", ""),
                        "vulnerable": item.get("vulnerable", False)
                    })

        # Rendering the CVE details template with the extracted data
        return render_template('cve_details.html', cve={
            "id": cve["id"],
            "descriptions": english_description,
            "severity": severity,
            "baseScore": baseScore,
            "accessVector": accessVector,
            "accessComplexity": accessComplexity,
            "authentication": authentication,
            "confidentialityImpact": confidentialityImpact,
            "integrityImpact": integrityImpact,
            "availabilityImpact": availabilityImpact,
            "impactScore": impactScore,
            "exploitabilityScore": exploitabilityScore,
            "vectorString": vectorString,
            "cpe": cpe
        })

