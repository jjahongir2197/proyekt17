import jwt
import datetime

SECRET = "supersecret"

def create_access_token(user_id):
    return jwt.encode({
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    }, SECRET, algorithm="HS256")

def create_refresh_token(user_id):
    return jwt.encode({
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }, SECRET, algorithm="HS256")

access = create_access_token(1)
refresh = create_refresh_token(1)

print(access)
print(refresh)
