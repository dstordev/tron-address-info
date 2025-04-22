from sqlalchemy.dialects.postgresql import BIGINT, TEXT, DOUBLE_PRECISION
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class TrxRequestsTable(Base):
    __tablename__ = "trx_requests"

    _id: Mapped[int] = mapped_column("id", BIGINT, primary_key=True)
    trx_address: Mapped[str] = mapped_column("trx_address", TEXT)
    bandwidth: Mapped[int] = mapped_column("bandwidth", BIGINT)
    energy: Mapped[int] = mapped_column("energy", BIGINT)
    balance: Mapped[float] = mapped_column("balance", DOUBLE_PRECISION)
