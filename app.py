from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"
@app.route("/flutter", methods =['GET', 'POST'])
def flutter():
    with open("flutter.json") as data_json:
        data = data_json.read()
        return data
    return "json not found"

@app.route("/realestate")
def a():
    with open("fake_json.json") as complex_data:
        data = complex_data.read()
        # print(data)
        return data
    return "holo x2"

if __name__ == "__main__":
    app.run(host='0.0.0.0')