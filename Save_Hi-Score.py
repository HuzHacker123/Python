import random

def Game():
    print("Welcome to the Game!")
    print("Game is Starting...")
    global Score
    Score = random.randint(0, 1000)
    print(f"Your Score is: {Score}")
    return Score

def Save_Hi_Score(Score):
    try:
        with open("Hi-Score.txt", "r") as file:
            Hi_Score = int(file.read())
    except FileNotFoundError:
        Hi_Score = 0

    if Score > Hi_Score:
        print("Congratulations! You have a new High Score!")
        with open("Hi-Score.txt", "w") as file:
            file.write(str(Score))
    else:
        print(f"The High Score still remains: {Hi_Score}")
    return Hi_Score

Game()
Save_Hi_Score(Score)