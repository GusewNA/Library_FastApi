from sqlalchemy.orm import Mapped

from .base import Base

class Author(Base):
    __tablename__ = "authors"

    name: Mapped[str]