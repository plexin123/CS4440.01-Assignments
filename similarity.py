# -------------------------------------------------------------------------
# AUTHOR: Paul Puma
# FILENAME: document_similarity.py
# SPECIFICATION: Build document-term matrix with binary encoding and find most similar documents
# FOR: CS 4440 (Data Mining) - Assignment #1
# TIME SPENT: [Fill in your time]
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
         documents.append(row)

docTermMatrix = []
unique_words = set()

for row in documents:
    text = row[1] if row else ""
    words = text.split() 
    unique_words.update(words)


unique_words = sorted(list(unique_words))

for row in documents:
    text = row[1] if row else ""
    words = text.split()
    temp = []
    # splitting the words in each document can be used as an index
    # for example the row [apple,car,idea] is compared to the unique words [apple, car,math,yellow, idea]
    # if the word appears on the set of values then append on the row i the value 1 other than that 0;
    for word in unique_words:
        if word in words:
          temp.append(1)
        else:
          temp.append(0)
          
    docTermMatrix.append(temp)


# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here
highest_similarity = 0
doc1 = 0
doc2 = 0

for i, row in enumerate(docTermMatrix):
    for j, row2 in enumerate(docTermMatrix):
      # Fix: Only check j > i to avoid duplicates and comparing document with itself
      if j > i:
        cosine_similarities = cosine_similarity([row], [row2])
        # Fix: cosine_similarity returns a 2D array, need to extract the value
        similarity_value = cosine_similarities[0][0]
        if similarity_value > highest_similarity:
          highest_similarity = similarity_value
          doc1 = i
          doc2 = j

# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here
print(f"The most similar documents are document {doc1} and document {doc2} with cosine similarity = {highest_similarity}")