import os
import time
from time import sleep
import ctypes
import string
import colorama
def quickChecker(code, Webhook):  # Used to check a single code at a time
        # Generate the request url
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        time.sleep(0.2)
        response = requests.get(url)  # Get the response from discord
        print(response)
        if response.status_code == 200:  # If the responce went through
            # Notify the user the code was valid
            print(f" Valid | {code} ", flush=True, end="" if os.name == 'nt' else "\n")
            DiscordWebhook(  # Send the message to discord letting the user know there has been a valid nitro code
                    url=Webhook,
                    content=f"Valid Nito Code detected! @everyone \n{code}"
                ).execute()

            return True  # Tell the main function the code was found

        # If the responce got ignored or is invalid ( such as a 404 or 405 )
        else:
            # Tell the user it tested a code and it was invalid
            print(f" Invalid | {code} ", flush=True, end="" if os.name == 'nt' else "\n")
            return False  # Tell the main function there was not a code found


print(colorama.Fore.CYAN + """
$$$$$$$$\                              $$\                     $$$$$$$\                               $$\ 
$$  _____|                             $$ |                    $$  __$$\                              $$ |
$$ |    $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$\   $$\   $$\       $$ |  $$ |$$$$$$\  $$$$$$$\   $$$$$$\  $$ |
$$$$$\ $$  __$$\ $$  __$$\ $$  _____|\_$$  _|  $$ |  $$ |      $$$$$$$  |\____$$\ $$  __$$\ $$  __$$\ $$ |
$$  __|$$ |  \__|$$ /  $$ |\$$$$$$\    $$ |    $$ |  $$ |      $$  ____/ $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |
$$ |   $$ |      $$ |  $$ | \____$$\   $$ |$$\ $$ |  $$ |      $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |
$$ |   $$ |      \$$$$$$  |$$$$$$$  |  \$$$$  |\$$$$$$$ |      $$ |     \$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |
\__|   \__|       \______/ \_______/    \____/  \____$$ |      \__|      \_______|\__|  \__| \_______|\__|
                                               $$\   $$ |                                                 
                                               \$$$$$$  |                                                 
                                                \______/                                                  """)

try:
    options = int(input(colorama.Fore.GREEN + """
|--------------------------------------------------------------------------------------------------------|
|                                                                                                        |
|1.Nitro Gen/Checker        2.Coming Soon        3.Coming Soon        4.Coming Soon        5.ComingSoon  |
|                                                                                                        |
|--------------------------------------------------------------------------------------------------------|
|                                                                                                        |
|6.Coming Soon        7.Coming Soon        8.Coming Soon        9.Coming Soon        10.Coming Soon      |
|                                                                                                        |
|--------------------------------------------------------------------------------------------------------|
"""))
except ValueError:
            input("Specified input wasn't a number.\nPress enter to exit")
            exit()  # Exit progra
if options == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colorama.Fore.LIGHTMAGENTA_EX +"""  
███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████       ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░   ░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░      ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
   ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒     ░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
         ░  ░              ░         ░ ░           ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░     
                                                                                                                           """)
    if os.name == "nt":  # If the system is windows
        print("")
        ctypes.windll.kernel32.SetConsoleTitleW("FrostyPanel Nitro Generator and Checker")  # Change the
    else:  # Or if it is unix
        print(f'\33]0;FrostyPanel Nitro Generator and Checker\a', end='', flush=True)  # Update title of command prompt
                                                                                                                                   
    try:  # Check if the requrements have been installed
        from discord_webhook import DiscordWebhook  # Try to import discord_webhook
    except ImportError:  # If it chould not be installed
    # Tell the user it has not been installed and how to install it
        input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3'} -m pip install discord_webhook'\nPress enter to continue.")
        exit()
    try:  # Setup try statement to catch the error
        import requests  # Try to import requests
    except ImportError:  # If it has not been installed
    # Tell the user it has not been installed and how to install it
        input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
        exit()  # Exit the program
    try:  # Setup try statement to catch the error
        import numpy  # Try to import requests
    except ImportError:  # If it has not been installed
    # Tell the user it has not been installed and how to install it
        input(f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
        exit()  # Exit the program
    url = "https://google.com"
    try:
        response = requests.get(url)  # Get the responce from the url
        print("Internet check")
        time.sleep(.4)
    except requests.exceptions.ConnectionError:
        # Tell the user
        input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
        exit()  # Exit program


    tocontinuegen1 = input("Reponse 404 = Invalid Code | Response 429 = Request Denied | Enter to continue")
    tocontinuegen2 = input("if a valid code is found everyone within server of webhook will be pinged and the code will be sent, Enter to Continue")
    Webhook = str(input("Paste Discord Webhook:"))
    try:
        DiscordWebhook(  # Let the user know it has started logging the ids
                        url=Webhook,
                        content=f"```Started checking nitro codes\nI will send any valid codes here```"
                    ).execute()
    except:
        input("Invalid Webhook \nPress enter to exit")
        exit()
    try: 
        num = int(input("How Many Codes To Generate?"))
    except:
        input("Invalid number entered \nPress enter to exit")
        exit()

    print(f"Generator and Checker Started, Amount: {num}, Webhook: {Webhook}")


    valid = []  # Keep track of valid codes
    invalid = 0  # Keep track of how many invalid codes was detected
    chars = []
    chars[:0] = string.ascii_letters + string.digits

    c = numpy.random.choice(chars, size=[num, 16])
    for s in c:  # Loop over the amount of codes to check
        try:
            code = ''.join(x for x in s)
            nurl = f"https://discord.gift/{code}"  # Generate the url

            result = quickChecker(code, Webhook)  # Check the codes

            if result:  # If the code was valid
                # Add that code to the list of found codes
                valid.append(url)
            else:  # If the code was not valid
                invalid += 1  # Increase the invalid counter by one
        except KeyboardInterrupt:
                # If the user interrupted the program
            print("\nInterrupted by user")
            break  # Break the loop

        except Exception as e:  # If the request fails
            print(f" Error | {url} ")  # Tell the user an error occurred

    DiscordWebhook(  # Send the message to discord with results
        url=Webhook,
        content=
        f"""
        Results:
            Valid: {len(valid)}
            Invalid: {invalid}
            Valid Codes: {', '.join(valid)}""").execute()  # Give a report of the results of the check
    
    print(
    f"""
    Results:
        Valid: {len(valid)}
        Invalid: {invalid}
        Valid Codes: {', '.join(valid)}""")  # Give a report of the results of the check

        # Tell the user the program finished
    input("\nThe end! Press Enter 5 times to close the program.")
    [input(i) for i in range(4, 0, -1)]  # Wait for 4 enter presses


