emotions = {"happy": 3, "stress": 2, "sad": 1}

class Person(): 
    ''' 
    This will represent a person, and their emotion
    ''' 

    def __init__(self, name, emotion): 
        self.name = name 
        self.emotion = emotion 

    def __str__(self): 
        return f'{self.name} is feeling {self.emotion}'

    def display(self): 
        feeling_level = emotions[self.emotion] 
        feeling = []
        
        if feeling_level == 1: 
            feeling_level = 'low'
        elif feeling_level == 2: 
            feeling_level = 'medium'
        elif feeling_level == 3: 
            feeling_level = 'high'
        return f'{self.name} is feeling a {feeling_level} amount of {self.emotion} '
        


jacob = Person('jacob', 'sad')
john = Person('john', 'happy')
jingle = Person('jim', 'stress')
print(jacob.display())
print(john.display())
print(jingle.display())