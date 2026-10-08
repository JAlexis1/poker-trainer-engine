import random
import time
from treys import Deck, Evaluator, Card

def evaluate_hand(hero_hand, villain_hand, board, evaluator):
    hero_score = evaluator.evaluate(board, hero_hand)
    villain_score = evaluator.evaluate(board, villain_hand)

    if hero_score < villain_score:
        return "hero"
    elif villain_score < hero_score:
        return "villain"
    else:
        return "tie"

def get_villain_hand(villain_range):
    villain_hand = random.choice(villain_range)
    return villain_hand


def run_monte_carlo(simulations, left_cards, board, hero_hand, villain_range, evaluator):
    hero_wins, villain_wins, ties = 0, 0, 0
    
    start_time = time.perf_counter()

    for _ in range(simulations):
        villain_hand = get_villain_hand(villain_range)
        
        v_set = set(villain_hand)
        current_deck = [c for c in left_cards if c not in v_set]

        turn_river = random.sample(current_deck, 2)
        board_full = board + turn_river

        result = evaluate_hand(hero_hand, villain_hand, board_full, evaluator)

        if result == "hero":
            hero_wins += 1
        elif result == "villain":
            villain_wins += 1
        else:
            ties += 1

    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    equity = (hero_wins + (ties / 2)) / simulations
    
    return equity, elapsed_time

if __name__ == "__main__":

    evaluator = Evaluator()
    deck = Deck()

    board = [Card.new("Kh"), Card.new("3s"), Card.new("6s")]
    hero_hand = [Card.new("As"), Card.new("Qs")]

    known_cards = set(board + hero_hand)
    left_cards = [c for c in deck.cards if c not in known_cards]
    REAL_EQUITY = 0.62428
    n_iterations = [100, 500, 1000, 2500, 5000, 10000, 20000, 50000]

    villain_range = [
        # --- PAIRS (42 combos) ---
        # AA (3 combos)
        [Card.new("Ac"), Card.new("Ad")], [Card.new("Ac"), Card.new("Ah")], [Card.new("Ad"), Card.new("Ah")],
        # KK (3 combos)
        [Card.new("Kc"), Card.new("Kd")], [Card.new("Kc"), Card.new("Ks")], [Card.new("Kd"), Card.new("Ks")],
        # QQ (3 combos)
        [Card.new("Qc"), Card.new("Qd")], [Card.new("Qc"), Card.new("Qh")], [Card.new("Qd"), Card.new("Qh")],
        # JJ (6 combos)
        [Card.new("Jc"), Card.new("Jd")], [Card.new("Jc"), Card.new("Jh")], [Card.new("Jc"), Card.new("Js")], [Card.new("Jd"), Card.new("Jh")], [Card.new("Jd"), Card.new("Js")], [Card.new("Jh"), Card.new("Js")],
        # TT (6 combos)
        [Card.new("Tc"), Card.new("Td")], [Card.new("Tc"), Card.new("Th")], [Card.new("Tc"), Card.new("Ts")], [Card.new("Td"), Card.new("Th")], [Card.new("Td"), Card.new("Ts")], [Card.new("Th"), Card.new("Ts")],
        # 99 (6 combos)
        [Card.new("9c"), Card.new("9d")], [Card.new("9c"), Card.new("9h")], [Card.new("9c"), Card.new("9s")], [Card.new("9d"), Card.new("9h")], [Card.new("9d"), Card.new("9s")], [Card.new("9h"), Card.new("9s")],
        # 88 (6 combos)
        [Card.new("8c"), Card.new("8d")], [Card.new("8c"), Card.new("8h")], [Card.new("8c"), Card.new("8s")], [Card.new("8d"), Card.new("8h")], [Card.new("8d"), Card.new("8s")], [Card.new("8h"), Card.new("8s")],
        # 77 (6 combos)
        [Card.new("7c"), Card.new("7d")], [Card.new("7c"), Card.new("7h")], [Card.new("7c"), Card.new("7s")], [Card.new("7d"), Card.new("7h")], [Card.new("7d"), Card.new("7s")], [Card.new("7h"), Card.new("7s")],
        # 66 (3 combos)
        [Card.new("6c"), Card.new("6d")], [Card.new("6c"), Card.new("6h")], [Card.new("6d"), Card.new("6h")],

        # --- SUITED HANDS (50 combos) ---
        # AKs (2 combos)
        [Card.new("Ac"), Card.new("Kc")], [Card.new("Ad"), Card.new("Kd")],
        # AQs (3 combos)
        [Card.new("Ac"), Card.new("Qc")], [Card.new("Ad"), Card.new("Qd")], [Card.new("Ah"), Card.new("Qh")],
        # AJs (3 combos)
        [Card.new("Ac"), Card.new("Jc")], [Card.new("Ad"), Card.new("Jd")], [Card.new("Ah"), Card.new("Jh")],
        # ATs (3 combos)
        [Card.new("Ac"), Card.new("Tc")], [Card.new("Ad"), Card.new("Td")], [Card.new("Ah"), Card.new("Th")],
        # A9s (3 combos)
        [Card.new("Ac"), Card.new("9c")], [Card.new("Ad"), Card.new("9d")], [Card.new("Ah"), Card.new("9h")],
        # A8s (3 combos)
        [Card.new("Ac"), Card.new("8c")], [Card.new("Ad"), Card.new("8d")], [Card.new("Ah"), Card.new("8h")],
        # A7s (3 combos)
        [Card.new("Ac"), Card.new("7c")], [Card.new("Ad"), Card.new("7d")], [Card.new("Ah"), Card.new("7h")],
        # A6s (3 combos)
        [Card.new("Ac"), Card.new("6c")], [Card.new("Ad"), Card.new("6d")], [Card.new("Ah"), Card.new("6h")],
        # A5s (3 combos)
        [Card.new("Ac"), Card.new("5c")], [Card.new("Ad"), Card.new("5d")], [Card.new("Ah"), Card.new("5h")],
        # A4s (3 combos)
        [Card.new("Ac"), Card.new("4c")], [Card.new("Ad"), Card.new("4d")], [Card.new("Ah"), Card.new("4h")],
        # A3s (3 combos)
        [Card.new("Ac"), Card.new("3c")], [Card.new("Ad"), Card.new("3d")], [Card.new("Ah"), Card.new("3h")],
        # A2s (3 combos)
        [Card.new("Ac"), Card.new("2c")], [Card.new("Ad"), Card.new("2d")], [Card.new("Ah"), Card.new("2h")],
        # KQs (2 combos)
        [Card.new("Kc"), Card.new("Qc")], [Card.new("Kd"), Card.new("Qd")],
        # KJs (3 combos)
        [Card.new("Kc"), Card.new("Jc")], [Card.new("Kd"), Card.new("Jd")], [Card.new("Ks"), Card.new("Js")],
        # KTs (3 combos)
        [Card.new("Kc"), Card.new("Tc")], [Card.new("Kd"), Card.new("Td")], [Card.new("Ks"), Card.new("Ts")],
        # QJs (3 combos)
        [Card.new("Qc"), Card.new("Jc")], [Card.new("Qd"), Card.new("Jd")], [Card.new("Qh"), Card.new("Jh")],
        # QTs (3 combos)
        [Card.new("Qc"), Card.new("Tc")], [Card.new("Qd"), Card.new("Td")], [Card.new("Qh"), Card.new("Th")],
        # JTs (4 combos)
        [Card.new("Jc"), Card.new("Tc")], [Card.new("Jd"), Card.new("Td")], [Card.new("Jh"), Card.new("Th")], [Card.new("Js"), Card.new("Ts")],

        # --- OFFSUIT HANDS (29 combos) ---
        # AKo (7 combos)
        [Card.new("Ac"), Card.new("Kd")], [Card.new("Ac"), Card.new("Ks")],
        [Card.new("Ad"), Card.new("Kc")], [Card.new("Ad"), Card.new("Ks")],
        [Card.new("Ah"), Card.new("Kc")], [Card.new("Ah"), Card.new("Kd")], [Card.new("Ah"), Card.new("Ks")],
        # AQo (6 combos)
        [Card.new("Ac"), Card.new("Qd")], [Card.new("Ac"), Card.new("Qh")],
        [Card.new("Ad"), Card.new("Qc")], [Card.new("Ad"), Card.new("Qh")],
        [Card.new("Ah"), Card.new("Qc")], [Card.new("Ah"), Card.new("Qd")],
        # AJo (9 combos)
        [Card.new("Ac"), Card.new("Jd")], [Card.new("Ac"), Card.new("Jh")], [Card.new("Ac"), Card.new("Js")],
        [Card.new("Ad"), Card.new("Jc")], [Card.new("Ad"), Card.new("Jh")], [Card.new("Ad"), Card.new("Js")],
        [Card.new("Ah"), Card.new("Jc")], [Card.new("Ah"), Card.new("Jd")], [Card.new("Ah"), Card.new("Js")],
        # KQo (7 combos)
        [Card.new("Kc"), Card.new("Qd")], [Card.new("Kc"), Card.new("Qh")],
        [Card.new("Kd"), Card.new("Qc")], [Card.new("Kd"), Card.new("Qh")],
        [Card.new("Ks"), Card.new("Qc")], [Card.new("Ks"), Card.new("Qd")], [Card.new("Ks"), Card.new("Qh")]
    ]

    print("\n" + "="*70)
    print("  BENCHMARK Y CONVERGENCIA MONTE CARLO - PRUEBA DE CONCEPTO")
    print("="*70)
    print(f"{'Iteraciones (N)':<18} | {'Equity Obtenido':<16} | {'Error Absoluto':<16} | {'Tiempo (s)':<10}")
    print("-" * 70)

    for n in n_iterations:
        equity, t_seconds = run_monte_carlo(
            n, 
            left_cards, 
            board, 
            hero_hand, 
            villain_range, 
            evaluator
        )
                
        error = abs(equity - REAL_EQUITY)
        
        print(f"{n:<18,}" f" | {equity:<16.2%}" f" | {error:<16.4%}" f" | {t_seconds:<10.4f}")

    print("="*70)