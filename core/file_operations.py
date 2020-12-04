def save_to_file(content, filename):
    """
    Save content to filename
    """
    with open(filename, 'w') as file:
        file.write(content)


def read_file(filename):
    """
    Return the content of the file
    """
    with open(filename, "r") as file:
        return file.read()
