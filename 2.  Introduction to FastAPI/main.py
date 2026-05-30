from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, FastAPI!'}

# run the app using: uvicorn main:app --reload
# OR
# fastapi dev
# fastapi dev main:app
# fastapi dev main.py
# fasapi run main:app # this is for production, it will not auto reload on code changes,...
# ...and also it will not show the swagger docs, so use this only when you are ready to deploy your app

# This block only runs if you use 'python main.py'
import uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)