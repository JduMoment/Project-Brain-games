#!/usr/bin/env python3
from brain_games.games import calc_game
from brain_games.games_core import play


def main():
    play(calc_game.generate_question_and_answer)


if __name__ == '__main__':
    main()
