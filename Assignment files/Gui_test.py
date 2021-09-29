import csv
import tkinter as tk
import numpy as np
from tkcalendar import Calendar
from tkinter import ttk
from tkinter.constants import BOTTOM, LEFT, NE, NW, RIGHT, TOP
from time import sleep
import pandas as pd
import search
import subs


class MainApplication():

    def __init__(self, master):
        self.dataFrame = pd.read_csv('Assignment files\calendar_dec18.csv', parse_dates=['date'])
        self.master = master
        self.setupApplication()
        # load the csv file

        self.importantInfo = [(1, 'Data', 'MoreData'),
                              (2, "data", 'More data'),
                              (1, 'Data', 'MoreData'),
                              (2, "data", 'More data'),
                              (1, 'Data', 'MoreData'),
                              (2, "data", 'More data'),
                              (1, 'Data', 'MoreData'),
                              (2, "data", 'More data'),
                              (1, 'Data', 'MoreData'),
                              (2, "data", 'More data'),
                              (1, 'Data', 'MoreData'),
                              ]

    def setupApplication(self):
        # Setting up Search Bar Frame
        self.SearchBar = tk.Frame(self.master, width=1200, height=150, borderwidth=1, relief=tk.RIDGE)
        self.SearchBar.pack(fill='both')

        # setting up important Window with scrolable Frame
        self.canvas = tk.Canvas(self.master, borderwidth=1, relief=tk.RIDGE)
        self.scrollbar = tk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview)
        self.ResultsTable = tk.Frame(self.canvas, borderwidth=1, relief=tk.RIDGE)
        self.ResultsTable.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.canvas.create_window((0, 0), window=self.ResultsTable, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=LEFT, fill='both', expand=True)
        self.scrollbar.pack(side=LEFT, fill="y")

        # setting up graph frame
        self.GraphFrame = tk.Frame(self.master, width=250, height=500, borderwidth=1, relief=tk.RIDGE)
        self.GraphFrame.pack(side=RIGHT, expand=True, fill="both")

        # Making Buttons inside frame
        self.ButtonFrame = tk.Frame(self.SearchBar, width=100, height=100)
        self.ButtonFrame.grid(column=8, row=2)

        self.SearchButton = tk.Button(self.ButtonFrame, text="Search", width=20, bg='#346ce3',
                                      command=self.OnSearchPress)
        self.SearchButton.grid(column=1, row=1, padx=40, pady=10)

        self.ClearButton = tk.Button(self.ButtonFrame, text="Clear", width=20, bg='#346ce3', command=self.OnClearPress)
        self.ClearButton.grid(column=1, row=2, padx=40, pady=10)

        # making Input Boxes
        self.InputFrame = tk.Frame(self.SearchBar, width=500, height=100)
        self.InputFrame.grid(column=1, row=2)

        self.DateBox1Label = tk.Label(self.InputFrame, text='First Date')
        self.DateBox1Label.grid(column=2, row=1)

        self.Cal1 = Calendar(self.InputFrame, selectmode='day')
        self.Cal1.grid(column=2, row=2, padx=5, pady=5)

        self.DateBox2Label = tk.Label(self.InputFrame, text='Last Date')
        self.DateBox2Label.grid(column=3, row=1)

        self.Cal2 = Calendar(self.InputFrame, selectmode='day')
        self.Cal2.grid(column=3, row=2, padx=5, pady=5)

        # suburb Search
        self.SuburbLabel = tk.Label(self.InputFrame, text='Suburb')
        self.SuburbLabel.grid(column=4, row=1)

        subss = subs.Subs('..\\Assignment files\\neighbourhoods_dec18.csv')
        self.suburbs = subss.get_suburbs()
        self.SuburbCombo = ttk.Combobox(self.InputFrame, values=self.suburbs, postcommand=self.ComboClick)
        self.SuburbCombo.grid(column=4, row=2, padx=5, pady=5)

        self.KeywordLabel = tk.Label(self.InputFrame, text='Keyword')
        self.KeywordLabel.grid(column=5, row=1)
        self.Keyword = tk.Entry(self.InputFrame)
        self.Keyword.grid(column=5, row=2, padx=5, pady=5)

        self.var = tk.IntVar()
        self.CheckFamilySearch = tk.Checkbutton(self.InputFrame, text="Family Search", command=self.OnCheck(),
                                                cursor='arrow', variable=self.var, onvalue=1, offvalue=0)
        self.CheckFamilySearch.grid(column=6, row=1)

    def OnCheck(self):
        if self.var.get() == 1:
            self.new = tk.Toplevel()
            self.BedsNeededLabel = tk.Label(self.new, text='Beds needed')
            self.BedsNeededLabel.grid(column=7, row=1)
            self.BedsNeeded = tk.Entry(self.new)
            self.BedsNeeded.grid(column=7, row=2, padx=5, pady=5)
        elif self.var.get() == 0:
            print("OFF")

    def dateSearch(self, dateInput1, dateInput2):

        # query for set between two dates
        query = "date >= '" + dateInput1 + "' and date < '" + dateInput2 + "'"
        self.dateResults = self.dataFrame.query(query)

        # filter for uniques
        uniqueResults = self.dateResults.drop_duplicates(subset=['listing_id'])

        # convert to array
        dateList = uniqueResults.listing_id.tolist()
        return dateList

    def ComboClick(self):
        # self.suburbs = self.key.get_suburbs()
        suburbs_left = []
        val = self.SuburbCombo.get()
        print(val)
        for i in self.suburbs:
            if i.find(val) != -1:
                suburbs_left.append(i)

        self.SuburbCombo.configure(values=suburbs_left)

        return None

    def updateTable(self):
        rows = len(self.importantInfo)
        columns = len(self.importantInfo[0])
        for i in range(rows):
            for j in range(columns):
                self.Table = tk.Entry(self.ResultsTable, width=10, fg='blue',
                                      font=('Arial', 16, 'bold'))

                self.Table.grid(row=i, column=j)
                self.Table.insert(tk.END, self.importantInfo[i][j])

    def UpdateGraph(self):
        return None

    def set_Date1(self):
        date = self.Cal1.get_date()
        return date

    def set_Date2(self):
        date = self.Cal2.get_date()
        return date

    def OnSearchPress(self):
        date1 = self.set_Date1()
        date2 = self.set_Date2()
        dateSearch = self.dateSearch(date1, date2)
        print(date1)

        key = search.SearchKeyWord('..\\Assignment files\\reviews_dec18.csv')
        suburb = search.SearchKeyWord('..\\Assignment files\\listings_summary_dec18.csv')

        searchTermsub = self.Keyword.get()
        values = suburb.search(searchTermsub)
        Suburb_List = []
        for value in values:
            Suburb_List.append(value[0])

        # use the search method of the class to find the keyword
        searchTerm = self.Keyword.get()
        results = key.search(searchTerm)
        # print(result)
        Keyword_list = []
        for result in results:
            Keyword_list.append(result[1])

        print(Keyword_list)

        fin_list = [i for i in dateSearch if i in Suburb_List + Keyword_list]
        print(fin_list)

        self.updateTable()
        self.OnCheck()

    def OnClearPress(self):
        print("clear")


def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.master.title("Hotel Analysis App")
    app.master.geometry('1200x1200')
    app.master.resizable(True, True)
    root.mainloop()


if __name__ == '__main__':
    main()