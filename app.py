from flask import Flask

app = Flask(__name__)

#adding more after / will change location hosted after localhost:5000
@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)