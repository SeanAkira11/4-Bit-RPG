class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self,sentence):
        print(sentence)
    #def bark(sale
class Dog(Animal):
    def __init__(self,name,bark):
        super(Animal,self).__init__(name)
        self.bark = bark

    def speak(self):
        super(Animal,self).speak(self.bark)

pig = Dog("Doge","That's rather strange if I do say so myself")
pig.speak()
#wack = Dog("How's life")
#wack.speak()
#wack.speak()
#pig.speak()
