bn = int(input("Enter your Bangla Marks: "))
en = int(input("Enter your English Marks: "))
mt = int(input("Enter your Math Marks: "))
sc = int(input("Enter your Science Marks: "))
average = (bn + en + mt + sc)//4
grade = ''
if(average <= 40):
    grade = 'F'
elif(average > 40 and average <= 60):
    grade = 'D'
elif (average > 60 and average <= 70):
    grade = 'C'
elif (average > 70 and average <= 80):
    grade = 'B'
elif (average > 80 and average <= 90):
    grade = 'A'
else:
    grade = 'A+'
print("Your grade is " + grade)