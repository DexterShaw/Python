def is_palindrom(text):
    if len(text)in [0, 1]:
        return True
    if text[0] == ' ':
        return is_palindrom(text[1:])
    if text[-1] == ' ':
        return is_palindrom(text[:-1])
    if text[0].lower() == text[-1].lower():
        return is_palindrom(text[1:-1])
    return False


print(is_palindrom('A tO idiota'))