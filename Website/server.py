from flask import Flask, render_template, request, redirect
import matplotlib
from integration import Integration
import numpy as np
import json

import matplotlib.pyplot as plt
import io
import base64
import json

from spiderDiagrams import SpiderDiagrams

matplotlib.use("Agg")


app = Flask(__name__)


@app.route("/")
def index():
    # plt.plot([i for i in range(10)], [i + 1 for i in range(10)])
    # img_buffer = io.BytesIO()
    # plt.savefig(img_buffer, format="png")
    # img_buffer.seek(0)
    # img_data = base64.b64encode(img_buffer.read()).decode()
    return render_template("index.html")


@app.route("/predictor")
def predictor():
    return render_template("predictor.html")


@app.route("/comparison")
def comparison():
    return render_template("comparison.html", chart="")


@app.route("/sustainability")
def sustainability():
    return render_template("index.html")


@app.route("/pred_results")
def pred_results():
    return render_template("pred_results.html")


@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        opposition = request.form["opposition"]
        place = request.form["place"]
        playerList = request.form.get("inputList")

        # playerList = json.loads(playerList)
        playerList = np.array(json.loads(playerList)).astype(float)

        predictor = Integration(opposition, playerList, place)
        loss, draw, win = predictor.predict()
        loss, draw, win = (
            round(loss * 100, 1),
            round(draw * 100, 1),
            round(win * 100, 1),
        )

    return render_template("pred_results.html", loss=loss, draw=draw, win=win)


@app.route("/filter", methods=["POST", "GET"])
def filter():
    if request.method == "POST":
        teams = request.form.getlist("team")
        stats = request.form.getlist("stat")
        print(teams)
        print(stats)
        SpiderDiagramMaker = SpiderDiagrams()
        plt = SpiderDiagramMaker.plot_average_radar(teams, stats)
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format="png")
        img_buffer.seek(0)
        img_data = base64.b64encode(img_buffer.read()).decode()
        # # Example usage
        # teams = ['Reading', 'Millwall', 'Brentford']  # Replace with your teams
        # selected_stats = ['possession', 'np_xg', 'shots', 'pressures', 'tackles', 'goals_conceded']  # Replace with your stats
        # plot_average_radar(teams, selected_stats)

    return render_template("comparison.html", chart=img_data)


if __name__ == "__main__":
    app.run(debug=True)
