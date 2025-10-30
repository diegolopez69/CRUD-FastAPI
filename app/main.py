from fastapi import FastAPI
from app.db import Base, engine
from app.routes import router as routes_router

# Create the tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register routes
app.include_router(routes_router)

@app.get("/")
def alive():
    return {"Message": "I'm alive"}