import random

class Player:
    """
    Represents a player in the game with a team name and strategy functions for each game mode.
    
    Attributes:
        teamname (str): Name of the player's team.
        strategies (list): A list of 6 strategy functions corresponding to each game mode.
    """

    def __init__(self, teamname, strategies):
        self.teamname = teamname
        self.strategies = strategies

    def play(self, prev_move=None, game_mode=0, discount=1.0):
        """
        Selects an action based on the assigned strategy for the game mode.

        Args:
            prev_move (int or None): The previous move of the opponent (0 or 1), or None.
            game_mode (int): Game mode index (0 to 3).
            discount (float): Discount factor for future rounds (only used in discounted modes).

        Returns:
            int: The selected move (0 = cooperate, 1 = defect).
        """
        strategy_fn = self.strategies[game_mode]
        if game_mode in [1, 3,5]:  # Memory-based
            return strategy_fn(prev_move, discount)
        else:  # Blind
            return strategy_fn(discount)


class Tournament:
    """
    Manages a round-robin tournament of players across multiple game modes.

    Attributes:
        players (list): List of Player objects.
        payoff_matrices (list): [Player1 matrix, Player2 matrix], each a 2x2 payoff matrix.
        discount_factor (float): Discount factor used in game modes 2 and 3 , 4 ,5`~.
    """

    def __init__(self, players, payoff_matrices, discount_factor):
        """
        Initialize the tournament.

        Args:
            players (list): List of Player objects.
            payoff_matrices (list): [Player1 matrix, Player2 matrix].
            discount_factor (float): Discount factor for discounted games.
        """
        self.players = players
        self.payoff_matrices = payoff_matrices
        self.discount_factor = discount_factor

    def play(self, player1, player2, game_mode, prev1, prev2, discount=1.0):
        """
        Play a round with memory of previous moves.

        Args:
            player1, player2 (Player): The two players.
            game_mode (int): Mode index.
            prev1, prev2 (int): Previous moves of players.
            discount (float): Discount factor.

        Returns:
            tuple: move1, move2, payoff1, payoff2
        """
        move1 = player1.play(prev_move=prev2, game_mode=game_mode, discount=discount)
        move2 = player2.play(prev_move=prev1, game_mode=game_mode, discount=discount)
        payoff1 = self.payoff_matrices[0][move1][move2]
        payoff2 = self.payoff_matrices[1][move2][move1]
        return move1, move2, payoff1, payoff2

    def blindplay(self, player1, player2, game_mode, discount=1.0):
        """
        Play a round without memory.

        Args:
            player1, player2 (Player): The two players.
            game_mode (int): Mode index.
            discount (float): Discount factor.

        Returns:
            tuple: move1, move2, payoff1, payoff2
        """
        move1 = player1.play(game_mode=game_mode, discount=discount)
        move2 = player2.play(game_mode=game_mode, discount=discount)
        payoff1 = self.payoff_matrices[0][move1][move2]
        payoff2 = self.payoff_matrices[1][move2][move1]
        return move1, move2, payoff1, payoff2

    def evaluate(self, player1, player2, rounds=10):
        """
        Evaluate two players across 6 game modes of the Iterated Prisoner's Dilemma.

        Game Modes:
        - Mode 0: Blind Iterative (no memory, no discount)
        - Mode 1: Iterated with Memory (remembers opponent's previous move, no discounting)
        - Mode 2: Discounted Blind Iterated (no memory, geometric discounting over time)
        - Mode 3: Discounted Iterated with Memory (remembers opponent's previous move, with discounting)
        - Mode 4: Blind Stochastic Game (no memory, probabilistic continuation)
        - Mode 5: Memory Stochastic Game (remembers opponent's previous move, probabilistic continuation)

        Returns:
            tuple: score1, score2 — 2D lists of scores per mode and round.
        """
        score1 = [[] for _ in range(6)]
        score2 = [[] for _ in range(6)]

        for mode in range(6):
            discount = 1.0 if mode in [0, 1] else self.discount_factor
            prev1 = None
            prev2 = None
            r = 0

            while True:
                if mode in [4, 5] and r > 0 and random.random() > discount:
                    break  # Stop stochastic game with probability (1 - discount)
                if mode in [0, 2, 4]:  # Blind modes
                    move1, move2, p1, p2 = self.blindplay(player1, player2, mode, discount)
                else:  # Memory-based modes
                    move1, move2, p1, p2 = self.play(player1, player2, mode, prev1, prev2, discount)
                    prev1, prev2 = move1, move2

                power = 1.0 if mode in [0, 1, 4, 5] else discount ** r
                score1[mode].append(p1 * power)
                score2[mode].append(p2 * power)

                r += 1
                if mode in [0, 1, 2, 3] and r >= rounds:
                    break

        return score1, score2


    def tournament(self, rounds=10):
        """
        Run a full round-robin tournament between all players.

        Each player pair is evaluated across all 4 game modes.

        Args:
            rounds (int): Number of rounds per game mode.

        Returns:
            3D list: scoreboard[i][j][mode] is the score list of player i vs j in mode.
        """
        n = len(self.players)
        scoreboard = [[[[] for _ in range(6)] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                s1, s2 = self.evaluate(self.players[i], self.players[j], rounds)
                scoreboard[i][j] = s1
                scoreboard[j][i] = s2

        return scoreboard


# --- Strategy Functions ---
def always_cooperate(*args):
    """Always plays cooperate (0)."""
    return 0

def always_defect(*args):
    """Always plays defect (1)."""
    return 1

def tit_for_tat(prev, discount):
    """Plays opponent's previous move; cooperates on first move."""
    return prev if prev is not None else 0

def random_strategy(*args):
    """Randomly chooses between cooperate (0) and defect (1)."""
    return random.choice([0, 1])


# --- Main Function ---
def main():
    """
    Sets up a sample tournament between predefined bots with different strategies
    and prints results across all game modes.
    """
    # Payoff matrices
    payoff_p1 = [[3, 0], [5, 1]] #player 1 perspective
    payoff_p2 = [[3, 0], [5, 1]] #player 2 perspective

    players = [
        Player("CooperateBot", [always_cooperate] * 6),
        Player("DefectBot", [always_defect] * 6),
        Player("TFT", [always_cooperate, tit_for_tat, always_cooperate, tit_for_tat,always_cooperate,tit_for_tat]),
        Player("RandomBot", [random_strategy] * 6)
    ]

    t = Tournament(players, [payoff_p1, payoff_p2], discount_factor=0.95)
    results = t.tournament(rounds=5)
    print_tournament_scores(players, results)


# --- Helper Function ---
def print_tournament_scores(players, scoreboard):
    """
    Prints human-readable tournament results.

    Args:
        players (list): Player objects.
        scoreboard (list): 3D scores from tournament.
    """
    mode_names = [
        "Blind Iterative (No Memory, No Discount)",
        "Memory Iterative (No Discount)",
        "Discounted Blind Iterative",
        "Discounted Memory Iterative",
        "Stochastic Blind (Probabilistic Rounds, No Memory)",
        "Stochastic Memory (Probabilistic Rounds with Memory)"
    ]
    n = len(players)
    for i in range(n):
        for j in range(n):
            if i != j:
                print(f"\nMatch: {players[i].teamname} vs {players[j].teamname}")
                for mode in range(6):
                    p1_total = sum(scoreboard[i][j][mode])
                    p2_total = sum(scoreboard[j][i][mode])
                    print(f"  Game Mode {mode} - {mode_names[mode]}: {p1_total:.2f} - {p2_total:.2f}")


# --- Entry Point ---
if __name__ == "__main__":
    main()
