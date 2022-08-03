#https://replit.com/@apnatvar/boilerplate-probability-calculator#prob_calculator.py

import copy
import random
# Consider using the modules imported above.

class Hat:

    balls = dict()
    tBalls = 0
    contents = []

    def __init__(self, **kwargs):
        self.balls = kwargs
        self.contents = self.makeContent(kwargs)
        self.totalBalls(kwargs)

    def totalBalls(self, ballsDict):
        self.tBalls = 0
        for i in ballsDict:
            self.tBalls += ballsDict[i]

    def makeContent(self, ballsDict):
        ballsList = []
        for i in ballsDict:
            for _ in range(0, ballsDict[i]):
                ballsList.append(i)
        return ballsList

    def draw(self, toDraw):
        if toDraw >= len(self.contents):
            ballsDrawn = copy.deepcopy(self.contents)
            return ballsDrawn

        ballsDrawn = []
        for _ in range(toDraw):
            ballsDrawn.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
        return ballsDrawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_list = hat.makeContent(expected_balls)
    success = 0
    for i in range(num_experiments):
        fail = False
        hat.contents = hat.makeContent(hat.balls)
        ballsDrawn = hat.draw(num_balls_drawn)
        for e in expected_balls_list:
            try:
                ballsDrawn.remove(e)
            except:
                fail = True
                break
        if fail:
            continue
        success += 1
    return success/num_experiments

random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
