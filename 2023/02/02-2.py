import re
import functools


class Game:

    def __init__(self, game_string):
        self.game_sets = []
        self.min_cubes = {"red": 0, "green": 0, "blue": 0}
        game_sets = game_string.split("; ")
        for gs in game_sets:
            cube_counts = gs.split(", ")
            for c in cube_counts:
                count, color = c.split(" ")
                self.min_cubes[color] = max(self.min_cubes[color], int(count))
        self.power = functools.reduce(
            lambda a, b: a * b, self.min_cubes.values())


def main():
    game_id = 1
    sum = 0
    with open("2023/02/input.txt") as file:
        for line in file:
            game_string = re.search("(?<=: )\\d.*", line).group()
            game = Game(game_string)
            print(game_id, game.min_cubes, game.power)
            sum = sum + game.power
            game_id = game_id + 1
    print(sum)


main()
