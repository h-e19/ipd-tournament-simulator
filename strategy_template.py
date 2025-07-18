class PSTNode:
    def __init__(self, count = 0):
        self.children = {
            (0,0): None,
            (0,1): None,
            (1,0): None,
            (1,1): None,
        }
        self.count = count

class probabilistic_suffix_tree():
    def __init__(self, history, myhistory, depth=5 ):
        self.depth = depth
        self.root = PSTNode()
        self.passes = 0
        self.update(history, myhistory)

    def update(self, history, myhistory):
        for start in range(len(history) - self.depth - 1):
            node = self.root
            for index in range(self.depth):
                self.passes += 1
                if node.children[myhistory[start + index], history[start + index]] is None:
                    node.children[myhistory[start + index], history[start + index]] = PSTNode()
                node = node.children[myhistory[start + index], history[start + index]]
                node.count += 1

    def traverse(self, depth, context1, context2):
        node = self.root
        for d in range(depth, 1, -1):
            if node.children[context1[-d], context2[-d]] is None:
                return {
                    (0, 0): 0,
                    (0, 1): 0,
                    (1, 0): 0,
                    (1, 1): 0
                }
            node = node.children[context1[-d], context2[-d]]
        result = {}
        for key in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            child = node.children.get(key)
            result[key] = child.count if child is not None else 0
        return result

    def query(self, history, myhistory):
        self.update(history, myhistory)
        context1 = myhistory[-self.depth:]
        context2 = history[-self.depth:]
        children_counts = self.traverse(self.depth, context1, context2)

        total = sum(children_counts.values())
        if total == 0:
            return 0
        probabilities = {k: v / total for k, v in children_counts.items()}

        best = max(probabilities.items(), key=lambda x: x[1])[0]  # key is (x,y)
        if best in [(0, 0), (1, 0)]:
            return 0
        else:
            return 1


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
    return 1


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
    if len(history) < 20:
        return history[-1] if history else 1

    if not hasattr(strategy1, "pst"):
        strategy1.pst = probabilistic_suffix_tree(history, myhistory, depth=5)

    prediction = strategy1.pst.query(history, myhistory)
    return 0 if prediction == 0 else 1

def strategy2(discount, payoff_matrices):
    """
    Strategy for Game Mode2: Discounted Blind Iterative (No Memory, Geometric Discounting)

    Args:
        discount (float): Discount factor applied to future payoffs.
        payoff_matrices (list of list of list of float]): Two 2x2 payoff matrices.

    Returns:
        int: 0 = cooperate, 1 = defect.
    """
    return 1


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
    if len(history) < 20:
        return history[-1] if history else 1

    if not hasattr(strategy3, "pst"):
        strategy3.pst = probabilistic_suffix_tree(history, myhistory, depth=5)

    prediction = strategy3.pst.query(history, myhistory)
    return 0 if prediction == 0 else 1


def strategy4(discount, payoff_matrices):
    """
    Strategy for Game Mode 4: Stochastic Blind Game (Probabilistic Continuation, No Memory)

    Args:
        discount (float): Probability to continue to the next round.
        payoff_matrices (list of list of list of float]): Two 2x2 payoff matrices.

    Returns:
        int: 0 = cooperate, 1 = defect.
    """
    return 1


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
    if len(history) < 20:
        return history[-1] if history else 1

    if not hasattr(strategy5, "pst"):
        strategy5.pst = probabilistic_suffix_tree(history, myhistory, depth=5)

    prediction = strategy5.pst.query(history, myhistory)
    return 0 if prediction == 0 else 1


