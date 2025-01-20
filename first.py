
def greet(name: str, lastname: str, age: int) -> str:
    """
    Devuelve un mensaje de saludo con el nombre, apellido y edad proporcionados.
    """
    return f"My name is {name}, my lastname is {lastname}, and I am {age} years old."

def verification(name: str, lastname: str, age: int) -> str:
    """
    Verifica si los datos de entrada son válidos y retorna el mensaje de saludo.
    """
    if not name or not lastname:
        raise ValueError("Name and lastname cannot be empty.")
    if age <= 0:
        raise ValueError("Age must be a positive integer.")
    return greet(name, lastname, age)

if __name__ == "__main__":
    try:
        # Solicitar entrada del usuario
        name = input("Enter a name: ").strip()
        lastname = input("Enter a lastname: ").strip()
        age = int(input("Enter an age: "))
        
        # Imprimir el resultado
        print(verification(name, lastname, age))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
