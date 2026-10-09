# @title
print("Welcome to KBC".center(50))
print("RULES: ")
print("1. Each question carries Rs.1000.\n2. There are 5 questions.\n3. If you answer all correctly, you'll win Rs.5000.\n4. If your answer is incorrect, you won't loose money, the amount will remain the same as you scored.\n ".center(40))
print("LET'S START!!".center(50))

qa=[["Who is the PM of India?","a. Narendra Modi","b. Amit Shah","c. Draupadi Murmu","d. Jawaharlal Nehru",1],
    ["Who is the President of India?","a. Narendra Modi","b. Amit Shah","c. Draupadi Murmu","d. Jawaharlal Nehru",3],
    ["Who was Nirmal(NimsDai) Purja?","a. Mountaineer","b. Soldier","c. Professor","d.Runner",1],
    ["Where is Broad Peak located?","a. Karakoram","b. Pakistan","c. Border between Nepal and China","d. Himalayas",1],
    ["What is a type of IPR?","a. Trademark","b. Copyright","c. Patent","d. All",4]]

amount=0
for i in range(0, len(qa)):
  question=qa[i]
  print(f"Question {i+1}: {question[0]}")
  print(f" {question[1]}   {question[2]}\n {question[3]}  {question[4]}")
  ans=int(input("Enter answer(1-4): "))
  if (ans==question[-1]):
    amount += 1000
    print(("Correct Answer!".center(50)))
    print(f"You Won:{amount}".center(50))
  else:
    print("Wrong Answer...Game Over".center(50))
    print(f"Total amount won: {amount}".center(50))
    break
print("Thank You for Playing".center(50))