from fastapi import FastAPI, Depends

app = FastAPI()


# dependency function # why DI? Reusability, Readability, Replaceability
def get_db():
    # db = SessionLocal() # This is example of a real Database Session object
    db = {'connection': 'mock_db_connection'}
    try:
        yield db
    finally:
        # db.close()
        print("Cleaning up: Fake database connection 'closed'")


# endpoint
@app.get('/home')
def home(db=Depends(get_db)):   # This is Dependency Injection, externally fed
    return {'db_status': db['connection']}