from flask import Flask, render_template, request
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


# @app.route("/data", methods=["GET"])
# def returnData():
#     with open("data.txt") as file:
#         data = file.read()
#     print(data)
#     return data, 200


# @app.route("/post", methods=["POST"])
# def get_post_javascript_data():
#     jsdata = request.form.to_dict(flat=False)
#     print(jsdata)
#     with open("data.txt", "w") as file:
#         file.truncate(0)
#         file.write(jsdata["data"][0])

#     return jsdata, 200


# @app.route("/json", methods=["GET"])
# def sendjson():
#     with open("data.json", "r") as j:
#         contents = json.loads(j.read())
#         print(contents["data"])
#     return contents, 200


if __name__ == "__main__":
    app.run(debug=True)
