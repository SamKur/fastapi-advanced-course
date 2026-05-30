from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # other middlewares from starlette
# Cross Origin Resource Sharing (CORS) is a security feature implemented by web browsers to restrict web applications running on one origin (domain) from accessing resources on a different origin. 
# CORS is a mechanism that allows servers to specify who can access their resources and how they can be accessed. 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://my-frontend.com', 'http://localhost:3000'
    ],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['*']
)

# define endpoints