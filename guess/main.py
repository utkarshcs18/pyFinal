import random as r
import tkinter as tk
from tkinter import font as tkfont

BG = "#0d0d15"
PANEL = "#15152a"
ACCENT = "#00f0ff"
ACCENT2 = "#ff2e88"
SUCCESS = "#39ff14"
WARN = "#ffb400"
TEXT = "#e8e8f0"
MUTED = "#7a7a90"


class GuessGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("⚡ GUESS THE NUMBER ⚡")
        self.geometry("480x560")
        self.configure(bg=BG)
        self.resizable(False, False)

        self.target = 0
        self.attempts = 0
        self.low_bound = 1
        self.high_bound = 1000

        self._load_fonts()
        self._build_ui()
        self.new_game()

    def _load_fonts(self):
        self.f_title = tkfont.Font(family="Consolas", size=26, weight="bold")
        self.f_sub = tkfont.Font(family="Consolas", size=11)
        self.f_big = tkfont.Font(family="Consolas", size=48, weight="bold")
        self.f_entry = tkfont.Font(family="Consolas", size=20, weight="bold")
        self.f_btn = tkfont.Font(family="Consolas", size=13, weight="bold")
        self.f_feedback = tkfont.Font(family="Consolas", size=15, weight="bold")
        self.f_stats = tkfont.Font(family="Consolas", size=11)

    def _build_ui(self):
        tk.Label(self, text="GUESS THE NUMBER", font=self.f_title,
                 fg=ACCENT, bg=BG).pack(pady=(28, 0))
        self.range_label = tk.Label(self, text="", font=self.f_sub,
                                     fg=MUTED, bg=BG)
        self.range_label.pack(pady=(4, 18))

        card = tk.Frame(self, bg=PANEL, highlightbackground=ACCENT,
                         highlightthickness=2, bd=0)
        card.pack(padx=30, pady=0, fill="both")

        self.feedback_label = tk.Label(card, text="MAKE A GUESS", font=self.f_feedback,
                                        fg=ACCENT2, bg=PANEL, pady=18)
        self.feedback_label.pack()

        self.display_label = tk.Label(card, text="?", font=self.f_big,
                                       fg=TEXT, bg=PANEL)
        self.display_label.pack(pady=(0, 10))

        entry_frame = tk.Frame(card, bg=PANEL)
        entry_frame.pack(pady=10)
        self.entry = tk.Entry(entry_frame, font=self.f_entry, justify="center",
                               width=8, bg="#0a0a12", fg=ACCENT,
                               insertbackground=ACCENT, relief="flat",
                               highlightbackground=ACCENT, highlightthickness=2)
        self.entry.pack(ipady=8)
        self.entry.bind("<Return>", lambda e: self.make_guess())
        self.entry.focus_set()

        self.guess_btn = tk.Button(card, text="⟩⟩ SUBMIT GUESS ⟨⟨", font=self.f_btn,
                                    bg=ACCENT, fg="#001015", activebackground=ACCENT2,
                                    activeforeground="#001015", relief="flat",
                                    cursor="hand2", command=self.make_guess)
        self.guess_btn.pack(pady=(14, 20), ipadx=10, ipady=8)

        stats_frame = tk.Frame(card, bg=PANEL)
        stats_frame.pack(pady=(0, 20))
        self.attempts_label = tk.Label(stats_frame, text="Attempts: 0", font=self.f_stats,
                                        fg=MUTED, bg=PANEL)
        self.attempts_label.grid(row=0, column=0, padx=14)
        self.bounds_label = tk.Label(stats_frame, text="", font=self.f_stats,
                                      fg=MUTED, bg=PANEL)
        self.bounds_label.grid(row=0, column=1, padx=14)

        self.restart_btn = tk.Button(self, text="🔄  PLAY AGAIN", font=self.f_btn,
                                      bg=ACCENT2, fg="#1a0010", activebackground=SUCCESS,
                                      relief="flat", cursor="hand2", command=self.new_game)

    def new_game(self):
        self.target = int(r.random() * 1000) + 1
        self.attempts = 0
        self.low_bound = 1
        self.high_bound = 1000
        self.range_label.config(text="I'm thinking of a number between 1 and 1000")
        self.feedback_label.config(text="MAKE A GUESS", fg=ACCENT2)
        self.display_label.config(text="?", fg=TEXT)
        self.attempts_label.config(text="Attempts: 0")
        self.bounds_label.config(text="Range: 1 - 1000")
        self.entry.config(state="normal", bg="#0a0a12")
        self.entry.delete(0, tk.END)
        self.guess_btn.config(state="normal")
        self.restart_btn.pack_forget()
        self.entry.focus_set()

    def make_guess(self):
        raw = self.entry.get().strip()
        if not raw.lstrip("-").isdigit():
            self.feedback_label.config(text="NUMBERS ONLY!", fg=WARN)
            return

        guess = int(raw)
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        self.display_label.config(text=str(guess))
        self.entry.delete(0, tk.END)

        if guess == self.target:
            self.feedback_label.config(
                text=f"🎉 CORRECT! IN {self.attempts} TRIES!", fg=SUCCESS)
            self.display_label.config(fg=SUCCESS)
            self.entry.config(state="disabled")
            self.guess_btn.config(state="disabled")
            self.restart_btn.pack(pady=18, ipadx=10, ipady=6)
            return

        elif guess < self.target:
            self.feedback_label.config(text="↑ TOO LOW — GO HIGHER", fg=ACCENT)
            self.low_bound = max(self.low_bound, guess + 1)
        else:
            self.feedback_label.config(text="↓ TOO HIGH — GO LOWER", fg=ACCENT2)
            self.high_bound = min(self.high_bound, guess - 1)

        self.bounds_label.config(text=f"Range: {self.low_bound} - {self.high_bound}")
        self.entry.focus_set()


if __name__ == "__main__":
    GuessGame().mainloop()