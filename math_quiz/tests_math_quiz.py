import unittest
from math_quiz import generate_random_integer, choose_random_operation, calculation_function


class TestMathGame(unittest.TestCase):

    def test_function_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_choose_random_operation(self):
        # Test if the random chosen arithematic operation is from the list of operations that are allowed in the maths quiz
        allowed_operations = ['+', '-', '*']
        random_chosen_operation = choose_random_operation()
        self.assertIn(random_chosen_operation,allowed_operations)


    def test_function_calculation_function(self):
            
            # Test if the calculation function is correctly applying the chosen arithmetic operation or not.
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (101, 78, '*', '101 * 78', 7878),
                (9, 3, '-', '9 - 3', 6),
                (5, 3, '*', '7 * 3', 15)]
            

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                with self.subTest(num1=num1, num2=num2, operator=operator, expected_problem=expected_problem, expected_answer=expected_answer):
                    result = calculation_function(num1, num2, operator)
                    self.assertEqual(result[1], expected_answer)
                

if __name__ == "__main__":
    unittest.main()
