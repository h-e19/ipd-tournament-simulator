def strategy0(discount, payoff_matrices):
    """
    Strategy for Game Mode 0: Blind Iterative (No Memory, No Discount)

    Args:
        discount (float): Discount factor (not used in this mode).
        payoff_matrices (list of list of list of float]): Two 2x2 payoff matrices:
            payoff_matrices[0][a][b] is this player's payoff.
            payoff_matrices[1][a][b] is the opponent's payoff.

    Returns:
        int: 0 = cooperate, 1 = defect.
    """
    return 0 or 1


def strategy1(history, myhistory, discount, payoff_matrices):
    """
    Strategy for Game Mode1: Iterated with Memory (Remembers Opponent's Last Move, No Discount)

    Args:
        history (list[int] | None): Opponent's previous moves.
        myhistory (list[int] | None): Own previous moves.
        discount (float): Discount factor (not used in this mode).
        payoff_matrices (list of list of list of float]): Two 2x2 payoff matrices.

    Returns:
        int: 0 = cooperate, 1 = defect.
    """
    last = history[-1] if history else None
    return 0 or 1


def strategy2(discount, payoff_matrices):
    """
    Strategy for Game Mode2: Discounted Blind Iterative (No Memory, Geometric Discounting)

    Args:
        discount (float): Discount factor applied to future payoffs.
        payoff_matrices (list of list of list of float]): Two 2x2 payoff matrices.

    Returns:
        int: 0 = cooperate, 1 = defect.
    """
    return 0 or 1


def strategy3(history, myhistory, discount, payoff_matrices):
    """
    Strategy for Game Mode 3: Discounted Iterated with Memory (Remembers Opponent's Last Move + Discounting)

    Args:
        history (list[int] | None): Opponent's previous moves.
        myhistory (list[int] | None): Own previous moves.
        discount (float): Discount factor applied to future payoffs.
        payoff_matrices (list of list of list of float]): Two 2x2 payoff matrices.

    Returns:
        int: 0 = cooperate, 1 = defect.
    """
    last = history[-1] if history else None
    return 0 or 1


def strategy4(discount, payoff_matrices):
    """
    Strategy for Game Mode 4: Stochastic Blind Game (Probabilistic Continuation, No Memory)

    Args:
        discount (float): Probability to continue to the next round.
        payoff_matrices (list of list of list of float]): Two 2x2 payoff matrices.

    Returns:
        int: 0 = cooperate, 1 = defect.
    """
    
    return 0 or 1


def strategy5(history, myhistory, discount, payoff_matrices):
    """
    Strategy for Game Mode 5: Memory Stochastic Game (Remembers Opponent's Last Move + Probabilistic Continuation)

    Args:
        history (list[int] | None): Opponent's previous moves.
        myhistory (list[int] | None): Own previous moves.
        discount (float): Probability to continue to the next round.
        payoff_matrices (list of list of list of float]): Two 2x2 payoff matrices.

    Returns:
        int: 0 = cooperate, 1 = defect.
    """
    last = history[-1] if history else None
    return 0 or 1


