import random 

name = input("What is your name?")
question = input("What is your question?")
# question = "Is there an afterlife?"
answer = ""

random_number = random.randint(1, 9)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "It is decidedly so"
elif random_number == 5:
  answer = "Reply hazy, try again"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

print(f"{name} asks: {question}")
print(f"Magic 8-Ball's answer: {answer}")
