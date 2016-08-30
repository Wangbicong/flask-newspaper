def date_parse(date):
    if date:
        return str(date.year) + '-' + str(date.month)\
               + '-' + str(date.day)
    else:
        return None
