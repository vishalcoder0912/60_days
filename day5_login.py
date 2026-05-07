correct_username="admin"
correct_password="1234"

max_attempts=3

attempts=0

while attempts<max_attempts:
    username=input("enter username:")
    password=input("enter password:")

    if username==correct_username and password==correct_password:
        print("login successfull");
        break
    else:
        attempts+=1
        remaining_attempts=max_attempts-attempts

        print("invalid username or password");

        if remaining_attempts>0:
            print(f"you have {remaining_attempts} attempts left")

if attempts==max_attempts:
    print("account locked due to too many failed login attempts")