from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import book_by_id
from .schemas import Book, BookCreate, BookUpdate, BookUpdatePartial

router = APIRouter(prefix="/books")


@router.get("/", response_model=list[Book])
async def get_books(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_books(session=session)


@router.post(
    "/",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
)
async def create_book(
        book_id: BookCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_book(session=session, book_id=book_id)


@router.get("/{book_id}/", response_model=Book)
async def get_book(
        book: Book = Depends(book_by_id),
):
    return book


@router.put("/{book_id}/")
async def update_book(
        book_update: BookUpdate,
        book: Book = Depends(book_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_book(
        session=session,
        book=book,
        book_update=book_update,
    )


@router.patch("/{book_id}/")
async def update_book_partial(
        book_update: BookUpdatePartial,
        book: Book = Depends(book_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_book(
        session=session,
        book=book,
        book_update=book_update,
        partial=True,
    )


@router.delete("/{book_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
        book: Book = Depends(book_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_book(session=session, book=book)
