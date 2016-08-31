# -*- coding:utf-8 -*-
def date_parse(date):
    if date:
        return str(date)
    else:
        return None


def sex_parse(sex, state):
    if sex == None:
        return sex
    if state:
        if sex == True:
            return u'男'
        else:
            return u'女'
    else:
        if sex == u'男':
            return True
        else:
            return u'女'