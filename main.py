
from tournament import Player,Tournament,Helper 
from strategy_template import strategy0,strategy1,strategy2,strategy3,strategy4,strategy5
import random

# --- Strategy Functions ---
def always_cooperate(*args):
    """Always cooperate (0)."""
    return 0

def always_defect(*args):
    """Always defect (1)."""
    return 1

def tit_for_tat(history, myhistory, discount, payoff_matrices):
    """
    Cooperate on the first move; thereafter copy opponent's last move.

    Args:
        history (list[int]): Opponent's previous moves.
        myhistory (list[int]): Player's previous moves.
        discount (float): Discount factor (unused here).
        payoff_matrices (list): Payoff matrices (unused here).

    Returns:
        int: 0 for cooperate, 1 for defect.
    """
    last = history[-1] if history else None
    return last if last is not None else 0

def random_strategy(*args):
    """Randomly choose cooperate (0) or defect (1)."""
    return random.choice([0, 1])

# --- Main ---
def main():
    payoff_p1 = [[3, 0], [5, 1]]
    payoff_p2 = [[3, 5], [0, 1]]
    discount_factor = 0.95
    players = [
        Player("CooperateBot", [always_cooperate]*6),
        Player("DefectBot", [always_defect]*6),
        Player("TFT", [always_cooperate, tit_for_tat, always_cooperate, tit_for_tat, always_cooperate, tit_for_tat]),
        Player("RandomBot", [random_strategy]*6),
        Player("My_Player",[strategy0,strategy1,strategy2,strategy3,strategy4,strategy5])
    ]
    tour = Tournament(players, [payoff_p1, payoff_p2], discount_factor)
    board = tour.tournament(rounds=5)
    Helper.print_tournament_scores(players, board)
    Helper.save_tournament_to_json(players, board, discount_factor, payoff_p1, payoff_p2)

if __name__ == "__main__":
    main()
