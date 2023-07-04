def is_isogram(string):
    return len(set(i.lower() for i in string if i.isalpha())) == len([i.lower() for i in string if i.isalpha()])
