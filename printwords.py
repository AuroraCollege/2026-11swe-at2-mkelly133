import csv

with open('words.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    word_lists = []
    for row in (reader):
        list = []
        for word in row:
            list.append(word)
        word_lists.append(list)

word_list=word_lists[1]
print(word_list)