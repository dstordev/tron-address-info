from pydantic import BaseModel


class TrxAddressInfo(BaseModel):
    bandwidth: int
    energy: int
    balance: float

class Error(BaseModel):
    error: str

class DatabaseRecord(BaseModel):
    id: int
    trx_address: str
    bandwidth: int
    energy: int
    balance: float
