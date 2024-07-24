'''Program for testing speed tester application'''
import time
from lorem_text import lorem

def generate_random_text(words):
    return lorem.words(words)

def typing_speed_test():
    words_count = 50  # You can adjust the number of words in the random text
    random_text = generate_random_text(words_count)

    print("Type the following random text:")
    print(random_text)

    input("Press Enter when you are ready to start typing.")

    start_time = time.time()

    # User types the text
    user_input = input("Type here: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Calculate words per minute (WPM)
    words_per_minute = (words_count / elapsed_time) * 60

    # Check the accuracy of typing
    correct_words = sum(1 for a, b in zip(random_text.split(), user_input.split()) if a == b)
    accuracy = (correct_words / words_count) * 100

    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {words_per_minute:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()
