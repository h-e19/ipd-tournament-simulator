def strategy0(payoff_matrices, discount):
    """
    Strategy for Game Mode 0: Blind Iterative (No Memory, No Discount)

    Args:
        payoff_matrices (list of list of list): Two 2x2 payoff matrices:
            - payoff_matrices[0][move1][move2] is this player's payoff.
            - payoff_matrices[1][move1][move2] is the opponent's payoff.
        discount (float): Discount factor (not used in this mode, passed for consistency).

    Returns:
        int: 0 for cooperate, 1 for defect.
    """
    return 0 or 1


def strategy1(payoff_matrices, prev_move, discount):
    """
    Strategy for Game Mode 1: Iterated with Memory (Remembers Opponent's Last Move, No Discount)

    Args:
        payoff_matrices (list of list of list): Two 2x2 payoff matrices:
            - payoff_matrices[0][move1][move2] is this player's payoff.
            - payoff_matrices[1][move1][move2] is the opponent's payoff.
        prev_move (int or None): Opponent's previous action (0 = cooperate, 1 = defect),
            or None if it's the first round.
        discount (float): Discount factor (not used in this mode, passed for consistency).

    Returns:
        int: 0 for cooperate, 1 for defect.
    """
    return 0 or 1


def strategy2(payoff_matrices, discount):
    """
    Strategy for Game Mode 2: Discounted Blind Iterative (No Memory, Geometric Discounting)

    Args:
        payoff_matrices (list of list of list): Two 2x2 payoff matrices:
            - payoff_matrices[0][move1][move2] is this player's payoff.
            - payoff_matrices[1][move1][move2] is the opponent's payoff.
        discount (float): Discount factor applied to future rewards.

    Returns:
        int: 0 for cooperate, 1 for defect.
    """
    return 0 or 1


def strategy3(payoff_matrices, prev_move, discount):
    """
    Strategy for Game Mode 3: Discounted Iterated with Memory (Memory + Discounting)

    Args:
        payoff_matrices (list of list of list): Two 2x2 payoff matrices:
            - payoff_matrices[0][move1][move2] is this player's payoff.
            - payoff_matrices[1][move1][move2] is the opponent's payoff.
        prev_move (int or None): Opponent's previous action (0 = cooperate, 1 = defect),
            or None if it's the first round.
        discount (float): Discount factor applied to future rewards.

    Returns:
        int: 0 for cooperate, 1 for defect.
    """
    return 0 or 1


def strategy4(payoff_matrices, discount):
    """
    Strategy for Game Mode 4: Stochastic Blind Game (Probabilistic Continuation, No Memory)

    Args:
        payoff_matrices (list of list of list): Two 2x2 payoff matrices:
            - payoff_matrices[0][move1][move2] is this player's payoff.
            - payoff_matrices[1][move1][move2] is the opponent's payoff.
        discount (float): Probability of continuation to the next round.

    Returns:
        int: 0 for cooperate, 1 for defect.
    """
    return 0 or 1


def strategy5(payoff_matrices, prev_move, discount):
    """
    Strategy for Game Mode 5: Memory Stochastic Game (Memory + Probabilistic Continuation)

    Args:
        payoff_matrices (list of list of list): Two 2x2 payoff matrices:
            - payoff_matrices[0][move1][move2] is this player's payoff.
            - payoff_matrices[1][move1][move2] is the opponent's payoff.
        prev_move (int or None): Opponent's previous action (0 = cooperate, 1 = defect),
            or None if it's the first round.
        discount (float): Probability of continuation to the next round.

    Returns:
        int: 0 for cooperate, 1 for defect.
    """
    return 0 or 1


# --- Generic Template ---

def strategy(payoff_matrices, *args):
    """
    Generic Strategy Template

    A flexible strategy function that accepts the payoff matrices and optional
    mode-specific arguments like `prev_move` or `discount`, but ignores them.

    Args:
        payoff_matrices (list of list of list): Two 2x2 payoff matrices:
            - payoff_matrices[0][move1][move2] is this player's payoff.
            - payoff_matrices[1][move1][move2] is the opponent's payoff.
        *args: Optional additional arguments for compatibility with any game mode.

    Returns:
        int: 0 for cooperate, 1 for defect.
    """
    return 0 or 1
