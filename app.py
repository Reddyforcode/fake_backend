from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/realestate")
def a():
    with open("fake_json.json") as complex_data:
        data = complex_data.read()
        # print(data)
        return data
    return "holo x2"

if __name__ == "__main__":
    app.run(host='0.0.0.0')