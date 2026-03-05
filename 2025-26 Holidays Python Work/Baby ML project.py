happy = []
sad = []

with open("Happy.txt", "r") as file:
    for line in file:
        happy.append(line.strip())

with open("Sad.txt", "r") as f:
    for line in f:
        sad.append(line.strip())

user = input("Enter a sentence and I will detect if it is happy or sad! : ").lower()
user_words = user.split()

for word in user_words:
    if word in happy:
        print("I think this is a happy sentence!")
        correct = input("Did I get it right? (y/n): ")
        if correct == "n":
            word = input("what was the sad word : ").strip()
            sad.append(word)
            with open("Sad.txt", "a") as f:
                f.write(word + "\n")
    elif word in sad:
        print("I think this is a sad sentence!")
        correct = input("Did I get it right? (y/n): ")
        if correct == "n":
            word = input("what was the happy word : ").strip()
            happy.append(word)
            with open("Happy.txt", "a") as f:
                f.write(word + "\n")
    else:
        what_was_it = input("I'm not sure, what is it? (happy/sad): ").lower()
        if what_was_it == "happy":
            word = input("what was the happy word : ").strip()
            happy.append(word)
            with open("Happy.txt", "a") as f:
                f.write(word + "\n")
        else:
            word = input("what was the sad word : ").strip()
            sad.append(word)
            with open("Sad.txt", "a") as f:
                f.write(word + "\n")




