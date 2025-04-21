from os import environ

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from models import TrxAddressInfo, DatabaseRecord
from trx import TrxAddress

load_dotenv()

app = FastAPI()


class AddressInfoRequestData(BaseModel):
    address: str


@app.post("/address/info")
async def address_info(address_info_request: AddressInfoRequestData) -> TrxAddressInfo:
    trx_address = TrxAddress(address_info_request.address, environ.get("trongrid_api_key"))
    return TrxAddressInfo(
        bandwidth=await trx_address.get_bandwidth(),
        energy=await trx_address.get_energy(),
        balance=await trx_address.get_balance()
    )


@app.get("/records/recent")
async def records_recent(limit: int = 10, page_index: int = 0) -> DatabaseRecord:
    pass
