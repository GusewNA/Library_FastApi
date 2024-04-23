from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
# from .dependencies import product_by_id
from .schemas import Book, BookCreate, BookUpdate, BookUpdatePartial

router = APIRouter(prefix="/books")


@router.get("/", response_model=list[Book])
async def get_products(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_books(session=session)


@router.post(
    "/",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
        book_id: BookCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_book(session=session, book_id=book_id)
