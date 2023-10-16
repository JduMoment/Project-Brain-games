#!/usr/bin/env python3
from brain_games.games import gcd_game
from brain_games.games_core import play


def main():
    play(gcd_game.generate_question_and_answer)


if __name__ == '__main__':
    main()
