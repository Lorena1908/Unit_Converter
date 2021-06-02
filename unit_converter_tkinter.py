from tkinter import *
import tkinter.font as tkFont

unit_dict = {
    "Centimeter" : 0.01,
    "Meter" : 1,
    "Kilometer": 1000,
    "Feet": 0.3048,
    "Miles": 1609.344,
    "Inches": 0.0254,
    "Grams" : 1,
    "Kilograms" : 1000,
    "Quintals": 100000,
    "Tonnes" : 1000000,
    "Pounds" : 453.592,
    "Square Meter" : 1,
    "Square Kilometer": 1000000,
    "Are" : 100,
    "Hectare" : 10000,
    "Acre": 4046.856,
    "Square Mile" : 2590000,
    "Square Foot" : 0.0929,
    "Cubic Centimeter" : 0.001,
    "Litre" : 1,
    "Mililiter" : 0.001,
    "Gallon": 3.785,
    "Yards": 0.9144,
    "Miligram": 0.001
}

length = ["Centimeter", "Meter", "Kilometer", "Feet", "Files", "Inches", "Yards"]
mass = ["Kilograms", "Grams", "Quintals", "Tonnes", "Pounds",'Miligram']
temperature = ["Celsius", "Fahrenheit", "Kelvin"]
area = ["Square Meter", "Square Kilometer", "Are", "Hectare", "Acre", "Square Mile", "Square Foot"]
volume = ["Cubic Centimeter", "Litre", "Mililiter", "Gallon"]

OPTIONS = ["Centimeter",
            "Meter",
            "Kilometer",
            "Feet",
            "Miles",
            "Inches",
            "Yards",
            "Kilograms",
            "Grams",
            "Quintals",
            "Tonnes",
            "Pounds",
            "Miligram",
            "Celsius",
            "Fahrenheit",
            "Kelvin",
            "Square Meter",
            "Square Kilometer",
            "Are",
            "Hectare",
            "Acre",
            "Square Mile",
            "Square Foot",
            "Cubic Centimeter",
            "Litre",
            "Mililiter",
            "Gallon"]

root = Tk()
root.config(bg='grey')
root.geometry('530x270')
root.title('Unit Converter')

def calculate():
    input_num = input_entry.get()
    inp_unit = unit1.get()
    out_unit = unit2.get()

    type_of_unit = [inp_unit in length and out_unit in length, inp_unit in mass and out_unit in mass,
    inp_unit in temperature and out_unit in temperature, inp_unit in area and out_unit in area,
    inp_unit in volume and out_unit in volume]

    if input_num.isnumeric():
        input_num = float(input_num)
    else:
        output_entry.delete(0, END)
        output_entry.insert(0, 'ERROR')

    if any(type_of_unit):
        if inp_unit == out_unit:
            answer = input_num
        elif inp_unit == 'Celsius' and out_unit == 'Fahrenheit':
            answer = (input_num * 1.8) + 32
        elif inp_unit == 'Fahrenheit' and out_unit == 'Celsius':
            answer = (input_num - 32) * 5/9
        elif inp_unit == 'Celsius' and out_unit == 'Kelvin':
            answer = input_num + 273
        elif inp_unit == 'Kelvin' and out_unit == 'Celcius':
            answer = input_num - 273
        elif inp_unit == 'Fahrenheit' and out_unit == 'Kelvin':
            answer = (input_num - 32) * 5/9 + 273
        elif inp_unit == 'Kelvin' and out_unit == 'Fahrenheit':
            answer = (input_num - 273) * 9/5 + 32
        else:
            answer = round(input_num * unit_dict[inp_unit]/unit_dict[out_unit], 5)
        output_entry.delete(0, END)
        output_entry.insert(0, answer)
    else:
        output_entry.delete(0, END)
        output_entry.insert(0, 'ERROR')

# FONT
font = tkFont.Font( size=12)

# VARIABLES
unit1 = StringVar()
unit2 = StringVar()

unit1.set('Select a Unit')
unit2.set('Select a Unit')

# LABELS
input_lbl = Label(root, text='Enter a input_Number:', bg='grey', fg='white', font=font)
output_lbl = Label(root, text='Here is the result:', bg='grey', fg='white', font=font)
title = Label(root, text='Unit Converter', bg='grey', fg='white', font='bold')

# CONVERSION NUMBERS
input_entry = Entry(root, justify='center', font='bold')
output_entry = Entry(root, justify='center', font='bold')

# DROPDOWN MENUS
input_unit = OptionMenu(root, unit1, *OPTIONS)
output_unit = OptionMenu(root, unit2, *OPTIONS)

# BUTTONS
submit_btn = Button(root, text='Calculate', command=calculate)

# DISPLAY ON SCREEN
input_lbl.grid(row=1, column=0, padx=20, pady=10)
output_lbl.grid(row=1, column=1, padx=20, pady=10)
title.grid(row=0, column=0, columnspan=2, pady=15)

input_entry.grid(row=2, column=0, padx=20, ipady=5)
output_entry.grid(row=2, column=1, padx=20, ipady=5)

input_unit.grid(row=3, column=0, padx=20, pady=20)
output_unit.grid(row=3, column=1, padx=20, pady=20)

submit_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, ipadx=100, ipady=3)

root.mainloop()