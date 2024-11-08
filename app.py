from flask import Flask, render_template, request
app = Flask(__name__)

# Variables de control
target_temperature = 25  # Temperatura inicial
agitator_speed = 100     # Velocidad inicial del agitador (RPM)

@app.route("/", methods=["GET", "POST"])
def index():
    global target_temperature, agitator_speed
    if request.method == "POST":
        target_temperature = float(request.form["temperature"])
        agitator_speed = int(request.form["agitator_speed"])
    return render_template("index.html", temperature=target_temperature, agitator_speed=agitator_speed)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
