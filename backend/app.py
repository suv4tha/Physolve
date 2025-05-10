from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    formula = data['formula']
    inputs = data['inputs']

    try:
        result = {}
        if formula == "average_speed":
            result['Average Speed (S)'] = float(inputs['d']) / float(inputs['t'])

        elif formula == "acceleration":
            result['Acceleration (a)'] = (float(inputs['v']) - float(inputs['u'])) / float(inputs['t'])

        elif formula == "density":
            result['Density (ρ)'] = float(inputs['m']) / float(inputs['V'])

        elif formula == "power":
            result['Power (P)'] = float(inputs['W']) / float(inputs['t'])

        elif formula == "newtons_2nd":
            result['Force (F)'] = float(inputs['m']) * float(inputs['a'])

        elif formula == "weight":
            result['Weight (W)'] = float(inputs['m']) * float(inputs['g'])

        elif formula == "pressure":
            result['Pressure (P)'] = float(inputs['F']) / float(inputs['A'])

        elif formula == "ohms_law":
            result['Voltage (V)'] = float(inputs['I']) * float(inputs['R'])

        elif formula == "kinetic_energy":
            result['Kinetic Energy (E)'] = 0.5 * float(inputs['m']) * float(inputs['v'])**2

        elif formula == "pendulum":
            result['Pendulum Time (T)'] = 2 * math.pi * math.sqrt(float(inputs['L']) / float(inputs['g']))

        # Add the remaining formulas similarly...

        else:
            return jsonify({'error': 'Formula not implemented yet'}), 400

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
