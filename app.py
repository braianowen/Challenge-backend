from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required
from graphql import schema
from flask_graphql import GraphQLView
from auth import app as auth_app

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

app.register_blueprint(auth_app)

@app.route('/')
def home():
    return jsonify(message="API is running")

# Protegemos el endpoint GraphQL
@app.add_url_rule(
    '/graphql',
    view_func=jwt_required()(GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    ))
)

if __name__ == '__main__':
    app.run(debug=True)
