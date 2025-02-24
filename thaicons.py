import tkinter as tk
import random

# List of Thai consonants and their names
thai_consonants = [
    ("ก", "กอ ไก่"), ("ข", "ขอ ไข่"), ("ค", "คอ ควาย"), ("ง", "งอ งู"),
    ("จ", "จอ จาน"), ("ฉ", "ฉอ ฉิ่ง"), ("ช", "ชอ ช้าง"), ("ซ", "ซอ โซ่"),
    ("ญ", "ญอ หญิง"), ("ฎ", "ฎอ ชฎา"), ("ฏ", "ฏอ ปฏัก"), ("ฐ", "ฐอ ฐาน"),
    ("ณ", "ณอ เณร"), ("ด", "ดอ เด็ก"), ("ต", "ตอ เต่า"), ("ถ", "ถอ ถุง")
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("400x300")
        
        self.current_card = None
        
        self.card_label = tk.Label(root, text="", font=("Arial", 48), width=5, height=2, relief="ridge")
        self.card_label.pack(pady=50)
        self.card_label.bind("<Button-1>", self.flip_card)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 14))
        self.next_button.pack()
        
        self.next_card()
    
    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.card_label.config(text=self.current_card[0])
        
    def flip_card(self, event):
        if self.card_label.cget("text") == self.current_card[0]:
            self.card_label.config(text=self.current_card[1])
        else:
            self.card_label.config(text=self.current_card[0])

if __name__ == "__main__":
    root = tk.Tk()
    game = FlashcardGame(root)
    root.mainloop()
