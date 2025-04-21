from typing import Any

from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider


class TrxAddress:
    def __init__(self, address: str, api_key: str):
        self._address = address
        self._tron = AsyncTron(provider=AsyncHTTPProvider(api_key=api_key))

    async def get_energy(self) -> int:
        account_resource_response = await self._tron.get_account_resource(self._address)
        energy_limit = account_resource_response.get("EnergyLimit", 0)
        energy_used = account_resource_response.get("EnergyUsed", 0)
        return energy_limit - energy_used

    async def get_bandwidth(self) -> int:
        bandwidth: int | Any = await self._tron.get_bandwidth(self._address)
        if bandwidth.__class__ is not int:
            raise TypeError(f"bandwith is not int: {bandwidth.__class__}")
        return bandwidth

    async def get_balance(self) -> float:
        return float(await self._tron.get_account_balance(self._address))
