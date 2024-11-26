import tkinter as tk
import random

class HPBlackJack:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        # Címke a státusz kiíratására
        self.status_label = tk.Label(self.frame, text="Üdv a BlackJack-ben!", font=("Arial", 14))
        self.status_label.pack()

        # Gombok
        self.deal_button = tk.Button(self.frame, text="Kártyát kér", command=self.hp_draw_card)
        self.deal_button.pack(pady=5)

        self.stand_button = tk.Button(self.frame, text="Megáll", command=self.hp_stand)
        self.stand_button.pack(pady=5)

        self.restart_button = tk.Button(self.frame, text="Új játék", command=self.hp_restart_game)
        self.restart_button.pack(pady=5)

        # Pontok megjelenítése
        self.points_label = tk.Label(self.frame, text="Pontszám: 0", font=("Arial", 12))
        self.points_label.pack(pady=10)

        # Adatok
        self.hp_initialize_game()

    def hp_initialize_game(self):
        """Inicializálja a játék állapotát."""
        self.player_points = 0
        self.dealer_points = random.randint(17, 26)  # Az osztó pontszáma fixált tartományban
        self.points_label.config(text="Pontszám: 0")
        self.status_label.config(text="Új játék indult! Húzz kártyát.")
        self.deal_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)

    def hp_draw_card(self):
        """Játékos húz egy kártyát, és frissítjük a pontszámot."""
        card = random.randint(1, 11)  # Egy kártya 1-11 pontot ér
        self.player_points += card
        self.points_label.config(text=f"Pontszám: {self.player_points}")
        self.status_label.config(text=f"Húztál egy {card}-et!")
        self.hp_check_game_status()

    def hp_check_game_status(self):
        """Ellenőrizzük, hogy a játékos túllépte-e a 21-et, vagy nyer-e."""
        if self.player_points > 21:
            self.status_label.config(text="Vesztettél! Túllépted a 21-et.")
            self.deal_button.config(state=tk.DISABLED)
            self.stand_button.config(state=tk.DISABLED)
        elif self.player_points == 21:
            self.status_label.config(text="Nyertél! Elérted a 21-et!")
            self.deal_button.config(state=tk.DISABLED)
            self.stand_button.config(state=tk.DISABLED)

    def hp_stand(self):
        """A játékos megáll, összehasonlítjuk az osztó pontjaival."""
        if self.player_points > self.dealer_points & self.dealer_points < 22:
            self.status_label.config(text=f"Nyertél! Osztó pontszáma: {self.dealer_points}")
        if self.player_points == self.dealer_points:
            self.status_label.config(text=f"Döntetlen! Osztó pontszáma: {self.dealer_points}")
        else:
            self.status_label.config(text=f"Vesztettél! Osztó pontszáma: {self.dealer_points}")
        self.deal_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)

    def hp_restart_game(self):
        self.hp_initialize_game()
