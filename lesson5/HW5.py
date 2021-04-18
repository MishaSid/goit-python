''' normalize function transliterates Cyrillic characters into Latin;
    replaces all characters except letters of the Latin alphabet and numbers with the character '_';
    uppercase letters remain uppercase and lowercase letters remain lowercase after transliteration
'''


def normalize(text):
    dictionary = {ord('А'): 'A',ord('Б'): 'B',ord('В'): 'V',ord('Г'): 'H',ord('Ґ'): 'G',ord('Д'): 'D',ord('Е'): 'E',ord('Є'): 'Ye',ord('Ж'): 'Zh',ord('З'): 'Z',ord('И'): 'Y',ord('І'): 'I',ord('Ї'): 'Yi',ord('Й'): 'Y',\
    ord('К'): 'K',ord('Л'): 'L',ord('М'): 'M',ord('Н'): 'N',ord('О'): 'O',ord('П'): 'P',ord('Р'): 'R',ord('С'): 'S',ord('Т'): 'T',ord('У'): 'U',ord('Ф'): 'F',ord('Х'): 'Kh',ord('Ц'): 'Ts',ord('Ч'): 'Ch',ord('Ш'): 'Sh',ord('Щ'): 'Shch',\
    ord('Ь'): '',ord('Ю'): 'Yu',ord('Я'): 'Ya',ord('а'): 'a',ord('б'): 'b',ord('в'): 'v',ord('г'): 'h',('ґ'): 'g',ord('д'): 'd',ord('е'): 'e',ord('є'): 'ie',ord('ж'): 'zh',ord('з'): 'z',ord('и'): 'y',ord('і'): 'i',ord('ї'): 'i',ord('й'): 'i',\
    ord('к'): 'k',ord('л'): 'l',ord('м'): 'l',ord('н'): 'n',ord('о'): 'o',ord('п'): 'p',ord('р'): 'r',ord('с'): 's',ord('т'): 't',ord('у'): 'u',ord('ф'): 'f',ord('х'): 'kh',ord('ц'): 'ts',ord('ч'): 'ch',ord('ш'): 'sh',ord('щ'): 'shch',ord('ь'): '',ord('ю'): 'iu',ord('я'): 'ia'}
    keys = []
    for key in dictionary:
        keys.append(key)
    normalized_text = []
    for letter in text:
        if ord(letter) in keys:
            letter = letter.translate(dictionary)
            normalized_text.append(letter)
        elif 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
            normalized_text.append(letter)
        elif letter.isdigit():
            normalized_text.append(letter)
        else:
            normalized_text.append('_')
    normalized_text = ''.join(normalized_text)
    return normalized_text
    


text = input('Please type your text: ')
if __name__ == '__main__':
    print(normalize(text))
