# These functions need to be implemented
from dbconnect import Session
import hashlib
import jwt
from config import CFG
from dbconnect import get_userdata

SECRET_KEY=CFG["jwt"]["secret"]

def salted_password(password, salt):
    return hashlib.sha512((password+salt).encode()).hexdigest()



class Token:

    def generate_token(self, username, password):
        result = get_userdata(username)
        if result.username==username and result.password== salted_password(password, result.salt):
            return jwt.encode(payload={"role": result.role}, key=SECRET_KEY)


    def decrypt_token(self, token):
        return jwt.decode(token, SECRET_KEY, algorithms="HS256")



class Restricted:

    def access_data(self, authorization):
        decoded = Token().decrypt_token(authorization)
        print(f"decoded--->{decoded}")
        if "role" in decoded and decoded["role"] in ["editor", "admin"]:
            return 'You are under protected data'
