import tkinter as tk
import random

class LuckyDrawApp:
    def __init__(self, staff_names_file):
        self.staff_names_file = staff_names_file
        self.winners = []
        self.draw_count = 1

        self.window = tk.Tk()
        self.window.title("Company Lucky Draw 2023")
        self.window.geometry ('750x800')
        
        self.winner_label = tk.Label(self.window, text="Winner: ", font=('Arial', 35))
        self.winner_label.pack(pady=10)
        self.winner_label.place(x=60, y=130)

        self.draw_button = tk.Button(self.window, text="\n 2023抽獎\n Good Luck & Good Health\n ", bg='blue', fg='white', font=('Arial', 18), command=self.lucky_draw)
        self.draw_button.pack(pady=30)
        self.draw_button.place(x=40, y=350)

        self.winners_listbox = tk.Listbox(self.window, width = 25, height= 31, font=('Arial', 17))
        self.winners_listbox.pack(pady=10)
        self.winners_listbox.place(x=400, y=10)

        self.export_button = tk.Button(self.window, text="Export", font=('Arial', 20), command=self.export_listbox_content)
        self.export_button.pack(pady=10)
        self.export_button.place(x=100, y=500)

        self.load_staff_names()

    def load_staff_names(self):
        try:
            with open(self.staff_names_file, 'r', encoding='utf-8') as file:
                self.staff_names = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"Staff names file '{self.staff_names_file}' not found.")
            self.staff_names = []

    def lucky_draw(self):
        if self.staff_names:
            winner = random.choice(self.staff_names)
            self.staff_names.remove(winner)
            self.winners.append(winner)
            self.winner_label.config(text="Winner: \n\n" + winner)
            self.winners_listbox.insert(tk.END, f"{self.draw_count}. {winner}")
            self.draw_count += 1

    def export_listbox_content(self):
        if self.winners:
            file_name = "winners.txt"
            with open(file_name, "w", encoding='utf-8') as file:
                for item in self.winners:
                    file.write(item + "\n")
            print(f"Listbox content exported to {file_name}")

    def run(self):
        self.window.mainloop()

# Staff names file path
staff_names_file = "staff_names.txt"

# Create the lucky draw app
lucky_draw_app = LuckyDrawApp(staff_names_file)

# Run the app
lucky_draw_app.run()
