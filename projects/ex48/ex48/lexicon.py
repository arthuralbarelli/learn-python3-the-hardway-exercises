def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(text_input):

    words = text_input.split()
    word_tuples = []

    for word in words:
        if word.lower() in ['north', 'south', 'east']:
            word_tuples.append(('direction', word))
        elif word.lower() in ['go', 'kill', 'eat']:
            word_tuples.append(('verb', word))
        elif word.lower() in ['the', 'in', 'of']:
            word_tuples.append(('stop', word))
        elif word.lower() in ['bear', 'princess']:
            word_tuples.append(('noun', word))
        elif isinstance(convert_number(word), (int, float)):
            word_tuples.append(('number', convert_number(word)))
        else:
            word_tuples.append(('error', word))

    return word_tuples