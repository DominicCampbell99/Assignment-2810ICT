import csv

class SearchKeyWord:
    def __init__(self, file):
        self.file = file

    def search(self, word):
        # Open the CSV file
        file = open(self.file, encoding="utf8")

        # Read the CSV file
        reader = csv.reader(file)

        # Iterate the rows inside the CSV file
        searchResults = []
        for row in reader:
            # we know the comment is column 6, which is array index [5]
            comment = row[5]
            if (word in comment):
                searchResults.append(row)

        # print out the 2nd column of the first result
                # searchResult = [
        #     [listing_id, id, date, reviewer_id, reviewer_name, comment],
        #     [listing_id, id, date, reviewer_id, reviewer_name, comment],
        #     [listing_id, id, date, reviewer_id, reviewer_name, comment],
        #     [listing_id, id, date, reviewer_id, reviewer_name, comment],
        #     [listing_id, id, date, reviewer_id, reviewer_name, comment],
        # ]
        # for result in searchResults:
        #     print(result[1] + ', ' + result[2])
        return searchResults