from pydantic import BaseModel


class TrxAddressInfo(BaseModel):
    bandwidth: int
    energy: int
    balance: float


class DatabaseRecord(BaseModel):
    id: int
    trx_address: str
    bandwidth: str
    energy: str
    balance: int
