def average(score1, score2, score3):
    NUMBER_TESTS = 3
    averageScore = float((score1 + score2 + score3) / NUMBER_TESTS)
    print(averageScore)
    return float((score1 + score2 + score3) / NUMBER_TESTS)


def run_average():
    score1 = int(input("Enter the first score "))
    try:
        score1 > 0
    except:
        print("your value was less than 0")
        # score1  =  int(input("You did not enter a positive number, please try again "))
    score2 = int(input("Enter the second score "))
    score3 = int(input("Enter the third score "))
    avgScore = average(score1, score2, score3)
    print(avgScore)


if __name__ == '__main__':
    run_average()
