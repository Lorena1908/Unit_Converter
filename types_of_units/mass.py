def tonne_pound(num, order=0):
    if order:
        return num / 2205
    else:
        return num * 2205

def tonne_kg(num, order=0):
    if order:
        return num / 1000
    else:
        return num * 1000
    
def tonne_g(num, order=0):
    if order:
        return num / 1000000
    else:
        return num * 1000000

def tonne_mg(num, order=0):
    if order:
        return num / 1000000000
    else:
        return num * 1000000000

def tonne_ounce(num, order=0):
    if order:
        return num / 35274
    else:
        return num * 35274

def pound_kg(num, order=0):
    if order:
        return num * 2.205
    else:
        return num / 2.205

def pound_g(num, order=0):
    if order:
        return num / 454
    else:
        return num * 454

def pound_mg(num, order=0):
    if order:
        return num / 453592
    else:
        return num * 453592

def pound_ounce(num, order=0):
    if order:
        return num / 16
    else:
        return num * 16

def kg_g(num, order=0):
    if order:
        return num / 1000
    else:
        return num * 1000

def kg_mg(num, order=0):
    if order:
        return num / 1000000
    else:
        return num * 1000000

def kg_ounce(num, order=0):
    if order:
        return num / 35.274
    else:
        return num * 35.274

def g_mg(num, order=0):
    if order:
        return num / 1000
    else:
        return num * 1000

def g_ounce(num, order=0):
    if order:
        return num * 28.35
    else:
        return num / 28.35

def mg_ounce(num, order=0):
    if order:
        return num * 28350
    else:
        return num / 28350

def compare_mass(unit1, unit2, num):
    if unit1 == unit2:
        answer = num
    
    # tonne
    elif unit1 == 'tonne' and unit2 == 'pound':
        answer = tonne_pound(num)
    elif unit1 == 'pound' and unit2 == 'tonne':
        answer = tonne_pound(num, order=1) 
    elif unit1 == 'tonne' and unit2 == 'kg':
        answer = tonne_kg(num) 
    elif unit1 == 'kg' and unit2 == 'tonne':
        answer = tonne_kg(num, order=1) 
    elif unit1 == 'tonne' and unit2 == 'g':
        answer = tonne_g(num)
    elif unit1 == 'g' and unit2 == 'tonne':
        answer = tonne_g(num, order=1) 
    elif unit1 == 'tonne' and unit2 == 'mg':
        answer = tonne_mg(num) 
    elif unit1 == 'mg' and unit2 == 'tonne':
        answer = tonne_mg(num, order=1) 
    elif unit1 == 'tonne' and unit2 == 'ounce':
        answer = tonne_ounce(num) 
    elif unit1 == 'ounce' and unit2 == 'tonne':
        answer = tonne_ounce(num, order=1)
    
    # pound
    elif unit1 == 'pound' and unit2 == 'kg':
        answer = pound_kg(num)
    elif unit1 == 'kg' and unit2 == 'pound':
        answer = pound_kg(num, order=1)
    elif unit1 == 'pound' and unit2 == 'g':
        answer = pound_g(num)
    elif unit1 == 'g' and unit2 == 'pound':
        answer = pound_g(num, order=1)
    elif unit1 == 'pound' and unit2 == 'mg':
        answer = pound_mg(num)
    elif unit1 == 'mg' and unit2 == 'pound':
        answer = pound_mg(num, order=1)
    elif unit1 == 'pound' and unit2 == 'ounce':
        answer = pound_ounce(num)
    elif unit1 == 'ounce' and unit2 == 'pound':
        answer = pound_ounce(num, order=1)
    
    # kg
    elif unit1 == 'kg' and unit2 == 'g':
        answer = kg_g(num)
    elif unit1 == 'g' and unit2 == 'kg':
        answer = kg_g(num, order=1)
    elif unit1 == 'kg' and unit2 == 'mg':
        answer = kg_mg(num)
    elif unit1 == 'mg' and unit2 == 'kg':
        answer = kg_mg(num, order=1)
    elif unit1 == 'kg' and unit2 == 'ounce':
        answer = kg_ounce(num)
    elif unit1 == 'ounce' and unit2 == 'kg':
        answer = kg_ounce(num, order=1)

    # g
    elif unit1 == 'g' and unit2 == 'mg':
        answer = g_mg(num)
    elif unit1 == 'mg' and unit2 == 'g':
        answer = g_mg(num, order=1)
    elif unit1 == 'g' and unit2 == 'ounce':
        answer = g_ounce(num)
    elif unit1 == 'ounce' and unit2 == 'g':
        answer = g_ounce(num, order=1)
    
    # mg
    elif unit1 == 'mg' and unit2 == 'ounce':
        answer = mg_ounce(num)
    elif unit1 == 'ounce' and unit2 == 'mg':
        answer = mg_ounce(num, order=1)
    
    return answer