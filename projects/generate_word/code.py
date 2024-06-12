

def generate_word(chat_generated_minute):

    file_path = 'minuta.md'
    with open(file_path, 'w') as file:
        file.write(chat_generated_minute)
    
    return file_path