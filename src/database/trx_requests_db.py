from os import environ
from typing import List

from sqlalchemy import create_engine, select, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from .models import TrxRequestsTable
from .models.base import Base


class TrxRequestsDB:
    def __init__(self):
        self._engine = create_async_engine("postgresql+psycopg://{0}:{1}@{2}:{3}/{4}".format(
            environ.get("POSTGRES_USER"),
            environ.get("POSTGRES_PASSWORD"),
            environ.get("POSTGRES_HOST"),
            environ.get("POSTGRES_PORT"),
            environ.get("POSTGRES_DB")
        ))
        self._async_session = sessionmaker(self._engine, expire_on_commit=False, class_=AsyncSession)

        self._create_database_if_not_exists()
        self._create_tables_if_not_exists()

    def _create_database_if_not_exists(self):
        if not (database_exists(self._engine.url)):
            create_database(self._engine.url)

    def _create_tables_if_not_exists(self):
        engine = create_engine(self._engine.url)
        Base.metadata.create_all(engine)

    async def add_request(self, trx_address: str, bandwidth: int, energy: int, balance: float) -> int:
        async with self._async_session() as session:
            session: AsyncSession = session
            q = insert(TrxRequestsTable).values(
                trx_address=trx_address,
                bandwidth=bandwidth,
                energy=energy,
                balance=balance
            ).returning(TrxRequestsTable._id)
            result = await session.execute(q)
            await session.commit()
            return int(result.first()[0])

    async def delete_request(self, _id: int) -> int:
        async with self._async_session() as session:
            session: AsyncSession = session
            q = delete(TrxRequestsTable).where(TrxRequestsTable._id == _id).returning(TrxRequestsTable._id)
            result = await session.execute(q)
            await session.commit()
            return int(result.first()[0])

    async def get_requests(self, limit: int = 10, page_index: int = 0) -> List[TrxRequestsTable]:
        async with self._async_session() as session:
            q = select(TrxRequestsTable).limit(limit).offset(page_index * limit)
            result = await session.execute(q)
            return [result[0] for result in result.all()]
