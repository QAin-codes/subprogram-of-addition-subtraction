#Quratul Ain
#July2022
#subprogram

print("*****welcome to add,sub numbers ****")
import random

def addition():
  num1=random.randint(5,20)
  num2=random.randint(5,20)
  print(num1,"+",num2,"=")
  user_answer=int(input("your answer: "))
  actual_answer=num1+num2
  answers=(user_answer,actual_answer)
  return answers

def subtraction():
  num3=random.randint(25,50)
  num4=random.randint(1,25)
  print(num3,"-",num4,"=" )
  user_answer=int(input("your answer: "))
  actual_answer=num3-num4
  answers=(actual_answer,user_answer)
  return answers
  
def check_answer(user_answer,actual_answer):
   if user_answer==actual_answer:
     print("correct")
   else:
     print("incorrect,the answer is",actual_answer)

def main():
  print("1) addition")
  print("2) subtraction")
  selection=int(input("enter 1 or 2 :"))
  if selection==1:
    user_answer,actual_answer=addition()
    check_answer(user_answer,actual_answer)
    
  elif selection==2:
    user_answer,actual_answer=subtraction()
    check_answer(user_answer,actual_answer)
  else:
    print("incorrect selection")
main()

    
     
  
  