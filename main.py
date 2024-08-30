"""
License: Apache
Organization: UNIR
"""

import os
import sys
from colorama import Fore, Style, init

# Inicializar colorama para habilitar colores en la consola
init(autoreset=True)

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print(Fore.BLUE + Style.BRIGHT + "Se debe indicar el fichero como primer argumento")
        print(Fore.BLUE + Style.BRIGHT + "El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    print(Fore.BLUE + Style.BRIGHT + f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                # Convertir cada palabra a mayúsculas
                word_list.append(line.strip().upper())
    else:
        print(Fore.BLUE + Style.BRIGHT + f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(Fore.BLUE + Style.BRIGHT + str(sort_list(word_list)))
