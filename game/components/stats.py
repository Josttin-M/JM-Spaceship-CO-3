class Stats:
    
    def __init__(self):
        self.score = 0
        self.death_count = 0
        self.max_score = 0

    def reset_stats(self):
        self.score = 0

    def add_death_count(self):
        self.death_count += 1

    def update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score