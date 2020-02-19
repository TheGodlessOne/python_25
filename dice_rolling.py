import time, math

def test(game, iterations=50): 
    throw_list = []
    num_of_thrown = [0 for i in range(6)]
    #print(num_of_thrown)
    for i in range(iterations):
        for dice in game.Dices():
            throw = []
            #print(dice)
            throw.append(dice)
            num_of_thrown[dice-1] = num_of_thrown[dice-1] + 1
            #print(num_of_thrown)
        throw_list.append(throw)
    print("Statistics:")
    for i in range(6):
        print("{0} was thrown {1} times, probability: {2}%"
            .format(i+1, num_of_thrown[i], 100*num_of_thrown[i]/iterations))


class Game:
    def __init__(self, a=48271, c=0, m=31): 
        self.msg = {
                    'greet': "Hello, my fellow friend! Do you throw the dices? y/n ",
                    'quest': "Excellent!",
                    'throws': "Throw #{0}: {1}",
                    'restart': "Do you want to play more? y/n ",
                    'farewell': "So, good luck! "
                    }
        self.a = a
        self.c = c
        self.m = m
        self.num_of_games = 0
        self.seq = [math.ceil(float(time.monotonic()))]
        for i in range(55): 
            self.seq.append(int((self.a*self.seq[i] + self.c) % (math.pow(2,self.m) - 1)))
        
    def Dices(self): 
        dice = int((self.seq[len(self.seq)-55] + self.seq[len(self.seq)-24]) % math.pow(2,self.m))
        self.seq.append(dice)
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
            print(dice)
            target.append(dice)
        print(self.msg.get('throws').format(self.num_of_games, target))
        self.main('restart')


game = Game(3)
game.main()
#test(game, 10000)
