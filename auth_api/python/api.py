from flask import Flask
from flask import jsonify
from flask import request
from methods import Token, Restricted 
from config import CFG

app = Flask(__name__)
login = Token()
protected = Restricted()


# Just a health check
@app.route("/")
def url_root():
    return "OK"


# Just a health check
@app.route("/_health")
def url_health():
    return "OK"


# e.g. http://127.0.0.1:8000/login
@app.route("/login", methods=['POST'])
def url_login():
    username = request.form['username']
    password = request.form['password']
    token = login.generate_token(username, password)

    if token is None:
        return "", 403
    
    return jsonify({"data": token}), 200


# # e.g. http://127.0.0.1:8000/protected
@app.route("/protected")
def url_protected():
    auth_token = request.headers.get('Authorization')
    auth_token = auth_token.removeprefix("Bearer ")
    print(f">>>>{auth_token=}")
    res = {
        "data": protected.access_data(auth_token)
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(**CFG["api"])
