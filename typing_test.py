import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Coding is a valuable skill for the future.",
    "Practice makes perfect, keep learning every day.",
    "Python is fun and easy to start with.",
]

print("\nWelcome to the Typing Speed Test!")
print("Type the following sentence as fast and accurately as you can:\n")

target = random.choice(sentences)
print("Sentence:")
print(target)
input("\nPress Enter when you're ready...\n")

start = time.time()
typed = input("Start typing here:\n")
end = time.time()

time_taken = end - start
words = len(target.split())
wpm = words / (time_taken / 60)

# accuracy calculation
correct = 0
for i in range(min(len(target), len(typed))):
    if target[i] == typed[i]:
        correct += 1

accuracy = correct / len(target) * 100

print("\n--- Results ---")
print(f"Time taken: {time_taken:.2f} seconds")
print(f"Words per minute (WPM): {wpm:.2f}")
print(f"Accuracy: {accuracy:.2f}%")
