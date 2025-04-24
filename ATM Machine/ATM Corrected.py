con=1
mbal=1000
damt1=float(input("Enter an Amount: "))
print(f"Amount Rs.%.2f Deposited"%(damt1))
while con<=3:
   ch=int(input("1.Deposit\n2.Withdraw\n3.Exit\nEnter Choice : "))
   if ch==1:
      damt2= float(input("Enter an Amount to Deposit : "))
      damt1+=damt2
      print(f"Amount deposited : {damt1}")
      con+=1
   elif ch==2:
      wamt1 = float(input("Enter withdraw amt: "))
      if wamt1>=100:
         if wamt1<=(damt1-mbal):
            damt1 -= wamt1
            print(f"Amount withdrawn : {wamt1}\nRemaining amt : {damt1}")
         else:
            print(f"Insufficent amt")
      else:
         print(f"Enter Min Balance: ")
      con+=1
   elif ch==3:
      print(f"No of Transaction Exceeded...")
      exit(0)
   else:
      print("Wrong Choice...")