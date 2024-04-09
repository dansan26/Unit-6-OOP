class String:
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return self.value
    def __repr__(self):
        return f"String: {self.value}"
    def __add__(self, other):
        if isinstance(other, String):
            text = self.value + other.value
        raise TypeError('Cannot concatenate String with non-string objects')
if __name__ == '__main__':
    text = String('Hello World!')
    print(text)
    print(repr(text))
    s1 = String('Hello')
    s2 = String('World!')
    print(s1 + s2)