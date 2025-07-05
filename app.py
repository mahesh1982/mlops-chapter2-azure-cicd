# app.py
from flask import Flask, request, jsonify
from add import add

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def do_add():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    result = add(a, b)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
