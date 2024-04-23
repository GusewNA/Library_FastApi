from pydantic import BaseModel, ConfigDict


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorCreate):
    pass


class AuthorUpdatePartial(AuthorCreate):
    name: str | None = None


class Author(AuthorBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
