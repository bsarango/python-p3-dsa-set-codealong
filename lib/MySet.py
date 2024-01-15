class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        #returning the following statement will return a bool, not a value
        #So, this statement will always work even if there is no match in value
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        #pop is a built in method for dictionaries to delete keys and values
        #the second argument is optional for if there isn't the existing value in the dictionary
        return self

    def size(self):
        return len(self.dictionary)