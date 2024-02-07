def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
    return len(text)

# Test the function
if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)

