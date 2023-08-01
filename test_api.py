from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def api_endpoint():
    data = request.get_json()

    if data is not None and 'name' in data and 'email' in data:
        variable1_value = data['name']
        variable2_value = data['email']
        print("name :", variable1_value)
        print("email 2:", variable2_value)
        return jsonify({'message': 'Variables printed successfully'})
    else:
        return jsonify({'error': 'Invalid request data'}), 400

    

if __name__ == '__main__':
    app.run(debug=True)
