from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from core.config import settings
from sqlalchemy.orm import DeclarativeBase


# class Base(DeclarativeBase):
#     pass

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True
)

async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False
)


async def get_db():
    async with async_session() as session:
        yield session

# async def async_main():
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# if __name__ == "__main__":
#     asyncio.run(async_main())

