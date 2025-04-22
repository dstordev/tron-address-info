from os import environ
from typing import List, Union

from dotenv import load_dotenv
from fastapi import FastAPI, Response
from pydantic import BaseModel
from tronpy.exceptions import BadAddress

from database import TrxRequestsDB
from models import TrxAddressInfo, DatabaseRecord, Error
from trx import TrxAddress

load_dotenv()

trx_requests_db = TrxRequestsDB()

app = FastAPI()


class AddressInfoRequestData(BaseModel):
    address: str


@app.post("/address/info")
async def address_info(address_info_request: AddressInfoRequestData, response: Response) -> Union[
    TrxAddressInfo | Error]:
    trx_address = TrxAddress(address_info_request.address, environ.get("trongrid_api_key"))
    try:
        trx_address_info = TrxAddressInfo(
            bandwidth=await trx_address.get_bandwidth(),
            energy=await trx_address.get_energy(),
            balance=await trx_address.get_balance()
        )
    except BadAddress:
        response.status_code = 400
        return Error(
            error="BadAddress TRX"
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
