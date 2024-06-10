import os
from dotenv import dotenv_values

def generate_env_example():
    # Carga las variables de entorno desde el archivo .env
    env_vars = dotenv_values(".env")
    
    # Genera el contenido del archivo .env.example con los nombres de las variables de entorno en blanco
    example_content = ""
    for var_name in env_vars.keys():
        example_content += f"{var_name}=\n"
    
    # Escribe el contenido en el archivo .env.example
    with open(".env.example", "w") as f:
        f.write(example_content)

if __name__ == "__main__":
    generate_env_example()
