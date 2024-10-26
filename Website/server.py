from flask import Flask, render_template, request, redirect
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import json

app = Flask(__name__)


@app.route("/")
def index():
    plt.plot([i for i in range(10)], [i + 1 for i in range(10)])
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    img_data = base64.b64encode(img_buffer.read()).decode()
    return render_template("index.html", name = 'new_plot', chart_data=img_data)


@app.route("/predictor")
def predictor():
    return render_template("predictor.html")

@app.route("/comparison")
def comparison():
    return render_template("comparison.html")

@app.route("/sustainability")
def sustainability():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        opposition = request.form['opposition']
        place = request.form['place']
        playerList = request.form.get('inputList')
        # playerList = json.loads(playerList)
        print(opposition)
        print(playerList)
        print(place)
        return redirect("/comparison")
    
    return redirect("/")

@app.route("/filter", methods=["POST", "GET"])
def filter():
    if request.method == "POST":
        teams = request.form.getlist('team')
        stats = request.form.getlist('stat')
        print(teams)
        print(stats)
        return "check terminal"
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
