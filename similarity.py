# -------------------------------------------------------------------------
# AUTHOR: Paul Puma
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4440 (Data Mining) - Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy or pandas.
#You have to work here only with standard dictionaries, lists, and arrays

# Importing some Python libraries
import csv
from sklearn.metrics.pairwise import cosine_similarity

documents = []

#reading the documents in a csv file
with open('cleaned_documents.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         documents.append (row)

#Building the document-term matrix by using binary encoding.
#You must identify each distinct word in the collection using the white space as your character delimiter.
#--> add your Python code here
docTermMatrix = []
unique_words = set()
for i, row in enumerate(documents):
    words = row.split() 
    unique_words.update(words)
    # docTermMatrix.appends(words)
for i, row in enumerate(documents):
    words = row.split()
    # splitting the words in each document can be used as an index
    # for example the row [apple,car,idea] is compared to the unique words [apple, car,math,yellow, idea]
    # if the word appears on the set of values then append on the row i the value 1 other than that 0;
    for word in words:
        if word in unique_words:
          docTermMatrix[i].append(1)
        else:
          docTermMatrix[i].append(0)


# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here
highest_similarity = 0
for i, row in enumerate(docTermMatrix):
    for j, row2 in enumerate(docTermMatrix):
      if i != j:
        cosine_similarities = cosine_similarity([row],[row2])
        if cosine_similarities > highest_similarity:
          highest_similarity = cosine_similarities

print(highest_similarity)

# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here