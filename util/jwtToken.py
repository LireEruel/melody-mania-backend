import jwt

def generate_jwt(user_id):
    payload = {"user_id": user_id}
    secret_key = "my-secret-key"
    algorithm = "HS256"
    jwt_token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return jwt_token