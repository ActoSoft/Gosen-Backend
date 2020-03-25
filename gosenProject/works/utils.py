from datetime import datetime


def validate_works_dates(date_start, date_end):
    return datetime.strptime(date_start, '%Y-%m-%d') < datetime.strptime(date_end, '%Y-%m-%d')
