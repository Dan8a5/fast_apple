import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from db import get_session
from models.ceos import Ceo
app = FastAPI()

@app.get("/") # where we define where out routes are
def root():
    return {"message": "Hello World"}

@app.get("/ceos")
def list_ceos(session: Session = Depends(get_session)):
    statement = select(Ceo)
    print(f"SQL STATEMENT: {statement}")
    results = session.exec(statement)
    return results.all()


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

    # if using fastapi use this "boiler plate" to start, you will need to add other things for other projects