filepath = 'Chapter 10\\text files\\programming.txt' 

with open(filepath, 'w') as file_object:
    file_object.write('i love programming.\n')
    file_object.write('But i love dogs more.\n')

with open(filepath, 'a') as file_object:
    file_object.write('I\'ve been slacking too much this week : /')
