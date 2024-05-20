class Person:
    def __init__(self, name, age, ssn):
        self.name = name # public attribute
        self._age = age # protected attribute
        self.__ssn = ssn # private attribute

    # Getter for the name
    def get_name(self):
        return self.name
    # Setter for the name
    def set_name(self, value):
        if isinstance(value,str) and value.isalpha():
            self._name = value
        else:
            raise ValueError('Name must be a string and containing only letters')
    @property
    def age(self):
        return self._age


person = Person('David', 20, '123-132-1091')
print(person.name) # Output: David
print(person._age) # (accessible)
# print(person.__ssn) # Attribute Error
print(person._Person__ssn)