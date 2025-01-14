meme_dict = {
    "LOL": "Una respuesta a algo gracioso",
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo o enojado"
}

print("¡Bienvenido a la aplicación de diccionario de memes!")
print("Aquí puedes buscar palabras de jerga y su significado.")
print("Escribe las palabras en MAYÚSCULAS para que funcione correctamente.")

for i in range(10):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!):")
    if word in meme_dict.keys():
        print("la palabra:",{word},"es:",{meme_dict[word]},)
    else:
        print("Lo siento, no conozco la palabra" ,{word},"¡Intenta otra!")

print("Gracias por usar la aplicación de diccionario. ¡Hasta luego!")
