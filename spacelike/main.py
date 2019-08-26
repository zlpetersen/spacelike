import random
import utilities
import generator

class TextHandler():
    def __init__(self):
        pass

if __name__ == '__main__':
    gen = generator.Generator(random.seed)
    for i in range(10):
        player = gen.generate_player()
        print(player.get_info())