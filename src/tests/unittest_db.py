import pytest
from dotenv import load_dotenv

from src.database import TrxRequestsDB

load_dotenv()


@pytest.mark.asyncio
async def test_write():
    trx_requests_db = TrxRequestsDB()
    # write
    record_id = await trx_requests_db.add_request(trx_address="address1", bandwidth=0, energy=0, balance=0)
    assert isinstance(record_id, int)
    # delete
    record_id = await trx_requests_db.delete_request(record_id)
    assert isinstance(record_id, int)
