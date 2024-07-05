from flask import Flask, request, jsonify


app = Flask(__name__)

DATA_FILE = '/data/data.txt'

@app.route('/')
def home():
    return 'Hello, World! This is an example Flask app!'

@app.route('/write', methods=['POST'])
def write_data():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    with open (DATA_FILE, 'w', encoding='utf-8') as file:
        file.write(data + '\n')
    
    return jsonify({'message': 'Data written'}), 200


@app.route('/read', methods=['GET'])
def read_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return jsonify({'data': file.readlines()}), 200
    except Exception as error:
        return jsonify({'error': error}), 404
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
