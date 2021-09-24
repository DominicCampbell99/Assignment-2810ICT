
# you can import python code via the filename (in this case we're importing search.py)
import search

# create an instance of the SearchKeyword class
# path needs to be backslashed, and backslashes need to be escaped
searcher = search.SearchKeyWord('..\\Assignment files\\reviews_dec18.csv')

# use the search method of the class to find the keyword
results = []

while (len(results) == 0):
    searchTerm = input("enter a search term: ")
    results = searcher.search(searchTerm)
    if (len(results) == 0):
        print('No results found.')

#print(result)
ids = []
for result in results:
    ids.append(result[1])

print(ids)