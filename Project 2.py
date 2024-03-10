def password():
    passkey = input()
    # count_uppercase,lowercase,digit,character,no of letter,sequence of password, same letters
    count,upper_count,lower_count,digit_count,char_count,seq_count,same_count=0,0,0,0,0,0,0

    for i in passkey:
       count=count+1
       if i.isupper()==True:
           upper_count=upper_count+1
       elif i.islower()==True:
           lower_count=lower_count+1
       elif i.isdigit()==True:
           digit_count=digit_count+1
       elif (ord(i)>=33 and ord(i)<=47) or (ord(i)>=58 and ord(i)<=64) or (ord(i)>=91 and ord(i)<=96) or (ord(i)>=123 and ord(i)<=126):
           char_count=char_count+1 

    if count<10:
        print("The password should contain contain at least ten letters.\nPlease re-enter the password.")
        password()
    elif upper_count<2 :
        print("The password should contain at least two uppercase letters.\nPlease re-enter the password.")
        password()
    elif lower_count<2:    
        print("The password should contain at least two lowercase letters.\nPlease re-enter the password.")
        password()
    elif digit_count<2:
        print("The password should contain at least two digits.\nPlease re-enter the password.")
        password()
    elif char_count<2:
        print("The password should contain at least two special cjaracters.\nPlease re-enter the password.")
        password()

    for i in range(len(passkey)-2):
        if passkey[i]==passkey[i+1] and passkey[i+1]==passkey[i+2] and passkey[i+2]==passkey[i+3]:
            print("The password should not contain more than three same letters consecutively.\nPlease re-enter the password.")
            password()

    if passkey == previous[0] or passkey == previous[1] or passkey == previous[2] :
        print("The password matches the previously set password.\nPlease re-enter the password.")
        password()

    flag=1
    for i in range(len(username)-2):
        verifier = username[i]+username[i+1]+username[i+2]
        for j in range(len(passkey)-2):
            if(passkey[j]==verifier[0] and passkey[j+1]==verifier[1] and passkey[j+2]==verifier[2]):
                flag = 0
                break
        if(flag==0):
            break

    if(flag==1):
        print("Password Verified Successfully!!!")
    else:
        print("The password contains the sequence of three or more consecutive characters from the username.\nPlease re-enter the password.",verifier)
        password()

    
    

# Criterias
print("Hi, Welcome to the Password Generator!\nYour password should match the following criterias:\n(1) It must be atleast 10 characters long.\n(2) It must contain at least 2 uppercase letters\n(3) It must contain at least 2 lowercase letters\n(4) It must contain at least 2 special characters\n(5) It shoul not contain any sequence of three or more consecutive letters from the username.\n(6) No character should repeat more than three times in row.\n(7) The new password must not be the same as the previous three passwords.")
# Obtaining username
username=input("Enter the Username : ")
# Obtaining prevoius passwords
previous=[]
a=input("Enter last password: ")
previous.append(a)
b=input("Enter second last password: ")
previous.append(b)
c=input("Enter third last password: ")
previous.append(c)
#Obtaining password
print("Enter the password: ")
password()