import random

def spin():
    symbols = ["🍒", "🍋", "🔔", "💎", "7️⃣"]
    return [random.choice(symbols) for _ in range(3)]

def main():
    balance = 10  # Starting balance
    while balance > 0:
        input("Press Enter to spin! 🎰")
        slots = spin()
        print(" | ".join(slots))
        
        if len(set(slots)) == 1:  # If all three symbols match
            print("🎉 JACKPOT! You win 5 points!")
            balance += 5
        else:
            print("❌ You lose 1 point.")
            balance -= 1
        
        print(f"Balance: {balance} points\n")
    
    print("Game over! 💀 You're out of points.")

main()