# Ray McMillin, Random Dice Code, 2/28/25
def randDice():
    
    return random.randint(1, 6) + random.randint(1, 6)

if __name__ == "__main__":
    total = 0
    rolls = 100
    
    for _ in range(rolls):
        total += randDice()
    
    average = round(total / rolls, 2)
    print(f"Average roll value over 100 dice rolls: {average}")
