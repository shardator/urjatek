from engine.game import Game

# Konstansok
WIDTH, HEIGHT = 800, 600
FPS = 60


def main():
    game = Game(WIDTH, HEIGHT, FPS)

    game.run()


if __name__ == "__main__":
    main()
