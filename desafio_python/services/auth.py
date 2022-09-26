from fastapi import HTTPException
from ..helpers.auth import SECRET_JWT

import jwt
import time


class AuthService:
    def __init__(self):
        pass

    def generate_token(self):
        return jwt.encode(
            {
                "payload": "047a9dd00a76b8237094f519fa08dbc0",
                "exp": int(time.time() + 3600),
            },
            SECRET_JWT,
            algorithm="HS256",
        )

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, SECRET_JWT, ["HS256"])
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, jwt.DecodeError):
            raise HTTPException(403, "Token error")
        except Exception as e:
            raise HTTPException(500, "Server error")
