""" Sorts the list by the reverse word order and in descending order
lambda x: x[::-1] reverses each word
reverse = True, reverses the sorting
"""

list1 = ['Jane', 'Superman', 'Bane',  'Batman', 'Benny', 'Johny']
list1.sort(key = lambda x: x[::-1], reverse = True)
print(list1)