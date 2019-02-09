from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')

def hello():
    return jsonify({"about" : "Testing"}) 

@app.route('/data')
def data():
    return "Data empty"

if __name__ == "__main__":
    app.run(debug=True)
