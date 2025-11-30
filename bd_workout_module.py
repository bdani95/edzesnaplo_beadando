class BDEdzes:
    def __init__(self, date, exercise, reps, weight):
        self.date = date
        self.exercise = exercise
        self.reps = reps
        self.weight = weight

    def to_list(self):
        return [self.date, self.exercise, self.reps, self.weight]


def bd_max_weight(entries, exercise_name):
    filtered = [e.weight for e in entries if e.exercise == exercise_name]
    return max(filtered) if filtered else 0
