import matplotlib.pyplot as plt

def show_weight_progress(entries, exercise_name):
    filtered = [e for e in entries if e.exercise == exercise_name]
    if not filtered:
        return

    dates = [e.date for e in filtered]
    weights = [e.weight for e in filtered]

    plt.figure(figsize=(8, 4))
    plt.plot(dates, weights, marker="o")
    plt.title(f"Súly alakulása: {exercise_name}")
    plt.xlabel("Dátum")
    plt.ylabel("Súly (kg)")
    plt.grid(True)
    plt.show()
