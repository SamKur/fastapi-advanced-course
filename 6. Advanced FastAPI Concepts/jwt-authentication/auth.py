from datetime import datetime, timedelta, timezone
from authlib.jose import JoseError, jwt
from fastapi import HTTPException

# constants - in prod use secure vault or dotenv or yaml
SECRET_KEY = 'my_secret'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRY_MINUTES = 30


# functions
def create_access_token(data: dict):
    header = {'alg': ALGORITHM}
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    payload = data.copy()
    payload.update({'exp': expire})
    return jwt.encode(header, payload, SECRET_KEY).decode('utf-8')

"""
# Turn below auth into a dependency by -
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
def get_current_user(token: str = Depends(oauth2_scheme)): same code
"""
def verify_token(token: str):   # better if turned into a dependency
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()
        username = claims.get('sub')
        if username is None:
            raise HTTPException(status_code=401, detail='Token missing')
        return username
    except JoseError:
        raise HTTPException(status_code=401, detail="Couldn't Validate Credentials")