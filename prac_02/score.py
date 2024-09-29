import random


def determine_score_result(score):
    # Function to determine the result based on the score
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    # Get the score from the user
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(result)

    # Generate a random score and print the result
    random_score = random.randint(0, 100)
    random_result = determine_score_result(random_score)
    print(f"Random score: {random_score}, Result: {random_result}")


main()

