from linked_list import LinkedList

def process_linked_list(linked_list):
    letters = []  # lista para armazenar letras
    digits = []   # lista para armazenar dígitos

    # Iterar sobre a lista encadeada
    for char in linked_list:
        if linked_list.is_digit(char):
            digits.append(char)  # adiciona dígito à lista
        else:
            letters.append(char)  # adiciona letra à lista

    digits.reverse()  # inverte a ordem dos dígitos
    return letters + digits  # retorna letras seguidas dos dígitos
