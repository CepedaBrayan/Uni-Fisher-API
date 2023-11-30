from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_events_by_user(db: Session, user_id: int):
    return db.query(models.Event).filter(models.Event.customer_id == user_id).all()


def save_income_event(db: Session, event: schemas.IncomingEvent):
    # create the user if it doesn't exist
    db_user = db.query(models.User).filter(models.User.id == event.customer_id).first()
    if not db_user:
        db_user = models.User(id=event.customer_id)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

    # create the email if it doesn't exist
    db_email = db.query(models.Email).filter(models.Email.id == event.email_id).first()
    if not db_email:
        db_email = models.Email(id=event.email_id)
        db.add(db_email)
        db.commit()
        db.refresh(db_email)

    # create the product if it doesn't exist
    db_product = (
        db.query(models.Product).filter(models.Product.id == event.product_id).first()
    )
    if not db_product:
        db_product = models.Product(id=event.product_id)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)

    # create the event
    db_event = models.Event(
        event_type=event.event_type,
        timestamp=event.timestamp,
        clicked_link=event.clicked_link,
        customer_id=event.customer_id,
        email_id=event.email_id,
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
