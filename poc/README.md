# Benchmark y Prueba de Concepto (PoC)

## Objetivo de la Prueba
Evaluar la convergencia de la equidad estimada y el margen de error absoluto con la referencia del calculo exacto de la equidad con *Flopzilla* para analizar el tiempo de ejecución en función del número de iteraciones y definir un punto óptimo entre tiempo de ejecución y precisión de la estimación.

## Escenario de Prueba

Para las mediciones se utilizó el siguiente escenario:
* **Mano de Hero:** $A\spadesuit Q\spadesuit$
* **Board (Flop):** $K\heartsuit 3\spadesuit 6\spadesuit$
* **Rango del Villano:** Rango teórico de apertura desde UTG nit de microlimites(*OR UTG*)
* **Referencia de Equidad Exacta (Flopzilla):** `62.428%`

Los datos fueron añadidos directamente dado que es un escenario de prueba y no se requiere la ejecución de un gestor de rangos o recibir un board y mano de hero.

Se utilizó un rango de iteraciones que va desde 100 hasta 50000 para evaluar la convergencia de la equidad estimada y el margen de error absoluto.

## Resultados Obtenidos

| Iteraciones (N) | Equity Promedio (%) | Error Absoluto (%) | Tiempo Promedio (s) | Uso / Observación |
| --- | --- | --- | --- | --- |
| 100 | 60,10% | 3,28% | 0,007 | Inestable (Alta varianza) |
| 500 | 63,74% | 2,68% | 0,042 | Inestable |
| 1000 | 63,50% | 1,42% | 0,065 | Estimación inicial |
| 2500 | 62,46% | 0,96% | 0,189 | Estimación rápida |
| 5000 | 62,63% | 0,72% | 0,352 | Rápido con buen margen |
| 10000 | 62,73% | 0,37% | 0,666 | Punto Óptimo/preciso |
| 20000 | 62,54% | 0,28% | 1,872 | Alta precisión |
| 50000 | 62,48% | 0,19% | 3,384 | Convergencia casi exacta |

Con estos datos se concluye que la prueba de concepto valida que el algoritmo Monte Carlo implementado alcanza un punto de equilibrio entre precisión y tiempo de ejecución en N=10,000 iteraciones. A este nivel de muestreo, el sistema ofrece un tiempo de respuesta de <0.7 segundos con un margen de error inferior al 0.4%. Aumentar el muestreo a 50,000 iteraciones reduce el error levemente a ≈0.19%, pero quintuplica el tiempo de respuesta (∼3.38" s" ), por lo que 10,000 iteraciones se establece como la configuración por defecto para garantizar fluidez en tiempo real.


## Instrucciones para Ejecutar el Benchmark

### 1. Requisitos previos
Tener Python 3.13+ instalado.

### 2. Crear y activar un entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate   # En Windows
```
Instalar dependencias
```bash
pip install -r requirements_poc.txt
```
### 4. Ejecutar el script de prueba
```bash 
python benchmark_montecarlo.py
```