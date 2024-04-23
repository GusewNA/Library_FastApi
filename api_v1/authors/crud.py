"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Author

from .schemas import AuthorCreate, AuthorUpdate, AuthorUpdatePartial


async def get_authors(session: AsyncSession) -> list[Author]:
    stmt = select(Author).order_by(Author.id)
    result: Result = await session.execute(stmt)
    authors = result.scalars().all()
    return list(authors)


async def get_author(session: AsyncSession, author_id: int) -> Author | None:
    return await session.get(Author, author_id)


async def create_author(session: AsyncSession, author_id: AuthorCreate) -> Author:
    author = Author(**author_id.model_dump())
    session.add(author)
    await session.commit()
    # await session.refresh(product)
    return author


async def update_author(
        session: AsyncSession,
        author: Author,
        author_update: AuthorUpdate | AuthorUpdatePartial,
        partial: bool = False,
) -> Author:
    for name, value in author_update.model_dump(exclude_unset=partial).items():
        setattr(author, name, value)
    await session.commit()
    return author


async def delete_author(
        session: AsyncSession,
        author: Author,
) -> None:
    await session.delete(author)
    await session.commit()
