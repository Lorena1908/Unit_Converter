def atm_pa(num, order=0):
    if order:
        return num / 101325
    else:
        return num * 101325

def atm_mmHg(num, order=0):
    if order:
        return num / 760
    else:
        return num * 760

def pa_mmHg(num, order=0):
    if order:
        return num * 133
    else:
        return num / 133

def compare_pressure(unit1, unit2, num):
    if unit1 == unit2:
        answer = num

    # atm
    if unit1 == 'atm' and unit2 == 'pa':
        answer = atm_pa(num)
    elif unit1 == 'pa' and unit2 == 'atm':
        answer = atm_pa(num, order=1)
    elif unit1 == 'atm' and unit2 == 'mmHg':
        answer = atm_mmHg(num)
    elif unit1 == 'mmHg' and unit2 == 'atm':
        answer = atm_mmHg(num, order=1)
    
    # pa
    elif unit1 == 'pa' and unit2 == 'mmHg':
        answer = pa_mmHg(num)
    elif unit1 == 'mmHg' and unit2 == 'pa':
        answer = pa_mmHg(num, order=1)
    
    return answer