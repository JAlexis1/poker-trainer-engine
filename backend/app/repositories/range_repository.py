from typing import Optional, Dict, Any
from app.repositories.base_repository import BaseRepository

class RangeRepository(BaseRepository):
    def __init__(self, client=None):
        super().__init__(client)
        self.collection = self.db["preflop_ranges"]

    def get_by_id(self, range_id: str) -> Optional[Dict[str, Any]]:
        return self.collection.find_one({"_id": range_id})

    def get_notation(self, range_id: str) -> Optional[str]:
        document = self.get_by_id(range_id)
        if document:
            return document.get("notation")
        return None