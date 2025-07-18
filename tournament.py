import random
import json

class Player:
    """
    Represents a player in the Iterated Prisoner's Dilemma tournament.

    Attributes:
        teamname (str): The player's team name.
        strategies (list[callable]): List of 6 strategy functions, one per game mode.
    """

    def __init__(self, teamname, strategies):
        self.teamname = teamname
        self.strategies = strategies

    def play(self, payoff_matrices, history=None, myhistory=None, game_mode=0, discount=1.0):
        """
        Choose an action based on the assigned strategy for the specified game mode.

        Args:
            payoff_matrices (list[list[list[float]]]): Two 2x2 payoff matrices for player1 and player2,
                structured as [matrix_p1, matrix_p2].
            history (list[int] | None): Opponent's past moves (0=cooperate, 1=defect).
            myhistory (list[int] | None): Player's own past moves.
            game_mode (int): Index of game mode (0–5):
                0: Blind Iterative (no memory, no discount)
                1: Iterated with Memory (remembers last move, no discount)
                2: Discounted Blind (no memory, geometric discount)
                3: Discounted Memory (last move, geometric discount)
                4: Stochastic Blind (probabilistic continuation, no memory)
                5: Stochastic Memory (probabilistic continuation, memory)
            discount (float): Discount factor for future payoffs or continuation probability.

        Returns:
            int: Chosen action (0 = cooperate, 1 = defect).
        """
        strategy_fn = self.strategies[game_mode]
        # Memory-based modes expect (history, myhistory, discount, payoff_matrices)
        if game_mode in [1, 3, 5]:
            return strategy_fn(history, myhistory, discount, payoff_matrices)
        # Blind modes expect (discount, payoff_matrices)
        return strategy_fn(discount, payoff_matrices)

class Tournament:
    """
    Conducts a round-robin tournament between players over six IPD game modes.

    Attributes:
        players (list[Player]): List of participants.
        payoff_matrices (list[list[list[float]]]): Payoff matrices for all matches.
        discount_factor (float): Discount factor for discounted and stochastic modes.
    """

    def __init__(self, players, payoff_matrices, discount_factor=1.0):
        self.players = players
        self.payoff_matrices = payoff_matrices
        self.discount_factor = discount_factor

    def play_round(self, player1, player2, game_mode, history1, history2, discount):
        """
        Play one iterated round where strategies can use memory.

        Args:
            player1, player2 (Player): Competitors.
            game_mode (int): Mode index (0–5).
            history1, history2 (list[int]): Past moves of each player.
            discount (float): Discount factor or continuation probability.

        Returns:
            tuple[int, int, float, float]: (move1, move2, payoff1, payoff2).
        """
        move1 = player1.play(self.payoff_matrices, history2, history1, game_mode, discount)
        move2 = player2.play(self.payoff_matrices, history1, history2, game_mode, discount)
        p1 = self.payoff_matrices[0][move1][move2]
        p2 = self.payoff_matrices[1][move1][move2]
        return move1, move2, p1, p2

    def blind_round(self, player1, player2, game_mode, discount):
        """
        Play one iterated round without memory dependence.

        Args:
            player1, player2 (Player): Competitors.
            game_mode (int): Mode index (0–5).
            discount (float): Discount factor (unused in payoff but for consistency).

        Returns:
            tuple[int, int, float, float]: (move1, move2, payoff1, payoff2).
        """
        move1 = player1.play(self.payoff_matrices, game_mode=game_mode, discount=discount)
        move2 = player2.play(self.payoff_matrices, game_mode=game_mode, discount=discount)
        p1 = self.payoff_matrices[0][move1][move2]
        p2 = self.payoff_matrices[1][move1][move2]
        return move1, move2, p1, p2

    def evaluate(self, player1, player2, rounds=10):
        """
        Run an iterated match between two players across all six modes.

        Args:
            player1, player2 (Player): Competitors.
            rounds (int): Fixed rounds for non-stochastic modes.

        Returns:
            tuple[list[list[float]], list[list[float]]]: Scores per mode per round for each player.
        """
        scores1 = [[] for _ in range(6)]
        scores2 = [[] for _ in range(6)]
        for mode in range(6):
            disc = self.discount_factor if mode not in [0, 1] else 1.0
            h1, h2 = [], []
            r = 0
            while True:
                # Break for stochastic modes with probability (1 - disc) after first round
                if mode in [4, 5] and r > 0 and random.random() > disc:
                    break
                if mode in [0, 2, 4]:
                    m1, m2, p1, p2 = self.blind_round(player1, player2, mode, disc)
                else:
                    m1, m2, p1, p2 = self.play_round(player1, player2, mode, h1, h2, disc)
                    h1.append(m1)
                    h2.append(m2)
                weight = 1.0 if mode in [0, 1, 4, 5] else (disc ** r)
                scores1[mode].append(p1 * weight)
                scores2[mode].append(p2 * weight)
                r += 1
                if mode in [0, 1, 2, 3] and r >= rounds:
                    break
        return scores1, scores2

    def tournament(self, rounds=10):
        """
        Conduct a full round-robin tournament over all player pairs.

        Args:
            rounds (int): Number of rounds for fixed-length modes.

        Returns:
            list[list[list[list[float]]]]: 4D list where [i][j][mode] is score list of player i vs j.
        """
        n = len(self.players)
        board = [[[[] for _ in range(6)] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                s1, s2 = self.evaluate(self.players[i], self.players[j], rounds)
                board[i][j] = s1
                board[j][i] = s2
        return board



class Helper:
    @staticmethod
    def print_tournament_scores(players, board):
        """
        Print match summaries for each player pair across all modes.

        Args:
            players (list[Player]): Competitors.
            board (4D list): Tournament scores from Tournament.tournament().
        """
        mode_names = [
            "Blind Iterative",
            "Memory Iterative",
            "Discounted Blind",
            "Discounted Memory",
            "Stochastic Blind",
            "Stochastic Memory"
        ]
        n = len(players)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                print(f"{players[i].teamname} vs {players[j].teamname}:")
                for m, name in enumerate(mode_names):
                    total1 = sum(board[i][j][m])
                    total2 = sum(board[j][i][m])
                    print(f"  Mode {m} ({name}): {total1:.2f} - {total2:.2f}")
    @staticmethod
    def save_tournament_to_json(players, board, discount, payoff_p1, payoff_p2, filename="tournament_scores.json"):
        """
        Save the full tournament results to a JSON file.

        Args:
            players (list[Player]): Competitors.
            board (4D list): Results from Tournament.tournament().
            discount (float): Discount factor used.
            payoff_p1, payoff_p2 (list[list[int]]): Payoff matrices.
            filename (str): Output path.
        """
        data = {
            "players": [p.teamname for p in players],
            "discount": discount,
            "payoff_player1": payoff_p1,
            "payoff_player2": payoff_p2,
            "results": []
        }
        n = len(players)
        for i in range(n):
            for j in range(i+1, n):
                entry = {"player1": players[i].teamname, "player2": players[j].teamname, "modes": []}
                for m in range(6):
                    entry["modes"].append({
                        "mode": m,
                        "scores_p1": board[i][j][m],
                        "scores_p2": board[j][i][m]
                    })
                data["results"].append(entry)
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
