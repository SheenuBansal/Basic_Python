import wikipedia
wikipedia.set_lang('en')
print(wikipedia.summary("Madhuri Dixit", sentences=1))
ny = wikipedia.page("Madhuri Dixit")
print(ny.content)
print(ny.url)
print(wikipedia.search("Madhuri Dixit"))
print(ny.original_title)
print(ny.references)
print(ny.categories)
print(ny.links)
print(wikipedia.random(5))
print(ny.images)

# Getting the wikipedia page in full html format
print(ny.html())

#Finding Pages Based on Coordinates
print(wikipedia.geosearch(37.787,-122.4))
print(wikipedia.page(37.787, -122.4))

#Get all the languages supported by wikipedia
print(wikipedia.languages())

'''
Suggestions related to the search result, 
It gives matching results even if we type the
wrong spellings.. & shows none if does not 
get what we want to search '''

print(wikipedia.suggest("Sanja dutt"))
