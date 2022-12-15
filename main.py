def cal():
  grade=int(input("What is your grade in that class?: "))

  if (grade >= 93):
    grade=4
    grad.append(grade)
  elif (grade >= 90 and grade < 93):
    grade=3.7
    grad.append(grade)
  elif (grade < 90 and grade >= 87):
    grade=3.3
    grad.append(grade)
  elif (grade < 87 and grade >= 83):
    grade=3
    grad.append(grade)
  elif (grade < 83 and grade >= 80):
    grade=2.7
    grad.append(grade)
  elif (grade < 80 and grade >= 77):
    grade=2.3
    grad.append(grade)
  elif (grade < 77 and grade >= 73):
    grade=2
    grad.append(grade)
  elif (grade < 73 and grade >= 70):
    grade=1.7
    grad.append(grade)
  elif (grade < 70 and grade >= 60):
    grade=1
    grad.append(grade)
  else:
    grade=0
    grad.append(grade)
  print("Your gpa for this class is ",grade)
  credit= int(input("How many credits is this class worth?: "))
  crd.append(credit)
  credit= credit*grade 
  cred.append(credit)

  
clna=[]
grad=[]
cred=[]
crd=[]
i=0
cls=int(input("How many classes do you have?: "))
while i<cls:
  cn=input("What is the class name?: ")
  if cn in clna:
    print('You entered this already')
    cn=input("What is the class name?: ")
    clna.append(cn)
  else:
    clna.append(cn)
  cal()
  i+=1
print("Your CGPA is ",(sum(cred)/sum(crd)))