from db.config import async_session
from db.book.loader import BookLoader


async def get_book_dal():
    async with async_session() as session:
        async with session.begin():
            yield BookLoader(session)
