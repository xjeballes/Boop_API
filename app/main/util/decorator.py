from functools import wraps
from flask import request
from app.main.services.user_service import get_logged_in_user

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user = get_logged_in_user(request)

        if not user:
            api.abort(401)

        return f(*args, **kwargs)

    return decorated

def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = get_logged_in_user(request)

        token = data.get("data")

        if not token:
            return data, status

        admin = token.get("admin")

        if not admin:
            response_object = {
                "status" : "fail",
                "message" : "Administrative token is required."
            }

            return response_object, 401

        return f(*args, **kwargs)

    return decorated
