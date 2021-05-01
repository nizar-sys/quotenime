
import requests
import time
url = "https://animechan.vercel.app/api/random"

print("\nWellcome to anime quote generator")
time.sleep(0.3)
print("Type 'quit' or 'exit' to exit")
while (True):
    generate = input("\nPress [Enter] to generate quote \n")
    if generate == 'quit' or generate == 'exit':
        print("Thanks for use this tool :)")
        time.sleep(0.5)
        exit()
    else:
        quote = requests.get(url).json()['quote']
        chara = requests.get(url).json()['character']
        print("\n")
        print(quote + "\n" + "- " + chara)
