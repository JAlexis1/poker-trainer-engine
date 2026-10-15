import sys
import os

directorio_actual = os.path.dirname(__file__)
ruta_backend = os.path.abspath(os.path.join(directorio_actual, '..', 'backend'))
sys.path.append(ruta_backend)

from app.repositories.range_repository import RangeRepository
from app.repositories.scenario_repository import ScenarioRepository


def test_repos():
    range_repo = RangeRepository()
    scenario_repo = ScenarioRepository()

    print("Probando RangeRepository...")
    notation = range_repo.get_notation("OR_UTG")
    expected_notation = "AA-66,AKs-A2s,KQs-KTs,QJs-QTs,JTs,AKo-AJo,KQo"   
    assert notation == expected_notation, f"Error en rango. Se obtuvo: {notation}"
    print("✓ RangeRepository funciona correctamente.\n")

    print("Probando ScenarioRepository...")
    scenario = scenario_repo.get_by_id("scenario_001")
    assert scenario is not None, "Error: No se encontró el escenario_001 en MongoDB."  
    expected_title = "Proyecto de Color a las nuts contra UTG"
    
    assert scenario["title"] == expected_title, f"Error en título. Se obtuvo: {scenario.get('title')}"
    assert scenario["board"]["street"] == "flop", "Error: La calle no es 'flop'"
    
    print("✓ ScenarioRepository funciona correctamente.")

if __name__ == "__main__":
    test_repos()
    print("\n¡Todas las pruebas pasaron exitosamente!")