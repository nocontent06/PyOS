import code
import sys
sys.path.append("../resources")
sys.path.append("./resources")
sys.path.append(".\\resources")
sys.path.append("..\\resources")
import os
import platform
import time
import psutil
import cpuinfo
import socket
from tkinter import * 
try:
    from tqdm import tqdm
except:
    os.system("pip3 install tqdm")
import cpuinfo

# from datetime import datetime

def clearConsole():
        command = "clear"
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)
clearConsole()
"""
def check_usr():
    with open("./resources/USERS.txt" , "r") as file:
        if file.read(9) == "Username:":
            print(f"Logging in as {file.readline()}")
        else:
            print("No User found please try again!")
        time.sleep(3)
check_usr()
""""""
def username():
    global username
    with open("./resources/USERS.txt" , "r") as file:
        username = file.readline()
        return username
username()
"""
def get_size(bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

def install_necessary_plugins():
    try:
        import cpuinfo
    except:
        missing_package = "py-cpuinfo"
        print()
        print("=" * 40 , " Package missing ", "=" * 40)
        print(f"{missing_package} is required to execute this script!")
        print()
        print(f"It will be installed automatically! ")
        print()
        print(f"Error: 0c: {missing_package} not found!")
        print()
        proceed_str = str(input("(Y) Yes to Proceed ; (N) No to abort: "))
        
        if proceed_str == "Y":
            os.system(f"pip3 install {missing_package}")
        
    try:
        f = open('./resources/USERS.txt')
        f.close()
    except:
        print("An error occured while opening the file 'Users.txt' make sure this File exists and try again!")
def loading_scr():
    print("\n OS is Loading...")
    for i in tqdm(range(100)):
        time.sleep(0.05)
    print("Necessary Files loaded...")
    print("Loading Kernel...")
    for i in tqdm(range(100)):
        time.sleep(0.025)
    print("Kernel loaded successfully...")
    print("Starting OS...")
    time.sleep(2)
    clearConsole()

def login_scr():
        #global usr_name
        login_inp = 0
        login_inp = int(input("Create a User ('1') ('Create'): "))
        if login_inp == 1 or login_inp == "Create":
            clearConsole()
            acc_creator()


def sys_inf():
        """
        global OS_architecture
        global OS_Platform
        global OS_System
        """
        global inp
        global abort
        global sys_abort
        clearConsole()
        print(f"About your System: ")
        print("\n" * 2)
        """
        print(f"Architecture: {OS_architecture}") 
        print(f"Platform: {OS_Platform}")
        print(f"System: {OS_System}")
        """
        #print(f"4.) Processor: {cpuinfo.get_cpu_info()['brand_raw']}")

        # print CPU information
        print("="*40, "CPU Info", "="*40)
        print()
        # Get CPU Name
        #cpuname = "i5-2500"
        cpuname = cpuinfo.get_cpu_info()['brand_raw']
        codename = cpuname.replace('Intel(R) Core(TM) ', '')
        proc_build = ""

        if codename.startswith("i3"):
            proc_build = "i3-"
        elif codename.startswith("i5"):
            proc_build = "i5-"
        elif codename.startswith("i7"):
            proc_build = "i7-"
        elif codename.startswith("i9"):
            proc_build = "i9-"
        else:
            print("Your Processor-Build cannot be found! \nPerhaps you have no Processor from the i-Series!")

        if len(codename) == 6:
            codename = "Penryn"
        elif codename.startswith(proc_build + "2"):
            codename = "Sandy Bridge"
        elif codename.startswith(proc_build + "3"):
            codename = "Ivy Bridge"
        elif codename.startswith(proc_build + "4"):
            codename = "Haswell"
        elif codename.startswith(proc_build + "5"):
            codename = "Broadwell"
        elif codename.startswith(proc_build + "6"):
            codename = "Skylake"
        elif codename.startswith(proc_build + "7"):
            codename = "Kaby Lake"
        elif codename.startswith(proc_build + "8"):
            codename = "Coffee Lake"
        elif codename.startswith(proc_build + "9"):
            codename = "Coffee Lake Refreshed"
        elif codename.startswith(proc_build + "10"):
            codename = "Comet Lake"
        elif codename.startswith(proc_build + "11"):
            codename = "Tiger Lake"
        elif codename.startswith(proc_build + "12"):
            codename = "Alder Lake"
        else:
            codename = "I think Penryn, or another codename which isn't implemented"
        print("CPU-Name:",cpuname)
        print("CPU-Codename:", codename)
        print()
        # number of cores
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Threads:", psutil.cpu_count(logical=True))
        print()
        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max/1000}Ghz")
        print(f"Min Frequency: {cpufreq.min/1000}Ghz")
        print(f"Current Frequency: {cpufreq.current/1000}GHz")
        print()
        # CPU usage
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")


        # Memory Information
        print("="*40, "Memory Information", "="*40)
        # get the memory details
        svmem = psutil.virtual_memory()
        print(f"Total: \t {get_size(svmem.total)}")
        print(f"Available: {get_size(svmem.available)}")
        print(f"Used: \t {get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")
        print()
def help():
    print("""
            0... \t\t Logging out of the Operating System
            1... \t\t Shows Information about your System
            2... \t\t Login screen (beta)
            3... \t\t Creates/Deletes a new File/Folder
            """)
# Call the Function 'Loading Screen'
loading_scr()

# Function to install necessary PlugIns  
install_necessary_plugins()

# define some Variables
inp = -1
abort = 0
sys_ver = "1.3.1"
#usrname = username()
acc_c_ver = "0.1.1 beta"
#USR = "Username:"
#PASSWD = "Password:"
usr_name = "Demo"


# acc_c_ver = "1.0"

# the Clear Console Function



# Define Variables for cpuinfo

OS_architecture = platform.machine()
OS_Platform = platform.platform()
OS_System = platform.system()

# The current Program
while abort == 0:

    def acc_creator():
        print("=" * 80)
        print("\t" * 2 + "Account Creator Software © NoContent_06" + "\t" * 2 + "Version: " + str(acc_c_ver))
        print("=" * 80)
        global usr_name
        
        #with open('./resources/USERS.txt', 'a') as file:
        usr_name = str(input("How is the User called? $> "))
            #file.write(f"{usr_name}\n")
        passwd = str(input("Whats his Password? $> "))
            #file.write(f"{passwd}\n\n")
        #file.close()
        
        def chk():
            #with open(".\\resources\\USERS.txt" , "r") as file:
            print(f"Logging in as {usr_name}")
                # else:
                #     print("No User found please try again!")
                #file.close()
            time.sleep(3)
        chk()
        
        print("Creating User Account... Please Wait")
        time.sleep(3)
        #acc_creator()
    
    def welc_scr():
        #usr_name = "Demo"
        global inp
        global abort
        global usr_name
        #global usr_name
        print("=" * 80)
        print(f"\t \t \t Welcome to PyOS! \t Version: {sys_ver}")
        print("=" * 80)
        inp = input(f"What do you want to do?: \t\n Type in 'help' if you want to see a list of available commands \n \n {usr_name} $> ")
       
        if inp == "1":
            sys_abort = 0
            while sys_abort != "exit" or sys_abort == "0":
                
                sys_inf()
                sys_abort = input("(Y) to go back to the main menu: ")
                time.sleep(1)

                    
                # sys_abort = input("(Y) to go back to the main menu: ")
                print("\n" * 2)
                time.sleep(0.1)
                if sys_abort == "Y" or sys_abort == "y":
                    sys_abort == 1
                    break
                else:
                    print("Invalid input try again!")
                    time.sleep(1)

            print("Back to Main Menu...")
            time.sleep(2)
            inp = -1

        elif inp == "2":
            login_scr()
            inp = -1

        elif inp == "3":
            inp_3 = input("File (1) ('File') or Folder (2) ('Folder') \n $> ")
            
            if inp_3 == "1" or inp_3 == "File":
                inp_3_1 = input("File: Delete (1) (Del) or Create (2) (make) \n $> ")
                if inp_3_1 == "1" or inp_3_1 == "Del":
                    name_file_1 = input("How is this File called?: \n $> ")
                    if os.path.exists(f"{name_file_1}"):
                        os.remove(f"{name_file_1}")
                    else:
                        print("Error 4b: The file does not exist!") 
            
                elif inp_3_1 == "2" or inp_3_1 == "make":
                    print("Create a new File...")
                    time.sleep(0.5)
                    name_file = input("Name that File: \n $> ")
                    f= open(f"{name_file}", "w+")
                    f.write = os.system(f"nano {name_file}")
                    f.close()
                else:
                    print("Input invalid, try again!")
                    time.sleep(1.5)
            
            elif inp_3 == "2" or inp_3 == "Folder":
                inp_3_2 = input("Folder: Delete (1) or Create (2)")
                if inp_3_2 == "1":
                    name_dir = input("How is the Folder called?: ")
                    os.rmdir(f"{name_dir}")
                elif inp_3_2 == "2":
                    print("Creating Folder...")
                    time.sleep(0.5)
                    directory_mkdir = input("How would you call your Folder?: ")
                    path = "/Users/felix/OneDrive\ -\ HTL\ Villach/Documents/Proghrammieren/Python/OS"
                    if os.name in ('nt', 'dos'):
                      os.system(f"mkdir .\{directory_mkdir}")
                    else:
                      os.system(f"mkdir ./{directory_mkdir}")
                    print(f"Successfully created {directory_mkdir}!")
                    time.sleep(1)
                else:
                    print("Input invalid! Try again!")
                    time.sleep(1.5)


        elif inp == "0":
            print("Bye!")
            print("Logging off...")
            time.sleep(2)
            abort = 1

        elif inp == "help":
            sys_abort = 0
            while sys_abort != "exit" or sys_abort == 0:
                help()
                print("\n" * 2)
                time.sleep(0.1)
                sys_abort = input("(Y) to go back to the main menu: ")
                if sys_abort == "Y":
                    sys_abort == 1
                    break
                else:
                    print("Invalid input try again!")
                    time.sleep(1)

            print("Back to Main Menu...")
            time.sleep(2)
            inp = -1
            
        else:
            print("Invalid input! Please make sure to read the manual ('help')")
            time.sleep(1.5)
        
    while abort == 0:
        welc_scr()
        clearConsole()


##############################
# Vorschläge: 
#   1.) Aktualis. d. CPU-Info á 1 sec.
#   2.) Prozessorname                   (erledigt)
#   3.) Einstellungen "Fenster"
#   4.) Minicon for editing files
##############################

    