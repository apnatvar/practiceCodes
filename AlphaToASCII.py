a_string = input("Enter a string to display their relevant ASCII Values\n")
indexNumber = []
for character in a_string:
   if (character == " "):#ignores all spaces in your text
      continue
   #incase you need to add spaces comment out the above 2 line
   print("Original Character:",character,"- ASCII Value:",ord(character))
