def dictionary_reader(first, last, age=''):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    return person

somebody = dictionary_reader('valentin', 'mirchev', 22)
print(somebody)
