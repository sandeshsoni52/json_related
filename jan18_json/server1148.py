from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def serve_json():
    with open('data.json') as f:
        data = f.read()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
