def cm_gallon(num, order=0):
    if order:
        return num / 264
    else:
        return num * 264

def cm_l(num, order=0):
    if order:
        return num / 1000
    else:
        return num * 1000

def cm_ml(num, order=0):
    if order:
        return num / 1000000
    else:
        return num * 1000000

def gallon_l(num, order=0):
    if order:
        return num / 3.785
    else:
        return num * 3.785

def gallon_ml(num, order=0):
    if order:
        return num / 3785
    else:
        return num * 3785

def l_ml(num, order=0):
    if order:
        return num / 1000
    else:
        return num * 1000

def compare_volume(unit1, unit2, num):
    if unit1 == unit2:
        answer = num

    # cm
    elif unit1 == 'cm' and unit2 == 'gallon':
        answer = cm_gallon(num)
    elif unit1 == 'gallon' and unit2 == 'cm':
        answer = cm_gallon(num, order=1)
    elif unit1 == 'cm' and unit2 == 'l':
        answer = cm_l(num)
    elif unit1 == 'l' and unit2 == 'cm':
        answer = cm_l(num, order=1)
    elif unit1 == 'cm' and unit2 == 'ml':
        answer = cm_ml(num)
    elif unit1 == 'ml' and unit2 == 'cm':
        answer = cm_ml(num, order=1)
    
    # gallon
    elif unit1 == 'gallon' and unit2 == 'l':
        answer = gallon_l(num)
    elif unit1 == 'l' and unit2 == 'gallon':
        answer = gallon_l(num, order=1)
    elif unit1 == 'gallon' and unit2 == 'ml':
        answer = gallon_ml(num)
    elif unit1 == 'ml' and unit2 == 'gallon':
        answer = gallon_ml(num, order=1)

    # l
    elif unit1 == 'l' and unit2 == 'ml':
        answer = l_ml(num)
    elif unit1 == 'ml' and unit2 == 'l':
        answer = l_ml(num, order=1)
    
    return answer