import guessing_game
import unittest


class TestGame(unittest.TestCase):
    def test_input_OK(self):
        answer = 5
        guess = 5
        result = guessing_game.run_guess(answer, guess)
        self.assertTrue(result)

    def test_input_NOK_guess(self):
        answer = 5
        guess = 0
        result = guessing_game.run_guess(answer, guess)
        self.assertFalse(result)

    def test_input_NOK_number(self):
        answer = 5
        guess = 11
        result = guessing_game.run_guess(answer, guess)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
