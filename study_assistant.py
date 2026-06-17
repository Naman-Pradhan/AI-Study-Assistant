print("=== AI Study Assistant ===")

topic = input("Enter a topic: ")

print("\nStudy Plan for:", topic)

days = [
    "Learn the basics",
    "Practice examples",
    "Solve problems",
    "Revise concepts",
    "Take a mini test"
]

for i in range(len(days)):
    print(f"Day {i+1}: {days[i]}")

print("\nPractice Questions:")
print(f"1. What is {topic}?")
print(f"2. Why is {topic} important?")
print(f"3. Explain real-world applications of {topic}")