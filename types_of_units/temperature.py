def c_f(num, order=0):
    if order:
        return (num - 32) * 5/9
    else:
        return (num * 9/5) + 32

def c_k(num, order=0):
    if order:
        return num -273
    else:
        return num + 273

def f_k(num, order=0):
    if order:
        return (num - 273) * 9/5 + 32
    else:
        return (num - 32) * 5/9 + 273

def compare_temperature(unit1, unit2, num):
    # c
    if unit1 == 'c' and unit2 == 'f':
        answer = c_f(num)
    elif unit1 == 'f' and unit2 == 'c':
        answer = c_f(num, order=1)
    elif unit1 == 'c' and unit2 == 'k':
        answer = c_k(num)
    elif unit1 == 'k' and unit2 == 'c':
        answer = c_k(num, order=1)
    
    # f
    elif unit1 == 'f' and unit2 == 'k':
        answer = f_k(num)
    elif unit1 == 'k' and unit2 == 'f':
        answer = f_k(num, order=1)
    
    return answer