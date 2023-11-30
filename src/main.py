from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db

app = FastAPI()


@app.post("/event/")
def catch_event(event: schemas.IncomingEvent, db: Session = Depends(get_db)):
    return crud.save_income_event(db=db, event=event)


@app.get("/event/user/{user_id}")
def get_events_by_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_events_by_user(db=db, user_id=user_id)
