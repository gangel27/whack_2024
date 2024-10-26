from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64
import json

app = Flask(__name__)


@app.route("/")
def index():
    
    return render_template("index.html", )


@app.route("/data", methods=["GET"])
def returnData():
    with open("data.txt") as file:
        data = file.read()
    print(data)
    return data, 200


@app.route("/post", methods=["POST"])
def get_post_javascript_data():
    jsdata = request.form.to_dict(flat=False)
    print(jsdata)
    with open("data.txt", "w") as file:
        file.truncate(0)
        file.write(jsdata["data"][0])

    return jsdata, 200


@app.route("/json", methods=["GET"])
def sendjson():
    with open("data.json", "r") as j:
        contents = json.loads(j.read())
        print(contents["data"])
    return contents, 200


if __name__ == "__main__":
    app.run()
