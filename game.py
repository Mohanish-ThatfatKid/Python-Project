import random
answer_List = ["green", "cry", "hot", "number", "orange", "python", "project", "lesson", "home"]
chance = 5
temp = 1
inde = 0
score = 0
game_List = []

def create_game_list():
    tempitem = answer_List[random.randint(0, len(answer_List)-1)]
    if tempitem not in game_List:
        game_List.append(tempitem)
    while len(game_List) < 5:
        create_game_list()


create_game_list()
print("Welcome to this game you will get 5 chances to guess the word correctly(Score 3 or more to win)")
def randomizer(i):
    while i < len(game_List):
        k = [j for j in game_List[i]]
        i += 1
        return k


while temp <= chance:
    print("Arrange the letters to form a valid word:")
    s = randomizer(inde)
    random.shuffle(s)
    if s == game_List[inde]:
        random.shuffle(s)
    else:
        print("".join(s))
        ans = input()
        if ans == game_List[inde]:
            score += 1
        else:
            score -= 1
    temp += 1
    inde += 1
if score >= 3:
    print("Your Score is: ", score, " You Won the game.")
else:
    print("Your Score is: ", score, "You lost")
