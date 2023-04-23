"""
Final Project: Guess the Number Game Test File 
===========================
Student:  Theresa Fu-Hsing Hsu
Semester: Spring 2023
Course: CS 5001
"""

import unittest
from unittest.mock import patch
import guess_the_number_game


class TestGuessTheNumberGame(unittest.TestCase):
    
    def setUp(self):
        self.hints = []
    
    def test_main(self):
        # Test a correct guess on the first try
        with patch('builtins.input', return_value='42'):
            with patch('builtins.print') as mock_print:
                guess_the_number_game.main()
                mock_print.assert_called_with("Congratulations! You guessed the number in 1 tries.")
        
        # Test a correct guess on the last try
        with patch('builtins.input', side_effect=['50']*9 + ['42']):
            with patch('builtins.print') as mock_print:
                guess_the_number_game.main()
                mock_print.assert_called_with("Congratulations! You guessed the number in 10 tries.")
        
        # Test an out of range guess
        with patch('builtins.input', side_effect=['0', '101', '42']):
            with patch('builtins.print') as mock_print:
                guess_the_number_game.main()
                mock_print.assert_called_with("Your guess is out of range. Please enter a number between 1 and 100.")
        
        # Test a too low guess with a hint
        with patch('builtins.input', side_effect=['30', '20', '25']):
            with patch('builtins.print') as mock_print:
                guess_the_number_game.main()
                self.assertIn("Hint: The number is between 25 and 100.", [c[0][0] for c in mock_print.call_args_list])
        
        # Test a too high guess with a hint
        with patch('builtins.input', side_effect=['70', '80', '75']):
            with patch('builtins.print') as mock_print:
                guess_the_number_game.main()
                self.assertIn("Hint: The number is between 1 and 75.", [c[0][0] for c in mock_print.call_args_list])
        
        # Test running out of tries
        with patch('builtins.input', side_effect=['50']*10):
            with patch('builtins.print') as mock_print:
                guess_the_number_game.main()
                mock_print.assert_called_with("Sorry, you ran out of tries. The number was 50.")
    
    def test_computer_plays(self):
        # Test a correct guess on the first try
        with patch('guess_the_number_game.random.randint', return_value=42):
            with patch('builtins.print') as mock_print:
                guess_the_number_game.computer_plays()
                mock_print.assert_called_with("The computer guessed the number in 1 tries.")
        
        # Test a correct guess on the last try
        with patch('guess_the_number_game.random.randint', return_value=42):
            with patch('builtins.print') as mock_print:
                guess_the_number_game.computer_plays()
                mock_print.assert_called_with("The computer guessed the number in 7 tries.")
        
        # Test a too low guess with a hint
        with patch('guess_the_number_game.random.randint', return_value=75):
            with patch('builtins.print') as mock_print:
                guess_the_number_game.computer_plays()
                self.assertIn("Hint: The number is between 76 and 100.", [c[0][0] for c in mock_print.call_args_list])
        
        # Test a too high guess with a hint
        with patch('guess_the_number_game.random.randint', return_value=25):
            with patch('builtins.print') as mock_print:
                guess_the_number_game.computer_plays()
