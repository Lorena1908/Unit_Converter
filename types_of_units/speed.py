def kh_ms(num, order=0):
    if order:
        return num * 3.6
    else:
        return num / 3.6

def kh_mileh(num, order=0):
    if order:
        return num * 1.609
    else:
        return num / 1.609

def ms_mileh(num, order=0):
    if order:
        return num / 2.237
    else:
        return num * 2.237

def compare_speed(unit1, unit2, num):
    if unit1 == unit2:
        answer = num
    
    # kh
    elif unit1 == 'kh' and unit2 == 'ms':
        answer = kh_ms(num)
    elif unit1 == 'ms' and unit2 == 'kh':
        answer = kh_ms(num, order=1)
    elif unit1 == 'kh' and unit2 == 'mileh':
        answer = kh_mileh(num)
    elif unit1 == 'mileh' and unit2 == 'kh':
        answer = kh_mileh(num, order=1)

    # ms
    elif unit1 == 'ms' and unit2 == 'mileh':
        answer = ms_mileh(num)
    elif unit1 == 'mileh' and unit2 == 'ms':
        answer = ms_mileh(num, order=1)
    
    return answer