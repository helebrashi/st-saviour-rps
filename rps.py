import random
import time

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
import random
import time

# 🎮 Rock Paper Scissors - Styled Version 🎮

choices = ["rock", "paper", "scissors"]


def dramatic_text(text, delay=0.02):
    """Print text with a typing effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def countdown():
    """Dramatic countdown like the example."""
    dramatic_text("\n🪨 Rock...")
    time.sleep(0.4)
    dramatic_text("📄 Paper...")
    time.sleep(0.4)
    dramatic_text("✂️ Scissors...")
    time.sleep(0.4)
    dramatic_text("💥 SHOOT!\n")
    time.sleep(0.3)


def get_user_choice():
    """Get and validate user input."""
    while True:
        choice = input("👉 Enter (rock, paper, scissors): ").lower().strip()
        if choice in choices:
            return choice
        else:
            print("❌ Invalid input. Try again.")


def get_computer_choice():
    """Random computer choice."""
    return random.choice(choices)


def emoji(choice):
    """Return emoji for each choice."""
    if choice == "rock":
        return "🪨"
    elif choice == "paper":
        return "📄"
    else:
        return "✂️"


def decide_winner(user, computer):
    """Determine winner."""
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "win"
    else:
        return "lose"


def play_game():
    user_score = 0
    computer_score = 0
    rounds_played = 0

    dramatic_text("🎮 Welcome to Rock, Paper, Scissors!")
    dramatic_text("🏆 First to win 2 out of 3 rounds!\n")

    while user_score < 2 and computer_score < 2:
        rounds_played += 1
        print(f"\n🔹 Round {rounds_played}")

        user = get_user_choice()
        computer = get_computer_choice()

        countdown()

        print(f"🙋 You chose: {emoji(user)} {user}")
        print(f"🤖 Computer chose: {emoji(computer)} {computer}\n")

        result = decide_winner(user, computer)

        if result == "tie":
            print("⚖️ It's a tie!")
        elif result == "win":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        print(f"\n📊 Score: You {user_score} | Computer {computer_score}")

    # Final result
    print("\n" + "=" * 30)
    if user_score > computer_score:
        dramatic_text(f"🏆 Congratulations! You won {user_score}/3!")
    else:
        dramatic_text(f"💻 Game Over! Computer won {computer_score}/3!")
    print("=" * 30)


# Run the game
play_game()
