def average(score1, score2, score3):
    try:
        if score1 < 0:
            raise ValueError
    except ValueError:
        print("You did not enter a positive number")
    NUMBER_TESTS = 3
    averageScore = float((score1 + score2 + score3) / NUMBER_TESTS)
    return float((score1 + score2 + score3) / NUMBER_TESTS)


def run_average():
    score1 = int(input("Enter the first score "))
    try:
        if score1 < 0:
            raise ValueError
    except ValueError:
        score1 = int(input("You did not enter a positive number, please try again "))
    score2 = int(input("Enter the first score "))
    try:
        if score2 < 0:
            raise ValueError
    except ValueError:
        score2 = int(input("You did not enter a positive number, please try again "))
    score3 = int(input("Enter the first score "))
    try:
        if score3 < 0:
            raise ValueError
    except ValueError:
        score3 = int(input("You did not enter a positive number, please try again "))

    avgScore = average(score1, score2, score3)
    print(avgScore)


if __name__ == '__main__':
    run_average()
