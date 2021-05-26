def wh_j(num, order=0):
    if order:
        return num / 3600
    else:
        return num * 3600

def wh_cal(num, order=0):
    if order:
        return num / 860
    else:
        return num * 860

def j_cal(num, order=0):
    if order:
        return num * 4.184
    else:
        return num / 4.184

def compare_energy(unit1, unit2, num):
    if unit1 == unit2:
        answer = num
    
    # wh
    elif unit1 == 'wh' and unit2 == 'j':
        answer = wh_j(num)
    elif unit1 == 'j' and unit2 == 'wh':
        answer = wh_j(num, order=1)
    elif unit1 == 'wh' and unit2 == 'cal':
        answer = wh_cal(num)
    elif unit1 == 'cal' and unit2 == 'wh':
        answer = wh_cal(num, order=1)
    
    # j
    elif unit1 == 'j' and unit2 == 'cal':
        answer = j_cal(num)
    elif unit1 == 'cal' and unit2 == 'j':
        answer = j_cal(num, order=1)
    
    return answer