def basic_calculator():
  while(True):

    oper=input("Enter The Operation (+,-,*,/)")

    if oper=="+":
      num1=int(input("Enter First Number: "))
      num2=int(input("\nEnter Second Number: "))
      print(f"Answer {num1+num2}")
    elif oper=="-":
      num1=int(input("Enter First Number: "))
      num2=int(input("\nEnter Second Number: "))
      print(f"Answer {num1-num2}")
    elif oper=="*":
      num1=int(input("Enter First Number: "))
      num2=int(input("\nEnter Second Number: "))
      print(f"Answer {num1*num2}")
    elif oper=="/":
      num1=int(input("Enter First Number: "))
      num2=int(input("\nEnter Second Number: "))
      print(f"Answer {num1/num2}")
    else:
      print("Invalid Input, Try Again!")

    cont=input("Do You Want To Continue: (Yes/No): ").lower()
    if cont=="yes":
      continue
    elif cont=="no":
      break

basic_calculator()
