from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import author_by_id
from .schemas import Author, AuthorCreate, AuthorUpdate, AuthorUpdatePartial

router = APIRouter(prefix="/authors")


@router.get("/", response_model=list[Author])
async def get_authors(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_authors(session=session)


@router.post(
    "/",
    response_model=Author,
    status_code=status.HTTP_201_CREATED,
)
async def create_author(
        author_id: AuthorCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_author(session=session, author_id=author_id)


@router.get("/{author_id}/", response_model=Author)
async def get_author(
        author: Author = Depends(author_by_id),
):
    return author


@router.put("/{author_id}/")
async def update_author(
        author_update: AuthorUpdate,
        author: Author = Depends(author_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_author(
        session=session,
        author=author,
        author_update=author_update,
    )


@router.patch("/{author_id}/")
async def update_author_partial(
        author_update: AuthorUpdatePartial,
        author: Author = Depends(author_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_author(
        session=session,
        author=author,
        author_update=author_update,
        partial=True,
    )


@router.delete("/{author_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(
        author: Author = Depends(author_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_author(session=session, author=author)
