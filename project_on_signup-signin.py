data_base={"username":"password"}

def signUp():
  print("\n-----welcome to SignUp Portal-----\n")
  
  while 1:
    userUp=input("Enter a new username: ").lower()
    if userUp == "0" :
      return "SignUp Failed"
    if userUp not in data_base:
      passUp = password_strength()
      
        
       #confirm password()
      data_base.update({userUp:passUp})
      return "SignUp Succesful"
    
    else:
      print('''Username is already taken.....Please try again....
      Press 0 to Exit
      Or''')
# signUp()
def password_strength():   
    l, u, p, d = 0, 0, 0, 0
    s = input("Enter a new password: ")
    capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets="abcdefghijklmnopqrstuvwxyz"
    specialchar="$@_%&#"
    digits="0123456789"
    if (len(s) >= 8):
        for i in s:

             
            if (i in smallalphabets):
                l+=1		

            
            if (i in capitalalphabets):
                u+=1		

             
            if (i in digits):
                d+=1		

            
            if(i in specialchar):
                p+=1	
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
        print("Valid Password")
    else:
        print("Invalid Password")


# password_strength()

def signIn():
  print("\n-----welcome to SignIn Portal-----\n")
  flag=3
  while (flag): 
    userIn = input("Enter your username: ").lower()
    if userIn == "0":
       return "SignIn Failed"
      
    if userIn in data_base:
       passIn=input("Enter your password: ")
  
      
    else:
      flag=flag-1
      print("Invalid Credentials.....",flag,"chances left")
      

# signIn()


def Login():

  while 1:
    mode = int(input('''Enter your Choice :
    Press 1 for SignUp
    Press 2 for SignIn
    Press 0 to Exit 
    '''))
    if mode == 1 :
      print("Welcome to the signUp Portal",signUp())

    if mode == 2:
      print("Welcome to the signIn Portal",SignIn()) 
    elif mode == 0:
      return "Exiting......."
    else:
      print("Invalid Input")
      break


# Login()
