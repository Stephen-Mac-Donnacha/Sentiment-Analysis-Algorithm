# Use this file for utility methods, i.e., methods that don't contribute much
# or anything to the main project, but add readability or convenience

# Method to sanitise a string for analysis, used for the content of tweets
def sanitise_str(string):
    string = string.lower()
    string = string.strip()
    return string


# Method to sanitise a date, for analysis of frequency and summation of sentiment, utility method
def sanitise_date(date_string):
    date_string = date_string.strip()
    return date_string

# Utility method, designed to extract the days, from a list of dates
def extract_days(lst):
    return [item[0] for item in lst]

# Utility method, designed to extract the month, from a list of dates
def extract_months(lst):
    return [item[1] for item in lst]



