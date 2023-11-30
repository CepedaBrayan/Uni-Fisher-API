from pydantic import BaseModel


class IncomingEvent(BaseModel):
    customer_id: int
    event_type: str = None
    timestamp: str = None
    email_id: int = None
    product_id: int = None
    clicked_link: str = None
