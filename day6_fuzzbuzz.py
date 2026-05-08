n=int(input("enter a number:"))

file =open("fuxxbuzz_output.txt","w")

for i in range(1,n+1):
    if i%3==0 and i%5==0:
        output ="fizzbuzz"
    elif i%3==0:
        output="fizz"
    elif i%5==0:
        output="buzz"
    else :
        output=str(i)

    print(output)
    file.write(output +"\n")



file.close()

print("output saved to fizzbuzz_output.txt")