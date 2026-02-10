score = 0

print("Welcome to MCQ Quiz App")
print("-----------------------")

for i in range(20):

    if i == 0:
        print("1. What is 5 + 3?")
        print("a) 6  b) 7  c) 8  d) 9")
        if input("Enter answer: ") == 'c':
            score += 1
        else:
            score -= 1

    elif i == 1:
        print("2. Which operator is used for comparison?")
        print("a) =  b) ==  c) +  d) *")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1

    elif i == 2:
        print("3. Which data operator is used for addition?")
        print("a) -  b) *  c) +  d) /")
        if input("Enter answer: ") == 'c':
            score += 1
        else:
            score -= 1

    elif i == 3:
        print("4. Which loop repeats a block of code?")
        print("a) if  b) for  c) break  d) return")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1

    elif i == 4:
        print("5. What is the output of print(2*3)?")
        print("a) 5  b) 6  c) 23  d) Error")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1

    elif i == 5:
        print("6. Which keyword is used to define a function?")
        print("a) fun  b) def  c) function  d) define")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1

    elif i == 6:
        print("7. Which data type stores True or False?")
        print("a) int  b) float  c) bool  d) str")
        if input("Enter answer: ") == 'c':
            score += 1
        else:
            score -= 1

    elif i == 7:
        print("8. What is the output of print(10//3)?")
        print("a) 3.33  b) 3  c) 4  d) Error")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1

    elif i == 8:
        print("9. Which symbol is used for comments?")
        print("a) //  b) <!-- -->  c) #  d) /* */")
        if input("Enter answer: ") == 'c':
            score += 1
        else:
            score -= 1

    elif i == 9:
        print("10. Which function takes input from user?")
        print("a) get()  b) scan()  c) input()  d) read()")
        if input("Enter answer: ") == 'c':
            score += 1
        else:
            score -= 1

    elif i == 10:
        print("11. Which keyword is used to stop a loop?")
        print("a) stop  b) end  c) break  d) exit")
        if input("Enter answer: ") == 'c':
            score += 1
        else:
            score -= 1

    elif i == 11:
        print("12. What is the output of print(type(5))?")
        print("a) int  b) <class 'int'>  c) number  d) error")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1
            
    elif i == 12:
        print("13. Which loop runs a fixed number of times?")
        print("a) while  b) for  c) if  d) break")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1

    elif i == 13:
        print("14. What is the output of print(5 % 2)?")
        print("a) 2  b) 1  c) 0  d) 3")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1

    elif i == 14:
        print("15. Which keyword is used for decision making?")
        print("a) for  b) if  c) loop  d) def")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1

    elif i == 15:
        print("16. Which data type stores text?")
        print("a) int  b) bool  c) str  d) float")
        if input("Enter answer: ") == 'c':
            score += 1
        else:
            score -= 1

    elif i == 16:
        print("17. What is the output of print(3**2)?")
        print("a) 6  b) 9  c) 8  d) 12")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1

    elif i == 17:
        print("18. Which operator checks equality?")
        print("a) =  b) ==  c) !=  d) >")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1

    elif i == 18:
        print("19. Which keyword is used to exit function?")
        print("a) break  b) exit  c) return  d) stop")
        if input("Enter answer: ") == 'c':
            score += 1
        else:
            score -= 1

    elif i == 19:
        print("20. What is the output of print(len('Python'))?")
        print("a) 5  b) 6  c) 7  d) Error")
        if input("Enter answer: ") == 'b':
            score += 1
        else:
            score -= 1

print("-----------------------")
print("Quiz Completed ")
print("Your Score:", score, "/ 20")
