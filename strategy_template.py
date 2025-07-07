def strategy0(discount):
    """
    Strategy for Game Mode 0: Blind Iterative (No Memory, No Discount)

    Args:
        discount (float): Discount factor (not used in this mode, passed for consistency)

    Returns:
        int: 0 for cooperate, 1 for defect
    """
    return 0 or 1


def strategy1(prev_move, discount):
    """
    Strategy for Game Mode 1: Iterated with Memory (Remembers Opponent's Last Move, No Discount)

    Args:
        prev_move (int or None): Previous move of the opponent (0 or 1), or None on first round
        discount (float): Discount factor (not used in this mode, passed for consistency)

    Returns:
        int: 0 for cooperate, 1 for defect
    """
    return 0 or 1


def strategy2(discount):
    """
    Strategy for Game Mode 2: Discounted Blind Iterative (No Memory, Geometric Discounting)

    Args:
        discount (float): Discount factor applied to future rewards

    Returns:
        int: 0 for cooperate, 1 for defect
    """
    return 0 or 1


def strategy3(prev_move, discount):
    """
    Strategy for Game Mode 3: Discounted Iterated with Memory (Memory + Discounting)

    Args:
        prev_move (int or None): Previous move of the opponent (0 or 1), or None on first round
        discount (float): Discount factor applied to future rewards

    Returns:
        int: 0 for cooperate, 1 for defect
    """
    return 0 or 1


def strategy4(discount):
    """
    Strategy for Game Mode 4: Stochastic Blind Game (Probabilistic Continuation, No Memory)

    Args:
        discount (float): Probability of continuation to the next round

    Returns:
        int: 0 for cooperate, 1 for defect
    """
    return 0 or 1


def strategy5(prev_move, discount):
    """
    Strategy for Game Mode 5: Stochastic Game with Memory (Memory + Probabilistic Continuation)

    Args:
        prev_move (int or None): Previous move of the opponent (0 or 1), or None on first round
        discount (float): Probability of continuation to the next round

    Returns:
        int: 0 for cooperate, 1 for defect
    """
    return 0 or 1


# --- Generic Template ---

def strategy(*args):
    """
    Generic Strategy Template

    A flexible strategy function that accepts any number of arguments.
    Useful when your logic does not depend on the specific game mode arguments
    like `prev_move` or `discount`.

    Args:
        *args: Flexible arguments, ignored by the strategy.

    Returns:
        int: 0 for cooperate, 1 for defect
    """
    return 0 or 1
