
alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input ("Type 'encode' to encrypt, Type decode to 'decrypt'\n")
text=input("Type your massage: \n")
shift=int(input("type the shift number: \n"))

def caeser(start_text,shift_amount,cipher_direction):
  end_text=""
  if cipher_direction == "decode":
     shift_amount *= -1
  for letter in start_text:
    position=alphabet.index(letter)
    new_position=position+shift_amount
    new_letter=alphabet[new_position]
    end_text += new_letter
  print(f"Here the {direction}d. The encoded text is {end_text}")

caeser(start_text=text, shift_amount=shift, cipher_direction=direction)