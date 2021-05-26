def m_cm(num, order=0):
    if order:
        return num / 100
    else:
        return num * 100

def km_m(num, order=0):
    if order:
        return num / 1000
    else:
        return num * 1000

def mile_km(num, order=0):
    if order:
        return num / 1.609
    else:
        return num * 1.609

def inch_cm(num, order=0):
    if order:
        return num / 2.54
    else:
        return num * 2.54

def cm_mm(num, order=0):
    if order:
        return num / 10
    else:
        return num * 10

def foot_cm(num, order=0):
    if order:
        return num / 30.48
    else:
        return num * 30.48

def foot_m(num, order=0):
    if order:
        return num / 3.3
    else:
        return num * 3.3

def km_yard(num, order=0):
    if order:
        return num / 1094
    else:
        return num * 1904

def km_cm(num, order=0):
    if order:
        return num / 100000
    else:
        return num * 100000

def mile_m(num, order=0):
    if order:
        return num / 1609
    else:
        return num * 1609

def foot_inch(num, order=0):
    if order:
        return num / 12
    else:
        return num * 12

def km_inch(num, order=0):
    if order:
        return num / 39370
    else:
        return num * 39370

def km_foot(num, order=0):
    if order:
        return num / 3281
    else:
        return num * 3281

def m_yard(num, order=0):
    if order:
        return num / 1.094
    else:
        return num * 1.094

def m_inch(num, order=0):
    if order:
        return num / 39.37
    else:
        return num * 39.37

def m_mm(num, order=0):
    if order:
        return num / 1000
    else:
        return num * 1000

def cm_yard(num, order=0):
    if order:
        return num * 91.44
    else:
        return num / 91.44

def cm_mile(num, order=0):
    if order:
        return num * 160934
    else:
        return num / 160934

def yard_mile(num, order=0):
    if order:
        return num * 1760
    else:
        return num / 1760

def yard_inch(num, order=0):
    if order:
        return num / 36
    else:
        return num * 36

def yard_foot(num, order=0):
    if order:
        return num / 3
    else:
        return num * 3

def yard_mm(num, order=0):
    if order:
        return num / 914
    else:
        return num * 914

def mile_inch(num, order=0):
    if order:
        return num / 63360
    else:
        return num * 63360

def mile_foot(num, order=0):
    if order:
        return num / 5280
    else:
        return num * 5280

def mile_mm(num, order=0):
    if order:
        return num / 1609000
    else: 
        return num * 1609000

def inch_mm(num, order=0):
    if order:
        return num / 25.4
    else:
        return num * 25.4

def foot_mm(num, order=0):
    if order:
        return num / 305
    else:
        return num * 305

def km_mm(num, order=0):
    if order:
        return num / 1000000
    else:
        return num * 1000000

# MAIN FUNCTION
def compare_length(unit1, unit2, num):
    if unit1 == unit2:
        answer = num

    # km
    elif unit1 == 'km' and unit2 == 'yard':
        answer = km_yard(num)
    elif unit1 == 'yard' and unit2 == 'km':
        answer = km_yard(num, order=1)
    elif unit1 == 'km' and unit2 == 'm':
        answer = km_m(num)
    elif unit1 == 'm' and unit2 == 'km':
        answer = km_m(num, order=1)
    elif unit1 == 'km' and unit2 == 'cm':
        answer = km_cm(num)
    elif unit1 == 'cm' and unit2 == 'km':
        answer = km_cm(num, order=1)
    elif unit1 == 'km' and unit2 == 'mile':
        answer = mile_km(num, order=1)
    elif unit1 == 'mile' and unit2 == 'km':
        answer = mile_km(num)
    elif unit1 == 'km' and unit2 == 'inch':
        answer = km_inch(num)
    elif unit1 == 'inch' and unit2 == 'km':
        answer = km_inch(num, order=1)
    elif unit1 == 'km' and unit2 == 'foot':
        answer = km_foot(num)
    elif unit1 == 'foot' and unit2 == 'km':
        answer = km_foot(num, order=1)
    elif unit1 == 'km' and unit2 == 'mm':
        answer = km_mm(num)
    elif unit1 == 'mm' and unit2 == 'km':
        answer = km_mm(num, order=1)
    
    # m
    elif unit1 == 'm' and unit2 == 'cm':
        answer = m_cm(num)
    elif unit1 == 'cm' and unit2 == 'm':
        answer = m_cm(num, order=0)
    elif unit1 == 'm' and unit2 == 'yard':
        answer = m_yard(num)
    elif unit1 == 'yard' and unit2 == 'm':
        answer = m_yard(num, order=1)
    elif unit1 == 'm' and unit2 == 'mile':
        answer = mile_m(num, order=1)
    elif unit1 == 'mile' and unit2 == 'm':
        answer = mile_m(num)
    elif unit1 == 'm' and unit2 == 'inch':
        answer = m_inch(num)
    elif unit1 == 'inch' and unit2 == 'm':
        answer = m_inch(num, order=1)
    elif unit1 == 'm' and unit2 == 'foot':
        answer = foot_m(num, order=1)
    elif unit1 == 'foot' and unit2 == 'm':
        answer = foot_m(num)
    elif unit1 == 'm' and unit2 == 'mm':
        answer = m_mm(num)
    elif unit1 == 'mm' and unit2 == 'm':
        answer = m_mm(num, order=1)
    
    # cm
    elif unit1 == 'cm' and unit2 == 'yard':
        answer = cm_yard(num)
    elif unit1 == 'yard' and unit2 == 'cm':
        answer = cm_yard(num, order=1)
    elif unit1 == 'cm' and unit2 == 'mile':
        answer = cm_mile(num)
    elif unit1 == 'mile' and unit2 == 'cm':
        answer = cm_mile(num, order=1)
    elif unit1 == 'cm' and unit2 == 'inch':
        answer = inch_cm(num, order=1)
    elif unit1 == 'inch' and unit2 == 'cm':
        answer = inch_cm(num)
    elif unit1 == 'cm' and unit2 == 'foot':
        answer = foot_cm(num, order=1)
    elif unit1 == 'foot' and unit2 == 'cm':
        answer = foot_cm(num)
    elif unit1 == 'cm' and unit2 == 'mm':
        answer = cm_mm(num)
    elif unit1 == 'mm' and unit2 == 'cm':
        answer = cm_mm(num, order=1)
    
    # yard
    elif unit1 == 'yard' and unit2 == 'mile':
        answer = yard_mile(num)
    elif unit1 == 'mile' and unit2 == 'yard':
        answer = yard_mile(num, order=1)
    elif unit1 == 'yard' and unit2 == 'inch':
        answer = yard_inch(num)
    elif unit1 == 'inch' and unit2 == 'yard':
        answer = yard_inch(num, order=1)
    elif unit1 == 'yard' and unit2 == 'foot':
        answer = yard_foot(num)
    elif unit1 == 'foot' and unit2 == 'yard':
        answer = yard_foot(num, order=1)
    elif unit1 == 'yard' and unit2 == 'mm':
        answer = yard_mm(num)
    elif unit1 == 'mm' and unit2 == 'yard':
        answer = yard_mm(num, order=1)

    # mile
    elif unit1 == 'mile' and unit2 == 'inch':
        answer = mile_inch(num)
    elif unit1 == 'inch' and unit2 == 'mile':
        answer = mile_inch(num, order=1)
    elif unit1 == 'mile' and unit2 == 'foot':
        answer = mile_foot(num)
    elif unit1 == 'foot' and unit2 == 'mile':
        answer = mile_foot(num, order=1)
    elif unit1 == 'mile' and unit2 == 'mm':
        answer = mile_mm(num)
    elif unit1 == 'mm' and unit2 == 'mile':
        answer = mile_mm(num, order=1)
    
    # inch
    elif unit1 == 'inch' and unit2 == 'foot':
        answer = foot_inch(num, order=1)
    elif unit1 == 'foot' and unit2 == 'inch':
        answer = foot_inch(num)
    elif unit1 == 'inch' and unit2 == 'mm':
        answer = inch_mm(num)
    elif unit1 == 'mm' and unit2 == 'inch':
        answer = inch_mm(num, order=1)
    
    # foot
    elif unit1 == 'foot' and unit2 == 'mm':
        answer = foot_mm(num)
    elif unit1 == 'mm' and unit2 == 'foot':
        answer = foot_mm(num, order=1)

    return answer