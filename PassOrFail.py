a=list(input("Enter your Marks in 3 subjects separated by comma: ").split(","))
if int(a[0])>=33 and int(a[1])>=33 and int(a[2])>=33 and sum(map(int,a))/3>=40:
    print("Congratulations! You have Passed the Exam")
else:
    print("Sorry! You have Failed the Exam")