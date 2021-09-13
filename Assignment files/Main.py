import csv
import tkinter as tk

class MainApplication():

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()




def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()