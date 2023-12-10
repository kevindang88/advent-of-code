import re
import functools


class GameSet:

    def __init__(self, game_set_string):
        self.cube_counts = {"red": 0, "green": 0, "blue": 0}
        cube_count_strings = game_set_string.split(", ")
        for s in cube_count_strings:
            count, color = s.split(" ")
            self.cube_counts[color] = int(count)

    def is_valid(self):
        return self.cube_counts["red"] <= 12 \
            and self.cube_counts["green"] <= 13 \
            and self.cube_counts["blue"] <= 14


class Game:

    def __init__(self, game_string):
        self.game_sets = []
        game_set_strings = game_string.split("; ")
        self.game_sets = list(map(GameSet, game_set_strings))

    def is_valid(self):
        bools = list(map(lambda gs: gs.is_valid(), self.game_sets))
        return functools.reduce(lambda a, b: a and b, bools)


def main():
    game_id = 1
    sum = 0
    with open("2023/02/input.txt") as file:
        for line in file:
            game_string = re.search("(?<=: )\\d.*", line).group()
            game = Game(game_string)
            if (game.is_valid()):
                sum = sum + game_id
            game_id = game_id + 1
    print(sum)


main()
