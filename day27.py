# simple quiz game in python.

questions = ['What is the sum of 100 + 20 \n', 'Which one is wild animal ?\n', 'What is the capital city of Nepal ?']
options = [' A.120\n B.110\n C.130\n D.140', ' A.Lion\n B.Cow\n C.Dog\n D.Cat', ' A.Biratnagar\n B.Bhaktapur\n C.Kathmandu\n D.Pokhara']
answers = ['A', 'A', 'C']
correctAnswer =[120, 'Lion', 'Kathmandu']

print("Welcome to kuin banaga crorepatti\n")
for i in range(len(questions)):
    print(questions[i])
    print(options[i], '\n')
    userAnswer = input("Answer : ")
    if userAnswer.title() == answers[i]:
        print("Correct answer, you won", (i+1)*200000)
    else:
        print("Wrong answer, Your correct answer is", correctAnswer[i], "and you won Rs.", i*200000)
        break


