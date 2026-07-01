def dividir_texto(texto, tamaño=500):

    fragmentos = []

    for i in range(0, len(texto), tamaño):
        fragmento = texto[i:i+tamaño]
        fragmentos.append(fragmento)

    return fragmentos


if __name__ == "__main__":

    texto = """
    Soluciones Atenea tiene una política de vacaciones.
    Los colaboradores deben solicitar vacaciones con anticipación.
    Recursos Humanos revisa las solicitudes.
    """

    partes = dividir_texto(texto)

    for numero, parte in enumerate(partes):
        print("\n--- CHUNK", numero, "---")
        print(parte)