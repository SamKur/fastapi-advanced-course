from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()

API_KEY = 'my-secret-key' # hardcoded constant for demo


def get_api_key(api_key: str = Header(...)): # key in header?
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail='Unauthorized')
    return api_key


@app.get('/get-data') # run -> curl.exe -i -H "api-key: my-secret-key" http://localhost:8000/get-data OR pass in header of like postman
def get_data(api_key: str = Depends(get_api_key)):
    return {'output': 'Access Granted!'} 