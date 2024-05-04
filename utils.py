import re

def validate_isbn(isbn):
    if re.match(r"^\d{13}$", isbn):
        return True
    else:
        return False

def validate_date(date):
    if re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        return True
    else:
        return False