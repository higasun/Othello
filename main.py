from model import Game

def main():
    game = Game()
    game.show()
    while True:
        x, y = map(int, input("{}'s Turn: ".format(game.player.disk)).split())
        game.place(x, y)
        game.show()

if __name__ == '__main__':
    main()