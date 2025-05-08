import webbrowser

options = {"1":"Playlists", 
           "2":"Search"}

print("Choose Option:")
for key,value in options.items():
    print(f"{key} . {value}")

option_selected = int(input("\nEnter the option by number:"))
if (option_selected == 1):
    webbrowser.open("https://www.youtube.com/feed/playlists")
elif (option_selected == 2):
    search = input("Search: ").replace(" ", "+")
    webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
else:
    print("Invalid Options")