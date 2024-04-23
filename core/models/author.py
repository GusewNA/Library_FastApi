from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship

from .base import Base
from .book_author_association import book_author_association_table

if TYPE_CHECKING:
    from .book import Book

class Author(Base):
    __tablename__ = "authors"

    name: Mapped[str]
    books: Mapped[list["Book"]] = relationship(secondary=book_author_association_table ,back_populates="authors")