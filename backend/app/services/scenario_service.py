class ScenarioService:
    def __init__(
        self, 
        scenario_repo,     # Inyección del repositorio de escenarios
        range_repo,        # Inyección del repositorio de rangos
        evaluator_engine   # Inyección del motor probabilístico/evaluador
    ):
        self.scenario_repo = scenario_repo
        self.range_repo = range_repo
        self.evaluator_engine = evaluator_engine