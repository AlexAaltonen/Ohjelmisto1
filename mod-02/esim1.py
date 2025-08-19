käyttäjä = input("Kirjoita nimesi: ")
print("Moro " + käyttäjä + "!")

fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)

celcius = (fahrenheit-32)*5/9

print(f"lämpötila Celscius-asteina: {celcius}")
