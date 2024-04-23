from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint
from .base import Base

book_author_association_table = Table(
    "book_author_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", ForeignKey("books.id"), primary_key=True, nullable=False),
    Column("author_id", ForeignKey("authors.id"), primary_key=True, nullable=False),
    UniqueConstraint("book_id", "author_id", name="idx_unique_book_author")
)