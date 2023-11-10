import random


def generate_random_integer(min, max):
    """
    Generates a random integer between a given range (between min-max values).
    """
    return random.randint(min, max)


def choose_random_operation():
    """
    Chooses an arithmetic operation at random from addition, subtraction and multiplication.
    """
    return random.choice(['+', '-', '*'])


def calculation_function(num1, num2, operation):
    """
    Executes an arithmetic operation based on the inputs entered and randomly chosen operation.
    """
    operation_string = f"{num1} {operation} {num2}"

    if operation == '+': 
        result = num1 + num2

    elif operation == '-': 
        result = num1 - num2

    else: 
        result = num1 * num2

    return operation_string, result

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):

        #generating random integers for num1 and num2 and choosing an arithmetic operation at random
        n1 = generate_random_integer(1, 10); n2 = generate_random_integer(1, 5); o = choose_random_operation()

        PROBLEM, ANSWER = calculation_function(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        
        #error handling in case of incorrect inputs from the user 
        try:
            useranswer = int(useranswer)

        except ValueError as e:
            print("You have entered an incorrect input (i.e float value or an alphabet), please input an integer number as your answer")
            print(f"Actual Error: {e}")
        
        else:

            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
