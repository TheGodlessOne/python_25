import time, math

class Game:
    def __init__(self, lvl): 
        self.msg = {
                    'greet': "Hello, my fellow friend! Do you throw the dices? y/n ",
                    'quest': "Excellent!",
                    'throws': "Throw #{0}: {1} {2}",
                    'restart': "Do you want to play more? y/n ",
                    'farewell': "So, good luck! "
                    }
        
    def Dices(self, a=48271, c=0, m=31): 
        t = [math.ceil(float(time.monotonic()))]
        for i in range(55):
            t.append(int((a*t[i] + c) % (math.pow(2, m)-1)))
        print(t)
        t.append(int((t[len(t)-55]+t[len(t)-24]) % math.pow(2, m)))
        print(t)
        return t

    def main(self, invite='greet'): 
        q = input(self.msg.get(invite))
        if q == 'n': 
            print(self.msg.get('farewell'))
        elif q == 'y': 
            self.game_run()

    def game_run(self): 
        print(self.msg.get('quest'))
        i = 1
        target = self.Dices()
        print(self.msg.get('throws').format(i, target.next(), target.next()))
        i = i + 1
        self.main('restart')

game = Game(3)
game.Dices()