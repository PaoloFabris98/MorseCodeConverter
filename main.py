import morseDict

fraseDaConvertire = input("Inserisci una frase che vuoi convertire in codice morse: ").lower()
fraseConvertita = ""

for x in fraseDaConvertire:
    if(x == " "):
        continue
    if not(x in morseDict.getMorseDict()):
        fraseConvertita += x
        print(f"Non è possibile convertire la lettera: {x}")
    else:
        for i in morseDict.getMorseDict():
            if(i == x):
                fraseConvertita += (morseDict.getMorseDict()[x] + " ")

print(fraseConvertita)