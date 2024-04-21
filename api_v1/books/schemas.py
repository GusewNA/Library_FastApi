from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    title: str

class BookCreate(BookBase):
    pass

class BookUpdate(BookCreate):
    pass

class BookUpdatePartial(BookCreate):
    title: str | None = None


class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)

    id: int