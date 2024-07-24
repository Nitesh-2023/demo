import time
import random
import string

def generate_random_text(length):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for _ in range(length))

def typing_speed_test():
    text_length = 100  # You can adjust the length of the random text
    random_text = generate_random_text(text_length)

    print("Type the following random text:")
    print(random_text)

    input("Press Enter when you are ready to start typing.")

    start_time = time.time()

    # User types the text
    user_input = input("Type here: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Calculate words per minute (WPM)
    words_per_minute = (text_length / elapsed_time) * 60

    # Check the accuracy of typing
    correct_chars = sum(1 for a, b in zip(random_text, user_input) if a == b)
    accuracy = (correct_chars / text_length) * 100

    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {words_per_minute:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()
