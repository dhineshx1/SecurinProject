def date_format_changer(date):
    """
    Converts a date string from "YYYY-MM-DD" format to "DD MON YYYY" format.

    Args:
        date (str): The date string to be converted.

    Returns:
        str: The converted date string in "DD MON YYYY" format, where MON represents the abbreviated month name.
    """
    # Dictionary mapping numeric month values to their corresponding abbreviated names
    month = {
        "01": "JAN",
        "02": "FEB",
        "03": "MAR",
        "04": "APR",
        "05": "MAY",
        "06": "JUN",
        "07": "JUL",
        "08": "AUG",
        "09": "SEP",
        "10": "OCT",
        "11": "NOV",
        "12": "DEC"
    }

    # Extracting only the date part from the input string
    date = date[:10]

    # Splitting the date string into year, month, and day components
    date_parts = date.split("-")

    # Replacing the numeric month with its abbreviated name
    date_parts[1] = month[date_parts[1]]

    # Joining the date parts in reverse order with spaces
    return " ".join(date_parts[::-1])
