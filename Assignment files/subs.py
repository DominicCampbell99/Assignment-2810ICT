import csv

class Subs:
    def __init__(self, file):
        self.file = file

    def get_suburbs(self):
        # Open the CSV file
        file = open(self.file, encoding="utf8")

        # Read the CSV file
        reader = csv.reader(file)
        next(reader)

        # Iterate the rows inside the CSV file
        searchResults = []
        for row in reader:
            Neighbourhood = row[1]
            searchResults.append(Neighbourhood)

        return searchResults