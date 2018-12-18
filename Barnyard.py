class Animal:
    def __init__(self,bark):
        self.bark = bark

    def speak(self):
        print(self.bark)
pig = Animal("That's rather strange if I do say so myself")
pig.speak()
wack = Animal("How's life")
wack.speak()
wack.speak()
pig.speak()
