from fastapi import FastAPI, Depends

app = FastAPI()


class Settings:
    def __init__(self):
        self.api_key = 'my_secret'
        self.debug = True
        print("more intensive setup for settings, like reading from env variables or a config file")

def get_settings():
    return Settings()

@app.get('/config')
def get_config(settings: Settings = Depends(get_settings)): # DI for config management, Depends only takes a callable (function, class, lambda function)
    return {'api_key': settings.api_key}