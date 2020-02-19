import math

class Game:
    def __init__(self, lvl): 
        self.msg = {
                    'greet': "Hello, my fellow friend! Do you throw the dices? y/n ",
                    'quest': "Excellent! Hit 'Enter' for new throw, and ",
                    'throws': "Throw #{0}: {1} {2}"
                    'farewell': "So, good luck! "
                    }
        
    def Dices(self):
        (a, c, m) = (48271, 0, 6)
        t = math.ceil(float(time.monotonic()))
        yield (a * t + c) % m

    def main(self, invite='greet'): 
        q = input(self.msg.get(invite))
        if q == 'n': 
            print(self.msg.get('farewell'))
        elif q == 'y': 
            self.game_run()

    def game_run(self): 
        i = 1
        target = self.Dices()
        print(self.msg.get('throws').format(i, target[0], target[1]))


game = Game(3)
game.game_run()