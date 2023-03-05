#!/usr/bin/python3
import secrets

def play():
    
    print("             !WELCOMEEE!          ")
    print("      Enter rock, paper, scissors")
    prompt = input("$")

    user = ['piedra, papel , tijera']
    computer = secrets.choice(user)

    if prompt == computer:
        print("the same")
    
    if case(prompt,computer):
        return 'You won!'
    return 'You lost!'
    
def case(player,opponet):
    if (player == 'piedra' and opponet == 'tijera') or (player == 'tijera' and opponet == 'papel') \
    or (player == 'papel' and opponet == 'piedra'):
        return True

print(play())
