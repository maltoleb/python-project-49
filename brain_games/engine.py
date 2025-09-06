from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def run_game(game):

    name = welcome_user()
    print(game.RULES)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.generate_question()
        print(question)
        user_answer = input('Your answer: ')
        if game.check_answer(user_answer, correct_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')