import random
import argparse
from messages import COMMIT_MESSAGES

def generate_commit():
    # return random message
    return random.choice(COMMIT_MESSAGES)

def main():
    parser = argparse.ArgumentParser(description="Sarcastic Commit Generator")
    parser.add_argument("command", choices=["generate"], help="generate random sarcastic message")
    args = parser.parse_args()

    if args.command == "generate":
        print(generate_commit())

if __name__ == "__main__":
    main()
