from krk_biblio.analizador_monedas import AnalizadorMonedas, obtener_pares_disponibles

# Bucle para solicitar al usuario que ingrese un par de monedas válido
while True:
    par_moneda_usuario = input("Ingrese el par de monedas a analizar (ejemplo: XBTEUR): ")
    pares_disponibles = obtener_pares_disponibles()

    if par_moneda_usuario in pares_disponibles:
        analizador = AnalizadorMonedas(par_moneda_usuario)
        analizador.procesar()
        break
    else:
        print(f"El par de monedas '{par_moneda_usuario}' no está disponible. Pares disponibles:")
        print(" // ".join(pares_disponibles))
