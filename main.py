import tkinter as tk
from hp_blackjack import HPBlackJack

def main():
    root = tk.Tk()
    root.title("BlackJack App")
    app = HPBlackJack(root)
    root.mainloop()

if __name__ == "__main__":
    main()
