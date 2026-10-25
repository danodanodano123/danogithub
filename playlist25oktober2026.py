playlist = ["Versace on the Floor", "GO!", "La Campanella", "Swim", "Southern Cross"]
print(f"Your playlist is currently: {playlist}")
indextoplay=int(input("Index of the song to play: "))
indextoreplace=int(input("Index of the song to replace: "))
replacement=input("What song to replace it with: ")

playlist[indextoreplace]=replacement
print(f"\nCurrently Playing: {playlist[indextoplay]}")
print(f"NEW PLAYLIST: {playlist}")