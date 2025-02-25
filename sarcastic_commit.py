import random
import argparse
import datetime
from messages import COMMIT_MESSAGES

def generate_commit(mood=None):
    # return message by mood
    if mood and mood in COMMIT_MESSAGES:
        return random.choice(COMMIT_MESSAGES[mood])
    else:
        # return random message
        all_messages = sum(COMMIT_MESSAGES.values(), [])
        return random.choice(all_messages)


# def get_time_based_message():
#     now = datetime.datetime.now()
#     hour = now.hour

#     if 0 <= hour < 4:
#         return "Committed this at {} AM. Future me, good luck understanding what I did here".format(hour)
#     elif 4 <= hour < 9:
#         return "Coding before sunrise? Hope this wasn’t a mistake."
#     elif 9 <= hour < 17:
#         return "Regular work hours. Boring commit message expected."
#     elif 17 <= hour < 22:
#         return "Evening commit. Maybe I should take a break?"
#     else:
#         return "Late-night commit. Sleep is overrated anyway."


def main():
    parser = argparse.ArgumentParser(description="Sarcastic Commit Generator")
    parser.add_argument("command", choices=["generate"], help="generate random sarcastic message")
    parser.add_argument("--mood", choices=COMMIT_MESSAGES.keys(), help="choose a mood")
    args = parser.parse_args()

    if args.command == "generate":
        print(generate_commit(args.mood))

if __name__ == "__main__":
    main()
