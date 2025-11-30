import csv
from datetime import datetime
from bd_workout_module import BDEdzes

def save_to_csv(entries, filename="workout_data.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Dátum", "Gyakorlat", "Ismétlés", "Súly"])
        for e in entries:
            writer.writerow(e.to_list())


def load_from_csv(filename="workout_data.csv"):
    entries = []
    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                date, exercise, reps, weight = row
                entries.append(BDEdzes(date, exercise, int(reps), float(weight)))
    except:
        pass
    return entries


def format_date(date_string):
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        return date_obj.strftime("%Y-%m-%d")
    except:
        return date_string
