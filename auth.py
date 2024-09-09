from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token
import datetime

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

@app.route('/auth/token', methods=['POST'])
def token():
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')
    
    if client_id == 'your_client_id' and client_secret == 'your_client_secret':
        access_token = create_access_token(identity='user', expires_delta=datetime.timedelta(hours=1))
        return jsonify(access_token=access_token), 200
    return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
