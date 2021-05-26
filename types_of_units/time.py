def year_mls(num, order=0):
    if order:
        return num / 31540000000
    else:
        return num * 31540000000

def year_week(num, order=0):
    if order:
        return num / 52.143
    else:
        return num * 52.143

def year_day(num, order=0):
    if order:
        return num / 365
    else:
        return num * 365

def year_h(num, order=0):
    if order:
        return num / 8760
    else:
        return num * 8760

def year_min(num, order=0):
    if order:
        return num / 525600
    else:
        return num * 525600

def year_s(num, order=0):
    if order:
        return num / 31540000
    else:
        return num * 31540000

def week_day(num, order=0):
    if order:
        return num / 7
    else:
        return num * 7

def week_h(num, order=0):
    if order:
        return num / 168
    else:
        return num * 168

def week_min(num, order=0):
    if order:
        return num / 10080
    else:
        return num * 10080

def week_s(num, order=0):
    if order:
        return num / 604800
    else:
        return num * 604800

def week_mls(num, order=0):
    if order:
        return num / 604800000
    else:
        return num * 604800000

def day_h(num, order=0):
    if order:
        return num / 24
    else:
        return num * 24

def day_min(num, order=0):
    if order:
        return num / 1440
    else:
        return num * 1440

def day_s(num, order=0):
    if order:
        return num / 86400
    else:
        return num * 86400

def day_mls(num, order=0):
    if order:
        return num / 86400000
    else:
        return num * 86400000

def h_min(num, order=0):
    if order:
        return num / 60
    else:
        return num * 60

def h_s(num, order=0):
    if order:
        return num / 3600
    else:
        return num * 3600

def h_mls(num, order=0):
    if order:
        return num / 3600000
    else:
        return num * 3600000

def min_s(num, order=0):
    if order:
        return num / 60
    else:
        return num * 60

def min_mls(num, order=0):
    if order:
        return num / 60000
    else:
        return num * 60000

def s_mls(num, order=0):
    if order:
        return num / 1000
    else:
        return num * 1000

def compare_time(unit1, unit2, num):
    if unit1 == unit2:
        answer = num

    # year
    elif unit1 == 'year' and unit2 == 'mls':
        answer = year_mls(num)
    elif unit1 == 'mls' and unit2 == 'year':
        answer = year_mls(num, order=1)
    elif unit1 == 'year' and unit2 == 'week':
        answer = year_week(num)
    elif unit1 == 'week' and unit2 == 'year':
        answer = year_week(num, order=1)
    elif unit1 == 'year' and unit2 == 'day':
        answer = year_day(num)
    elif unit1 == 'day' and unit2 == 'year':
        answer = year_day(num, order=1)
    elif unit1 == 'year' and unit2 == 'h':
        answer = year_h(num)
    elif unit1 == 'h' and unit2 == 'year':
        answer = year_h(num, order=1)
    elif unit1 == 'year' and unit2 == 'min':
        answer = year_min(num)
    elif unit1 == 'min' and unit2 == 'year':
        answer = year_min(num, order=1)
    elif unit1 == 'year' and unit2 == 's':
        answer = year_s(num)
    elif unit1 == 's' and unit2 == 'year':
        answer = year_s(num, order=1)

    # week
    elif unit1 == 'week' and unit2 == 'day':
        answer = week_day(num)
    elif unit1 == 'day' and unit2 == 'week':
        answer = week_day(num, order=1)
    elif unit1 == 'week' and unit2 == 'h':
        answer = week_h(num)
    elif unit1 == 'h' and unit2 == 'week':
        answer = week_h(num, order=1)
    elif unit1 == 'week' and unit2 == 'min':
        answer = week_min(num)
    elif unit1 == 'min' and unit2 == 'week':
        answer = week_min(num, order=1)
    elif unit1 == 'week' and unit2 == 's':
        answer = week_s(num)
    elif unit1 == 's' and unit2 == 'week':
        answer = week_s(num, order=1)
    elif unit1 == 'week' and unit2 == 'mls':
        answer = week_mls(num)
    elif unit1 == 'mls' and unit2 == 'week':
        answer = week_mls(num, order=1)

    # day
    elif unit1 == 'day' and unit2 == 'h':
        answer = day_h(num)
    elif unit1 == 'h' and unit2 == 'day':
        answer = day_h(num, order=1)
    elif unit1 == 'day' and unit2 == 'min':
        answer = day_min(num)
    elif unit1 == 'min' and unit2 == 'day':
        answer = day_min(num, order=1)
    elif unit1 == 'day' and unit2 == 's':
        answer = day_s(num)
    elif unit1 == 's' and unit2 == 'day':
        answer = day_s(num, order=1)
    elif unit1 == 'day' and unit2 == 'mls':
        answer = day_mls(num)
    elif unit1 == 'mls' and unit2 == 'day':
        answer = day_mls(num, order=1)
    
    # h
    elif unit1 == 'h' and unit2 == 'min':
        answer = h_min(num)
    elif unit1 == 'min' and unit2 == 'h':
        answer = h_min(num, order=1)
    elif unit1 == 'h' and unit2 == 's':
        answer = h_s(num)
    elif unit1 == 's' and unit2 == 'h':
        answer = h_s(num, order=1)
    elif unit1 == 'h' and unit2 == 'mls':
        answer = h_mls(num)
    elif unit1 == 'mls' and unit2 == 'h':
        answer = h_mls(num, order=1)
    
    # min
    elif unit1 == 'min' and unit2 == 's':
        answer = min_s(num)
    elif unit1 == 's' and unit2 == 'min':
        answer = min_s(num, order=1)
    elif unit1 == 'min' and unit2 == 'mls':
        answer = min_mls(num)
    elif unit1 == 'mls' and unit2 == 'min':
        answer = min_mls(num, order=1)
    
    # s
    elif unit1 == 's' and unit2 == 'mls':
        answer = s_mls(num)
    elif unit1 == 'mls' and unit2 == 's':
        answer = s_mls(num, order=1)
    
    return answer