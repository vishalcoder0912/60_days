marks =input("enter your makrs:");
if not marks.isdigit():
    print("Enter a Valid number ")
else:
    marks =int(marks);
    
    if marks <0 or marks >100:
        print("Marks should be between 0 and 100")
    else :
        if marks >=90:
            grade="A"
        elif marks >=75:
            grade="B"
        elif marks >=50:
            grade ="C"
        else:
            grade="Fail"

        if marks >=50:
            status="pass"
        else:
            status="fail"

print(f"Marks :{marks}")
print(f"Grade :{grade}")
print(f"Status :{status}")