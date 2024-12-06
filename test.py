from flask import Flask, render_template, redirect
from gpiozero import LED
from time import strftime


app = Flask(__name__)


led = LED(16)  
last_timestamp = ""


@app.route('/led_on', methods=["POST"])
def led_on():
    global last_timestamp
    print("turning led on")

    # LED anschalten
    led.on()

    last_timestamp = "LED an: " + strftime('%x %X')

    return redirect("/")


@app.route('/led_off', methods=["POST"])
def led_off():
    global last_timestamp
    print("turning led off")

    # LED ausschalten
    led.off()

    last_timestamp = "LED aus: " + strftime('%x %X')

    return redirect("/")


@app.route('/')
def home():
    return render_template("index.html", timestamp=last_timestamp)

if __name__ == '__main__':
    # Flask-App auf der IP-Adresse und einem Port starten
    app.run(host='0.0.0.0', port=5000)
