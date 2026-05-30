from fastapi import FastAPI, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# 1. Define the Security Scheme. 
# tokenUrl tells Swagger UI where to send the username/password to get a token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='mera_token') 

@app.post('/mera_token') 
def login(username: str = Form(...), password: str = Form(...)): 
    """
    Step A: The Exchange.
    The user provides credentials; if valid, we provide a 'key' (token).
    """
    if username == 'john' and password == 'pass123':
        return {'access_token': 'mera_valid_token', 'token_type': 'bearer'}
    
    raise HTTPException(status_code=400, detail='Invalid Credentials')


def decode_token(token: str): 
    """
    Step C: The Validation.
    In production, this would use a library (like PyJWT) to verify 
    the token's signature and expiration.
    """
    if token == 'mera_valid_token': 
        return {'name': 'john'}
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid Authentication Credentials'
    )


def get_current_user(token: str = Depends(oauth2_scheme)): 
    """
    Step B: The Extraction.
    Depends(oauth2_scheme) automatically looks for the 'Authorization: Bearer <token>' 
    header in the incoming request and passes the token string here.
    """
    return decode_token(token)


@app.get('/profile') 
def get_profile(user=Depends(get_current_user)):
    """
    Step D: The Protected Endpoint.
    This function only executes if 'get_current_user' successfully returns a user.
    If the token was missing or invalid, FastAPI returns 401 before this even runs.
    """
    return {'username': user['name']}