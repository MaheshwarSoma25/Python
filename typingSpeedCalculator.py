from time import *
import random as r

def mistake(paratest, usertest):
    error = 0
    for i in range(min(len(paratest), len(usertest))):
        if paratest[i] != usertest[i]:
            error += 1
    error += abs(len(paratest) - len(usertest))
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    if time_delay == 0: 
        return 0
    speed = len(userinput) / time_delay
    return round(speed)

if __name__ == "__main__":

    test = [
        "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
        "Life is not a race everyone grows in their own time with their own journey.",
        "Consistency beats talent when talent does not work hard enough.",
        "Success is the result of continuous effort and not a one day miracle.",
        "Discipline is more powerful than motivation because it keeps you moving every day.",
        "Technology is evolving quickly and learning continuously keeps us ahead.",
        "Never compare your life with others everyone is fighting battles you cannot see.",
        "Small progress every day adds up to big results over time.",
        "In this digital world data has become more valuable than oil shaping the future of businesses.",
        "Failure is not the opposite of success it is a part of success that teaches us valuable lessons.",
        "Hard work gives success but smart work gives success faster which is why both are important.",
        "Your comfort zone may feel safe but nothing ever grows there take risks and explore more.",
        "Emotional intelligence helps you understand people and build better relationships.",
        "Opportunities do not happen you create them with dedication and effort.",
        "Time is the most valuable resource once wasted it never comes back.",
        "Dream big work hard stay humble and success will follow you naturally.",
        "Every expert was once a beginner practice consistency and patience always win.",
        "Believe in yourself even when nobody else does that is true confidence."
    ]

    while True:
        check = input("Ready to give test (Yes/No): ").strip().lower()

        if check in ["yes", "y"]:
            test1 = r.choice(test)
            print("\n***** Typing Speed *****")
            print(test1)
            print()
            time_1 = time()
            testinput = input("Enter: ")
            time_2 = time()

            print("\nSpeed:", speed_time(time_1, time_2, testinput), "chars/sec")
            print("Error:", mistake(test1, testinput))
            print("-----------------------------\n")

        elif check in ["no", "n"]:
            print("Thank You")
            break

        else:
            print("Wrong input. Please type Yes or No.\n")
