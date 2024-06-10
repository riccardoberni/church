import tkinter as tk
import os
import pandas as pd




CALENDAR = [["SONOBELLO", "PALOMA"], ["CUCADORES", "SONOBELLO"]]

class Tournament():
    def __init__(self) -> None:
        
        self.teamA = []
        self.teamB = []
        self.risultato=[]
        
        self.window = tk.Tk()
        self.window.columnconfigure(0, weight=4)
        self.window.columnconfigure(1, weight=3)
        self.window.columnconfigure(2, weight=3)
        self.window.geometry("340x100")
        self.window.title("Partita numero 1")
        self.window.resizable(0, 0)
        
        self.team1_points = tk.StringVar()
        self.team2_points = tk.StringVar()
        
        # TEAM 1 COLUMN
        first_team = tk.Label(self.window, text=self.teamA)
        first_team.grid(column=1, row=11, sticky=tk.N, padx=5, pady=5)

        team1_score = tk.Entry(self.window, textvariable=self.team1_points)
        team1_score.grid(column=1, row=12, sticky=tk.W, padx=1, pady=1)

        # TEAM 2 COLUMN
        second_team = tk.Label(self.window, text=self.teamB)
        second_team.grid(column=2, row=11, sticky=tk.N, padx=5, pady=5)

        team2_score = tk.Entry(self.window, textvariable=self.team2_points)
        team2_score.grid(column=2, row=12, sticky=tk.W, padx=1, pady=1)

        # CONFIRM BUTTON
        confirm = tk.Button(self.window, text="Conferma", command=self.write_result)
        confirm.grid(column=3, row=50, sticky=tk.W, padx=1, pady=1)
                
    
    def write_result(self):
        self.risultato.append(self.team1_points.get() + "-" + self.team2_points.get())
        dict = {"casa": [self.teamA], "tradsferta": [self.teamB], "risultato": self.risultato}
        df = pd.DataFrame(dict)
        print(str(self.risultato))
        df.to_csv("prova.csv")
        self.window.destroy()
        return
    
    def play(self):
        self.window.mainloop()
        
    def start(self):
        i = 0
        while i < len(CALENDAR):
            self.teamA = CALENDAR[i][0]
            self.teamB = CALENDAR[i][1]
            i+=1
        return

        
        

if __name__ == "__main__":
    t = Tournament()
    t.start()
    

