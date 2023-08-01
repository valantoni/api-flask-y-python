from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
from flask_cors import CORS  # Import the CORS extension

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

# Initialize Firebase
cred = credentials.Certificate("firebase-credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'databaseurl'
})


# Define the API
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
    
        data = request.get_json()

        
        name = data['name']
        email = data['email']

        
        ref = db.reference('emails')
        new_email_ref = ref.push()
        new_email_ref.set({
            'name': name,
            'email': email
        })
        
        return jsonify({"message": "Email saved successfully!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
