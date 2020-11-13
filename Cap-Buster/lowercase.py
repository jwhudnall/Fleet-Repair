# ToDo: Add sentence splits/capitalization on '?' '!'


user_text = input('Text to be translated: ')

def split_to_sentences(string):
    '''Accepts a string. Returns a list of sentences'''
    sentence_list = string.split('.')
    return sentence_list

def capitalize_sentences(lst):
    '''Accepts a list as input. Returns a list of capitalized sentences'''
    capitalized = []
    for sentence in lst:
        stripped_sentence = sentence.strip()
        capital_sentence = stripped_sentence.capitalize()
        capitalized.append(capital_sentence)
    return capitalized

def join_sentences(lst):
    return '. '.join(lst)

def main():  
    capitalized = capitalize_sentences(split_to_sentences(user_text))
    result = join_sentences(capitalized)
    print(result)

main()
