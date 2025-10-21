from flask import Flask, render_template
import serial
import time

app = Flask(__name__)

# Percorso della porta seriale del tuo Arduino
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

@app.route('/')
def index():
    data = ""
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            data = ser.readline().decode('utf-8').strip()
    except Exception as e:
        data = f"Errore: {e}"
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
