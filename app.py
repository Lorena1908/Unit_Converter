from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Conversion factors
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

OPTIONS = ["Select Unit",
            "Centimeter",
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

@app.route('/')
def index():
    return render_template('index.html', OPTIONS=OPTIONS)

@app.route('/main', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        num = request.form['num']
        if num.isnumeric():
            num = int(num)
        else:
            not_number = True
            return render_template('index.html', OPTIONS=OPTIONS, num=num, answer='', not_number=not_number)
        unit1 = request.form['unit1']
        unit2 = request.form['unit2']

        type_of_unit = [unit1 in length and unit2 in length, unit1 in mass and unit2 in mass,
                        unit1 in temperature and unit2 in temperature, unit1 in area and unit2 in area,
                        unit1 in volume and unit2 in volume]

        if any(type_of_unit):
            if unit1 == unit2:
                answer = num
            elif unit1 == 'Celsius' and unit2 == 'Fahrenheit':
                answer = (num * 1.8) + 32
            elif unit1 == 'Fahrenheit' and unit2 == 'Celsius':
                answer = (num - 32) * 5/9
            elif unit1 == 'Celsius' and unit2 == 'Kelvin':
                answer = num + 273
            elif unit1 == 'Kelvin' and unit2 == 'Celcius':
                answer = num - 273
            elif unit1 == 'Fahrenheit' and unit2 == 'Kelvin':
                answer = (num - 32) * 5/9 + 273
            elif unit1 == 'Kelvin' and unit2 == 'Fahrenheit':
                answer = (num - 273) * 9/5 + 32
            else:
                answer = round(num * unit_dict[unit1]/unit_dict[unit2], 5)
            return render_template('index.html', OPTIONS=OPTIONS, num=num, answer=answer, unit1=unit1, unit2=unit2)
        else:
            different_type = True
            return render_template('index.html', OPTIONS=OPTIONS, num=num, answer='', different_type=different_type)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)