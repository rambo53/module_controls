from datetime import datetime

def get_datetime():
    return datetime.now()

def format_datetime(date):
    format_date = "%d/%m/%y %H:%M"
    return datetime.strptime(date, format_date)
    