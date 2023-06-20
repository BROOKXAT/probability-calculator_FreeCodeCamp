import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)

    def __str__(self):
        return "content :" + str(self.contents)

    def draw(self, num_balls_to_draw):
        if num_balls_to_draw >= len(self.contents):
            return self.contents
        picked_balls = random.sample(self.contents, num_balls_to_draw)
        for ball in picked_balls:
            self.contents.remove(ball)
        return picked_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0

    for i in range(num_experiments):
        flag = False
        hat_copy = copy.deepcopy(hat)
        picked_balls = hat_copy.draw(num_balls_drawn)
        for color, count in expected_balls.items():
            if picked_balls.count(color) < count:
                flag = True
        if flag: continue
        M += 1
    return M / num_experiments
