
print("\n                Precious Blood Bank               ")
print("\n                This Is A Blood Bank Portal\n\n")
print("Follow the above instructions")
print("\nFOR Admin: Press 1")
print("FOR User : Press 2")
choice=int(input())

class Donor:
  COUNT=0
  req=[]
  def __init__(self,name,age,sex,blood_group):
    self.Name=name
    self.Age=age
    self.Sex=sex
    self.BloodGroup=blood_group
    
    Donor.COUNT+=1
    

donor1=Donor('James',30,'Male','AB-')
donor2=Donor('Jhon',43,'Mmale','AB+')
donor3=Donor('Tom',24,'Male','O+')
donor4=Donor('Peter',29,'Male','A-')
donor5=Donor('Parker',30,'Male','B+')
donor6=Donor('Zendaya',23,'Female','O-') 
donor7=Donor('Mary',44,'Female','AB+')
donor8=Donor('Jane',40,'Female','O+')
donor9=Donor('Emma',36,'Female','B-')
donor10=Donor('Kane',31,'Male','AB-') 

def Request(reqtype):
    Donor.req.append(reqtype)
    print("Your request for blood is succesfull")


def blood_banks():
  print("\n\nThe below mentioned blood banks are near you: ")
  print("\n1. Healthcare Blood bank")
  print("\n2. ABC Blood Bank")
  print("\n3. Manipal Blood Bank")
  print("\n4. Konidela Blood Bank")
  print("\n5. Amma Blood Bank")
  print("\n6. Rainbow Hospital and Blood Bank")


def rare_blood_groups():
  print("\nDonors with rare blood groups \n ")
  print("James       25         Male           AB-\n")
  print("Zendaya     24         Female        B-\n")
  print("Kane        31         Male           AB-\n")
  print("Emma        36         Female         O-\n")

if choice==1:
  print("\n\n               Welcome Admin                \n")
  u=input("Please enter the username: ")
  if u=='username':
    p=input("\n Please enter your password: ")  
    if p=='password':
      print("\nSigned In successfully!")
      print("\n           Admin Welcome back     ")
      print("\n Your Dashboard")
      print("\n1. Details of the Donors")
      print("\n2. list of the Blood Banks")
      print("\n3. Details of the donors with rare blood groups")
      a=int(input("\nEnter a choice index from the above: "))
      if a==1:
        donor_list=[donor1,donor2,donor3,donor4,donor5,donor6,donor7,donor8,donor9,donor10]
        for i in donor_list:
          print("\n")
          print(i.__dict__)
      elif a==2:
        blood_banks()
      elif a==3:
        rare_blood_groups()
        
      else:
        print("\nInvalid Choice")
    else:
      print("\nPassword  Incorrect")
  
  else:
    print("\n Please enter the correct Username")

elif choice==2:
  print("\n              Welcome User                    \n")
  u=input("Please enter the username: ")

  if u=='Rohit' or 'Virat' or 'Bumrah' or 'Rishab' or 'Rahane':
    p=input("\n Please enter your password: ")  
    if p=='password':
      print("\n Successfully Logged in")
      print("\n             Hello User Welcome back            ")
      print("\nSelect from below dashboard")
      print("\n1. Request for blood group") 
      print("\n2. List of the Blood Banks")
      print("\n3. Details of the donors with rare blood groups")
      user_choice=int(input("\n\nEnter a choice from the above: "))
      if user_choice==1:
        n=input("Please enter your blood group:")
        Request(n)
      elif user_choice==2:
        blood_banks()
      elif user_choice==3:
        rare_blood_groups()
      else:
        print("\nInvalid Choice!")
    else:
      print("\nPassword Incorrect")
  
  else:
    print("\n Please enter the correct Username")

else:
  print("\nWrong Choice")
      




