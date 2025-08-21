leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

#muutetaan Asiat grammoiksi
leiviskagramma = leiviska * 20 * 32 * 13.3

naulagramma = naula * 32 * 13.3

luotigramma = luoti * 13.3

massagramma = leiviskagramma + naulagramma + luotigramma

#Erotetaan kokonaiset kilot
kilo = massagramma // 1000
# yli jäävät grammat saadaan jakojäännoksen avulla
gramma = massagramma % 1000

print("Massa nykymittojen mukaan: ")
print(f"{kilo:2.0f} kg {gramma:.2f} g")
