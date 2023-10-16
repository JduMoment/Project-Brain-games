#!/usr/bin/env python3
from brain_games.games import prime_game
from brain_games.games_core import play


def main():
    play(prime_game.generate_question_and_answer)


if __name__ == '__main__':
    main()
