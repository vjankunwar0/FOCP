import random 

def valid_email(email,domain):#Function to validate email
    if email.count("@")!=1:
        return False
    
    if len(email.split("@")[0])<2:
        return False

    if email.split("@")[1]!=domain:
        return False
    
    return True




connection_error=[False,False,False,False,False,False,False,False,False,True]
operator_name=["bruce","emma","john","ellen","tina"]#shows random operator name
exit_statement=["bye","exit","help","goodbye","end"] #if the input is these words it will close the program
no_output=["hmm","I didn't understand","I see","sorry"]#if the word doesn't contain in the statement it give this result as a random format
print("Welcome to Pop Chat \nOne of our operators will be pleased to help you today.\n")
email=input("Please enter your Poppleton email address:")

if valid_email(email,"pop.ac.uk"):#checks whether the mail is valid or not 
    print("Hi, {}! Thank you, and Welcome to PopChat!".format(email.split("@")[0]))
    print(f"My name is {random.choice(operator_name)}, and it will be my pleasure to help you.")
    while True:
        sent=input("-->")
        if random.choice(connection_error):
            print("Network error")
            break
        if any(word in sent.lower() for word in exit_statement):#checks whether the satement contains the words like library,wifi,fee etc
            print("Thanks, {}, for using PopChat. See you again soon!".format(email.split("@")[0]))
            break    
        elif("library" in sent):
            print("The library is closed today.")
        elif("WiFi" in sent):
            print("WiFi is excellent across the campus.")
        elif "deadline" in sent:
            print( "Your deadline has been extended by two working days.")
        elif "books" in sent:
            print( "You can access the book from the library")
        elif "timing" in sent:
            print( "The class timing will be sent in your pop mail")
        elif "classes" in sent:
            print( "You have two classes today")
        
        else:
            print(random.choice(no_output))
            
else:
    print("This email is not valid")#shows this when the mail is incorrect