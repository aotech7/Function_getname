


#defining the functions
def name_function(name):
    print("Your name is " + name)
    print()
    print("Welcome! " + name)

def ask():
    ask = input("Would  you like to give a name? type Y for 'Yes' or N for 'No': ")
    return(ask)
    


def get_name():
    name = input("What is your name ? ")
    return name

def run_it(answer):
    if answer == "Y":
        name = get_name()
        name_function(name)

    else:
        print("Program ended, goodbye")

#run the program
answer = ask()
run_it(answer)



#name = get_name()
