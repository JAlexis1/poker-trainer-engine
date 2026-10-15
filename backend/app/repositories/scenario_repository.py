from typing import Optional, Dict, Any, List
from app.repositories.base_repository import BaseRepository

class ScenarioRepository(BaseRepository):
    def __init__(self, client=None):
        super().__init__(client)
        self.collection = self.db["training_scenarios"]

    def get_by_id(self, scenario_id: str) -> Optional[Dict[str, Any]]:
        return self.collection.find_one({"_id": scenario_id})

    def get_all(self) -> List[Dict[str, Any]]:
        return list(self.collection.find({}, {"_id": 1, "title": 1, "board.street": 1}))