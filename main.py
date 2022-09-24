from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {
        "name":"akash",
        "age":45,
        "city":"gondia"
    }

@app.route("/contact")
def hello_wold():
    return "<h1>This is contact page</h1>"

# if __name__ == "__main__":
#     app.run(debug=True)
app.run(host="0.0.0.0", port=4545)