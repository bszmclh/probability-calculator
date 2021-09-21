import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for a in kwargs:
            for i in range(kwargs[a]):
                self.contents.append(a)
        
        self.balls = kwargs
        
    
    def draw(self, num):
        max = len(self.contents)
        if num > max: 
             num = max
        
        drawed = []
        for i in range(num):
            seed = random.randint(0, len(self.contents)-1)
            drawed.append(self.contents[seed])
            del self.contents[seed]

        return drawed

            
    
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successed = 0
    for i in range(num_experiments):
        newHat = copy.deepcopy(hat)
        drawed = newHat.draw(num_balls_drawn)
        success = True
        for color in expected_balls:
            if expected_balls[color] > drawed.count(color):
                success = False
                break
        
        if success: successed+=1
    
    return successed / num_experiments
