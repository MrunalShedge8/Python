# Create a list of ten numbers and print the sum of last four elements of the list
numbers = [35, 23, 15, 20, 25, 30, 5, 4, 6, 10]
print(sum(numbers[-4:]))
# OR
sum=0
for i in range(len(numbers)-4, len(numbers)):
    sum=sum + numbers[i]
print(sum)


# Find out the difference between maximum and minimum element of the list
print(max(numbers) - min(numbers))


# Insert a number in the list at 6th postion, this number must be one third of number stored at 4th postion.
numbers.insert(5, numbers[3] / 3)
print(numbers)

# Write a program to guess a number between 1 to 9. If the user guesses the correct number, give a reward.
import random
target = random.randint(1, 9)
guess = int(input("Guess a number between 1 and 9: "))
if guess == target:
    print("You won 100 points!")
else:
    print("Try again")