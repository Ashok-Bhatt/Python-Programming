choice=int(input("Enter your choice: '0' for centigrade to farhenheit and '1' for farhenheit to centigrade:"))
if choice==0:
    centigrade=float(input("Enter the centigrade value:"))
    print("The corresponding farhenheit value is:",9*centigrade/5+32)
elif choice==1:
    farhenheit=float(input("Enter the farhenheit value:"))
    print("the corresponding centigrade value is:",(farhenheit-32)*5/9)
else:
    print("Invalid Service!")