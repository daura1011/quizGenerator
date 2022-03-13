#Name: Aliyu Abdullahi 
#Reg. No: H20CS095
#Title: Python Random Quiz Generator

while True:
    import time
    import random
    
    
    #variables declarations
    correct = int(0)
    count = int(0)
    totalQuestions = int(5)

    
    

   
    startTimer = time.time()

    print("\nThe Quiz Has Begin")

       
    while count<totalQuestions:
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        answer = int(input("What is "+str(num1)+ " Raised to the Power of "+str(num2)+" ?\n"))
        if(answer != pow(num1, num2)):
            print("You are wrong!, Correct answer is "+str(int(pow(num1, num2))))
        else:
            print("You are Correct!")
            correct+=1
        count+=1

    #Calculating total time taken for the Quiz 
    endTimer = time.time()
    totalTime = int(endTimer-startTimer)

    # Printing number of points received based on correct answers
    print("\n")
    print("*#"*30)
    print("The number of points received are "+str(correct)+" out of "+str(totalQuestions))
    print("The total time taken is "+str(totalTime)+" seconds.")
    
    # Asking user to retake or exit the program
    retake = input("Do you want to retake the quiz? Type Y/N\n")
    
    if(retake.upper()=="N"):
        print("Thanks for taking this quiz Good Bye...\n")
        break
    else:
        continue



        
    




