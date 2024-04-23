from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship

from .base import Base
from .book_author_association import book_author_association_table

if TYPE_CHECKING:
    from .author import Author

class Book(Base):
    __tablename__ = "books"

    title: Mapped[str]
    authors: Mapped[list["Author"]] = relationship(secondary=book_author_association_table, back_populates="books")

