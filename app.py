from flask import Flask, render_template, request, url_for, redirect
from types_of_units import length, area, pressure, temperature, mass, time, volume, speed, energy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_type', methods=['POST', 'GET'])
def get_type():
    if request.method == 'POST':
        type = request.form['type']
        return render_template('index.html', type=type)

@app.route('/main', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        num = request.form['num']
        if num.isnumeric():
            num = int(num)
        else:
            return "<h1>Enter a number</h1><a href='/'>Go Back</a>"
        unit1 = request.form['unit1']
        unit2 = request.form['unit2']
        
        try:
            answer = length.compare_length(unit1, unit2, num)
            return render_template('index.html', type='length', num=num, answer=answer)
        except:
            pass
        
        try:
            answer = area.compare_area(unit1, unit2, num)
            return render_template('index.html', type='area', num=num, answer=answer)
        except:
            pass
        
        try:
            answer = pressure.compare_pressure(unit1, unit2, num)
            return render_template('index.html', type='pressure', num=num, answer=answer)
        except:
            pass

        try:
            answer = temperature.compare_temperature(unit1, unit2, num)
            return render_template('index.html', type='temperature', num=num, answer=answer)
        except:
            pass
        
        try:
            answer = mass.compare_mass(unit1, unit2, num)
            return render_template('index.html', type='mass', num=num, answer=answer)
        except:
            pass

        try:
            answer = time.compare_time(unit1, unit2, num)
            return render_template('index.html', type='time', num=num, answer=answer)
        except:
            pass

        try:
            answer = volume.compare_volume(unit1, unit2, num)
            return render_template('index.html', type='volume', num=num, answer=answer)
        except:
            pass

        try:
            answer = speed.compare_speed(unit1, unit2, num)
            return render_template('index.html', type='speed', num=num, answer=answer)
        except:
            pass

        try:
            answer = energy.compare_energy(unit1, unit2, num)
            return render_template('index.html', type='energy', num=num, answer=answer)
        except:
            pass
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)