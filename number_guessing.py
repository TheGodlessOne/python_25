import time, math

class Game:
    def __init__(self, lvl): 
        self.msg = {
                    'greet': "Hello, my fellow friend! Do you want to play a Game of Numbers? y/n ",
                    'quest': "Excellent! I made up a number from {0} to {1}. Try to guess it in {2} attempts! ",
                    'win': "Yes! Exactly! ", 
                    'wrong': "Oh, no! But you have the {0} chances! ", 
                    'lose': "Sorry, my dear, this was you're last try... The number was {0}", 
                    'restart': "Do you want to play more? y/n ",
                    'error': "Can't understand you, dear. Try again! ",
                    'farewell': "So, good luck! "
                    }
        self.min = 0
        self.max = 100
        self.lvl = 3

    def Random_Number(self):
        (a, c, m) = (48271, 0, 100)
        t = math.ceil(float(time.monotonic()))
        print(t)
        t = (a * t + c) % m
        return t

    def main(self, invite='greet'): 
        q = input(self.msg.get(invite))
        if q == 'n': 
            print(self.msg.get('farewell'))
        elif q == 'y': 
            self.game_run()

    def game_run(self): 
        target = int(self.Random_Number())
        print(self.msg.get('quest').format(self.min, self.max, self.lvl))
        i = 0
        print("test: ", target)
        while i < self.lvl:
            a = int(input())
            i = i+1
            if int(a) == target: 
                print(self.msg.get('win'))
                self.main('restart')
                break
            elif i - self.lvl != 0: 
                print(self.msg.get('wrong').format(self.lvl-i))
            else: 
                print(self.msg.get('lose').format(target))
                self.main('restart')


game = Game(3)
game.game_run()
