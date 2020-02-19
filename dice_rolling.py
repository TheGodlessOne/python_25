import time, math

class Game:
    def __init__(self, lvl): 
        self.msg = {
                    'greet': "Hello, my fellow friend! Do you throw the dices? y/n ",
                    'quest': "Excellent!",
                    'throws': "Throw #{0}: {1}",
                    'restart': "Do you want to play more? y/n ",
                    'farewell': "So, good luck! "
                    }
        self.num_of_games = 0
        
    def Dices(self, a=48271, c=0, m=31): 
        seq = [math.ceil(float(time.monotonic()))]
        for i in range(2):
            dice = int((a*seq[i] + c) % (math.pow(2,m) - 1))
            seq.append(dice)
            yield (dice % 6) + 1

    def main(self, invite='greet'): 
        q = input(self.msg.get(invite))
        if q == 'n': 
            print(self.msg.get('farewell'))
        elif q == 'y': 
            self.game_run()

    def game_run(self): 
        self.num_of_games = self.num_of_games + 1
        target = []
        print(self.msg.get('quest'))
        for dice in self.Dices():
            target.append(dice)
        print(self.msg.get('throws').format(self.num_of_games, target))
        self.main('restart')


game = Game(3)
game.main()
