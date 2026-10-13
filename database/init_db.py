import json
from pathlib import Path
from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "poker_training_db"

def seed_database():
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
        client.admin.command('ping')
        print(" Conexión exitosa a MongoDB.")

        db = client[DB_NAME]
        base_dir = Path(__file__).parent / "seeds"

        ranges_file = base_dir / "preflop_ranges.json"
        if ranges_file.exists():
            with open(ranges_file, "r", encoding="utf-8") as f:
                ranges_data = json.load(f)
                db.preflop_ranges.delete_many({})
                db.preflop_ranges.insert_many(ranges_data)
                print(f" {len(ranges_data)} rangos guardados en la colección 'preflop_ranges'.")

        scenarios_file = base_dir / "training_scenarios.json"
        if scenarios_file.exists():
            with open(scenarios_file, "r", encoding="utf-8") as f:
                scenarios_data = json.load(f)
                db.training_scenarios.delete_many({})
                db.training_scenarios.insert_many(scenarios_data)
                print(f" {len(scenarios_data)} escenarios guardados en la colección 'training_scenarios'.")

        print(f"\n¡Base de datos '{DB_NAME}' inicializada correctamente!")

    except Exception as e:
        print(f"\n Error al conectar con MongoDB: {e}")
        print("Asegúrate de que el servicio de MongoDB esté iniciado en tu equipo.")

if __name__ == "__main__":
    seed_database()