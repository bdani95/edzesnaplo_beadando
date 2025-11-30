import tkinter as tk
from tkinter import messagebox

from bd_workout_module import BDEdzes, bd_max_weight
from bd_data_handler import save_to_csv, format_date, load_from_csv
from bd_visualize import show_weight_progress


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("BD Edzésnapló")

        self.entries = load_from_csv()

        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="Dátum (YYYY-MM-DD):").grid(row=0, column=0)
        tk.Label(frame, text="Gyakorlat:").grid(row=1, column=0)
        tk.Label(frame, text="Ismétlés:").grid(row=2, column=0)
        tk.Label(frame, text="Súly (kg):").grid(row=3, column=0)

        self.date_entry = tk.Entry(frame)
        self.exercise_entry = tk.Entry(frame)
        self.reps_entry = tk.Entry(frame)
        self.weight_entry = tk.Entry(frame)

        self.date_entry.grid(row=0, column=1)
        self.exercise_entry.grid(row=1, column=1)
        self.reps_entry.grid(row=2, column=1)
        self.weight_entry.grid(row=3, column=1)

        tk.Button(frame, text="Hozzáadás", command=self.add_entry).grid(row=4, column=0, columnspan=2, pady=5)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack()

        for e in self.entries:
            self.listbox.insert(tk.END, f"{e.date} – {e.exercise} – {e.reps} ism. – {e.weight} kg")

        tk.Button(root, text="Törlés", command=self.delete_entry).pack(pady=5)
        tk.Button(root, text="Max súly kiszámítása", command=self.show_max_weight).pack(pady=5)
        tk.Button(root, text="Mentés CSV-be", command=self.save).pack(pady=5)
        tk.Button(root, text="Grafikon megjelenítése", command=self.show_graph).pack(pady=5)
        tk.Button(root, text="Kilépés", command=self.exit_app).pack(pady=5)

    def add_entry(self):
        date = format_date(self.date_entry.get())
        exercise = self.exercise_entry.get()
        reps = self.reps_entry.get()
        weight = self.weight_entry.get()

        if not (date and exercise and reps and weight):
            messagebox.showwarning("Hiba", "Minden mezőt ki kell tölteni!")
            return

        try:
            reps = int(reps)
            weight = float(weight)
        except:
            messagebox.showerror("Hiba", "Ismétlés és súly csak szám lehet!")
            return

        entry = BDEdzes(date, exercise, reps, weight)
        self.entries.append(entry)

        self.listbox.insert(tk.END, f"{date} – {exercise} – {reps} ism. – {weight} kg")

        self.date_entry.delete(0, tk.END)
        self.exercise_entry.delete(0, tk.END)
        self.reps_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)

    def delete_entry(self):
        index = self.listbox.curselection()
        if not index:
            return
        self.listbox.delete(index)
        del self.entries[index[0]]

    def show_max_weight(self):
        exercise = self.exercise_entry.get()
        if not exercise:
            messagebox.showinfo("Info", "Adj meg egy gyakorlatot a mezőben!")
            return

        result = bd_max_weight(self.entries, exercise)
        messagebox.showinfo("Max súly", f"{exercise} - max súly: {result} kg")

    def save(self):
        save_to_csv(self.entries)
        messagebox.showinfo("Siker", "Adatok elmentve workout_data.csv fájlba.")

    def show_graph(self):
        exercise = self.exercise_entry.get()
        if not exercise:
            messagebox.showinfo("Info", "Adj meg egy gyakorlatot a grafikonhoz!")
            return
        show_weight_progress(self.entries, exercise)

    def exit_app(self):
        self.root.destroy()
