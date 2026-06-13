from datetime import datetime

def parse_and_inspect_date(date_str: str):

    time_format = "%Y-%m-%d"
    return datetime.strptime(date_str, time_format)