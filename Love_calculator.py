print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

name = name1+name2
true_count = 0
love_count = 0
for i in "true":
    a = name.count(i)
    true_count += a

for i in "love":
    b = name.count(i)
    love_count += b

score = str(true_count) + str(love_count)
final_score = int(score)

if final_score <= 0 or final_score >= 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif 40 <= final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
