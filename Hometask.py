# 1)
# import random
# a = random.randint(1, 100)
# l = 5
# print(f"You have {l} l")
# while l > 0:
#     c = input("Enter your guess: ")
#     if c.isdigit():
#         b = int(c)
#     else:
#         print("Please enter a valid number.")
#         continue 
#     if b == a:
#         print("You Win!!!")
#         break
#     elif abs(b - a) <= 2:
#         print("Too closer")
#     elif b > a:
#         print("Too high")
#     elif b < a:
#         print("Too low")
    
#     l -= 1
#     print(f"Lives remaining: {l}")
#     if l == 0:
#         print("Game Over!!!")
#         print(f"The correct number was {a}")


# 2)
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = a == b
# print("First array:\n", a)
# print("Second array:\n", b)
# print("Are the two arrays equal?\n", c)


# 3)
# import random, string
# a = int(input())
# b = string.ascii_letters + string.digits + string.punctuation
# if a > len(b):
#     print()
# else:
#     password = ''.join(random.sample(b, a))
#     print(password)



# 4)
# import random
# a = ["Rock", "Paper", "Scissors"]
# b = int(input("Select your move (1 for Rock, 2 for Paper, 3 for Scissors): ")) - 1
# if b not in [0, 1, 2]:
#     print("Invalid input. Please select 1, 2, or 3.")
# else:
#     c = random.choice([0, 1, 2])
#     print(f"Your choice: {a[b]}")
#     print(f"Computer chose: {a[c]}")
#     if b == c:
#         print("It's a tie!")
#     elif (b == 0 and c == 2) or \
#          (b == 1 and c == 0) or \
#          (b == 2 and c == 1):
#         print("You win!")
#     else:
#         print("You lose!")


