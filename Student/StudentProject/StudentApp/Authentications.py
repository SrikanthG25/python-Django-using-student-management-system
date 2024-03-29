import jwt , datetime
from rest_framework import exceptions

def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2),
        'iat': datetime.datetime.utcnow()
    }, 'access_secret', algorithm='HS256')

def decode_acsess_token(token):
    try:
        payload = jwt.decode(token,'access_secret' , algorithms='HS256')
        return payload['user_id']

    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed('Access token has expired')
    
    except jwt.DecodeError:
        raise exceptions.AuthenticationFailed('Invalid access token')






















def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=2),
        'iat': datetime.datetime.utcnow()
    }, 'access_secret', algorithm='HS256')


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')

        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')