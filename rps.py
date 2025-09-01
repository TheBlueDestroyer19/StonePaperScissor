import random

moves={0:2,1:0,2:1}
maping={0:"Rock", 1:"Paper",2:"Sissor"}
demaping={'r':0,'p':1,'s':2}

username=input("What is your name?\n")
print(f"\nHello {username}\nAre you ready to play????\n\nLessgo!!!!\n\n")

# adding a comment here 1
# adding a new comment

i,user_score,comp_score=1,0,0
while i<=5:
    user_move=input("Enter your move out of rock (r), paper (p) and scissor (s)\n")
    while user_move not in ['r','p','s']:
        print("Please enter a valid move!\n")
        user_move=input("Enter your move out of rock (r), paper (p), sissor (s)\n")

    comp_move=random.randint(0,2)
    user_move=demaping[user_move]
    print(f"Your choice: {maping[user_move]}\nComputer's move: {maping[comp_move]}\n")
    
    if comp_move!=user_move:
        if moves[user_move]==comp_move:
            user_score+=1;
            print(f"Great move! The computer chose {maping[comp_move]}\n")
        else:
            comp_score+=1
            print(f"Opps!! The computer chose {maping[comp_move]}\n")
    else:
        print(f"You both chose {maping[comp_move]}! It is a match!\n")
    i+=1

    print(f"Your Score: {user_score}")
    print(f"Computer's Score: {comp_score}")


width = 50  
print("\n"+"="*width)
print("Final Score".center(width))
print("="*width)

print(f"{username}'s Score:".ljust(width-len(str(user_score)))+f"{user_score}")
print(f"Computer's Score:".ljust(width-len(str(comp_score)))+f"{comp_score}")

print("="*width)

if user_score==comp_score:
    print("\nIt is a tie!")
elif user_score>comp_score:
    print(f"\nCongrats {username}!!! You won!!!")
else:
    print("\nOops!! Computer Won!! Better luck next time!")

