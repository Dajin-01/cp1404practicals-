
MENU = ("Menu:\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")


def determine_score_result(score):
    # Determine the result based on the score
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    # Get a valid score (between 0 and 100 inclusive)
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def show_stars(score):
    # Print stars equal to the score
    print('*' * int(score))


def main():
    print(MENU)

    choice = input("Choose an option: ").upper()

    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_score_result(score)
            print(f"The result for the score {score} is: {result}")
        elif choice == 'S':
            show_stars(score)
        else:
            print("Invalid option. Please choose again.")

        choice = input("Choose an option: ").upper()


    print("Goodbye!")


main()
