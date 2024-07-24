import time

def typing_speed_test():
    # Text for typing test
    text = "The quick brown fox jumps over the lazy dog."

    print("Type the following text:")
    print(text)
    
    input("Press Enter when you are ready to start typing.")
    
    start_time = time.time()
    
    # User types the text
    user_input = input("Type here: ")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Calculate words per minute (WPM)
    words_per_minute = (len(text.split()) / elapsed_time) * 60
    
    # Check the accuracy of typing
    correct_words = sum(1 for a, b in zip(text.split(), user_input.split()) if a == b)
    accuracy = (correct_words / len(text.split())) * 100
    
    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {words_per_minute:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_speed_test()
