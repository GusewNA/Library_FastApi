from sqlalchemy.orm import Mapped

from .base import Base

class Book(Base):
    __tablename__ = "books"

    title: Mapped[str]

