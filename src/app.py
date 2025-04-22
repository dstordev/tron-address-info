from os import environ
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from database import TrxRequestsDB
from models import TrxAddressInfo, DatabaseRecord
from trx import TrxAddress

load_dotenv()

trx_requests_db = TrxRequestsDB()

app = FastAPI()


class AddressInfoRequestData(BaseModel):
    address: str


@app.post("/address/info")
async def address_info(address_info_request: AddressInfoRequestData) -> TrxAddressInfo:
    trx_address = TrxAddress(address_info_request.address, environ.get("trongrid_api_key"))
    trx_address_info = TrxAddressInfo(
        bandwidth=await trx_address.get_bandwidth(),
        energy=await trx_address.get_energy(),
        balance=await trx_address.get_balance()
    )
    await trx_requests_db.add_request(
        trx_address=address_info_request.address,
        bandwidth=trx_address_info.bandwidth,
        energy=trx_address_info.energy,
        balance=trx_address_info.balance
    )
    return trx_address_info


@app.get("/records/recent")
async def records_recent(limit: int = 10, page_index: int = 0) -> List[DatabaseRecord]:
    results = await trx_requests_db.get_requests(limit, page_index)
    return [DatabaseRecord(
        id=result._id,
        trx_address=result.trx_address,
        bandwidth=result.bandwidth,
        energy=result.energy,
        balance=result.balance
    ) for result in results]
