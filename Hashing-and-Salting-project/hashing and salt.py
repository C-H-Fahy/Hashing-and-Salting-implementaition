import time
def sha256(hashie):
    #hashfunction
    import hashlib
    hashie = hashie.encode('utf-8') 
    m = hashlib.sha256(hashie)
    return m.hexdigest()

def EnterPassword():
        trys = 0
        while (trys < 3):
                username = input("type your username: ")
                #takes password input
                password = input("type your password: ")
                
                #gets file names
                saltname = username + "salt.txt"
                username = username + ".txt"
                        
                #opens salt file
                text_file = open(saltname, "r")
                salt1 = text_file.read(1023)
                text_file.close()
                #opens the hashed passwords file
                text_file = open(username, "r")
                correctpassword = text_file.read(500)
                text_file.close()
            
                #adds the salt to the password input
                saltedpassword = password + salt1

            
                #hashes the saltedpassword
                hashedpassword = sha256(saltedpassword)

                #compears hashed passwords
                if hashedpassword != correctpassword:
                        trys += 1
                        print("your password or username is incorrect please wait")
                        time.sleep(5)
                if trys == 3:
                        print("you have been locked out for using to many failed trys")
                        return False
                if hashedpassword == correctpassword:
                        print ("Password Correct ")
                        trys = 0
                        return True
                        break
                        

def Createpassword():
    import random
    import hashlib
    username = input("type your username")
    newpassword = input("type your new password? ")

    #adds some salt
    b = random.randint(0, 255)
    randomsalt = str(b)
    
    saltedpassword = (newpassword + randomsalt)

    #hashes the newpassword
    finishedpassword = sha256(saltedpassword)

    #creates file names
    saltname = username + "salt.txt"
    username = username + ".txt"
    
    #saves the hashedpassword and the salt
    text_file = open(username, "w")    
    text_file.write(finishedpassword)
    text_file.close()
    text_file = open(saltname, "w")    
    text_file.write(randomsalt)
    text_file.close()
    print("your new password has been saved")

def login():
        startup = 'm'
        trys = 0
        startup = input("type 2 to change/create a new password or type 1 to login ")
        if startup == "1":
                print(EnterPassword())


        if startup == "2":
                Createpassword()
login()
