from pydantic import BaseModel


class Cars(BaseModel):
    id: str
    name: str
    company: str
    price: int
    admin_id: str = None