import csv
import tkinter as tk
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP

class MainApplication():

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.setupApplication()
        
        

    def setupApplication(self):
        self.SearchBar = tk.Frame(self.master)
        self.SearchBar.pack(side=TOP)
        self.ResultsTableFrame = tk.Frame(self.master)
        self.ResultsTableFrame.pack(side=LEFT, padx=100, pady= 100)
        self.GraphFrame = tk.Frame(self.master)
        self.GraphFrame.pack(side=RIGHT, padx=100, pady=100)

        self.SearchButton = tk.Button(self.SearchBar, text="Search", width=20, command = self.OnSearchPress)
        self.SearchButton.grid(column=10, row=1)

        self.ClearButton = tk.Button(self.SearchBar, text="Clear", width=20, command=self.OnClearPress)
        self.ClearButton.grid(column=10, row=2)

        self.DateBox1Label = tk.Label(self.SearchBar, text='First Date')
        self.DateBox1Label.grid(column=2, row=1)
        self.DateBox1 = tk.Entry(self.SearchBar)
        self.DateBox1.grid(column=2, row=2, padx = 5, pady = 5)


        self.DateBox2Label = tk.Label(self.SearchBar, text ='Last Date')
        self.DateBox2Label.grid(column=3, row=1 )
        self.DateBox2 = tk.Entry(self.SearchBar)
        self.DateBox2.grid(column=3, row=2, padx = 5, pady = 5)

        self.SuburbLabel = tk.Label(self.SearchBar, text ='Suburb')
        self.SuburbLabel.grid(column=4, row=1)
        self.Suburb = tk.Entry(self.SearchBar)
        self.Suburb.grid(column=4, row=2, padx = 5, pady = 5)

        self.KeywordLabel = tk.Label(self.SearchBar, text ='Suburb')
        self.KeywordLabel.grid(column=5, row=1)
        self.Keyword = tk.Entry(self.SearchBar)
        self.Keyword.grid(column=5, row=2, padx = 5, pady = 5)
        
    def set_Date1(self):
        date = self.DateBox1.get()
        return date

    def set_Date2(self):
        print("kkk")

    def OnSearchPress(self):
        date1 = self.set_Date1()
        print("Search")
        print("date:", date1)

    def OnClearPress(self): 
        print("clear") 
        


def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.master.title("Hotel Analysis App")
    root.mainloop()

if __name__ == '__main__':
    main()