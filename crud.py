import asyncio

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import (
    Base,
    Book,
    DatabaseHelper,
    db_helper,
    Author,
    book_author_association
)


async def create_book(session: AsyncSession, title: str) -> Book:
    book = Book(title=title)
    session.add(book)
    await session.commit()
    return book


async def create_author(session: AsyncSession, name: str) -> Author:
    author = Author(name=name)
    session.add(author)
    await session.commit()
    return author