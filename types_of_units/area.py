def hec_sm(num, order=0):
    if order:
        return num / 10000
    else:
        return num * 10000

def compare_area(unit1, unit2, num):
    if unit1 == unit2:
        answer = num
    
    if unit1 == 'hec' and unit2 == 'sm':
        answer = hec_sm(num)
    elif unit1 == 'sm' and unit2 == 'hec':
        answer = hec_sm(num, order=1)
    
    return answer