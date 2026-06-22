from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # other middlewares from starlette
# Cross Origin Resource Sharing (CORS) is a security feature implemented by web browsers to restrict 
# web applications running on one origin (domain) from accessing resources on a different origin. 

# CORS is a mechanism that allows servers to specify who can access their resources and how they can be accessed. 

# Lets say Frontend: https://dashboard.mycompany.com , Backend API: https://api.mycompany.com
# Because these are different origins, the browser will block the frontend from talking to your backend by default. 
# CORS is a relaxation of this strict policy.


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://my-frontend.com', 'http://localhost:3000' # localhost frontend uri
    ],
    allow_credentials=True, # get the browser send cookies?
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['*']
)

# define endpoints