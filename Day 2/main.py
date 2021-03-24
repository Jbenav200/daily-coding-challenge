from challenge2 import ChallengeTwo
import random


def main():
    # Given Test Data
    arr1 = [1, 2, 3, 4, 5]

    # Random test data
    arr2 = []

    # For each value in arr1, assign a new random value between 1 and 14
    # and add it to the end of arr2
    for x in arr1:
        x = random.randint(1, 14)
        arr2.append(x)

    # Instantiate the ChallengeTwo Class
    challenge_two = ChallengeTwo()

    # Compile both arrays in a single array to couple up the results
    arr3 = [arr1, arr2]
    # For each array in arr3, return the result of product_except_self method
    # in the ChallengeTwo class
    for x in arr3:
        res = challenge_two.product_except_self(x)
        # Print the result to the terminal.
        print(f'\nthe result of passing {x} is: {res}\n')


# This method is what causes the main method to run
if __name__ == "__main__":
    main()
