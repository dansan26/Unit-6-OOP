class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def speak(self):
        return f'{self.name} says {self.sound}'
    
class Dog(Animal):
    def __init__(self, name, sound, breed):
        # Call to the superclass constructor (using the variables from parent class)
        super().__init__(name, sound)
        self.breed = breed
    def fetch(self, item):
        return f'{self.name} fetched the item: {item}'
    
class Cat(Animal):
    def __init__(self, name, sound, favorite_toy):
        super().__init__(name, sound)
        self.favorite_toy = favorite_toy
    def play(self):
        return f"{self.name}'s favorite toy to play with is {self.favorite_toy}"

if __name__ == '__main__':
    dog = Dog('Hershey', 'Bark', 'Golden Retriever')
    cat = Cat('Munchkin', 'Meow', 'Rope')
    print(f'{dog.speak()}\n{dog.fetch('bone')}')
    print(f'{cat.speak()}\n{cat.play()}')
