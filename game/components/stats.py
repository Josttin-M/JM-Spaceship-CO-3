class Stats:
    def __init__(self):
        self.score = 0
        self.death_count = 0
        self.score_history = [0]

    def reset_stats(self):
        self.score = 0

    def add_score(self):
        self.score_history.append(self.score)

    def get_max_score(self):
        return max(self.score_history)