# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 대소문자 구분없이 "H" 또는 "HELP"일 경우 True,
          그렇지 않을 경우 False를 반환함
    Examples:
        >>> import morsecode as mc
        >>> mc.is_help_command("H")
        True
        >>> mc.is_help_command("Help")
        True
        >>> mc.is_help_command("Half")
        False
        >>> mc.is_help_command("HeLp")
        True
        >>> mc.is_help_command("HELLO")
        False
        >>> mc.is_help_command("E")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    lower_user_input = user_input.lower()
    
    if 'help' == lower_user_input:
        return True
    elif 'h' == lower_user_input:
        return True

    return False
    # ==================================


def is_validated_english_sentence(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) 숫자가 포함되어 있거나,
          2) _@#$%^&*()-+=[]{}"';:\|`~ 와 같은 특수문자가 포함되어 있거나
          3) 문장부호(.,!?)를 제외하면 입력값이 없거나 빈칸만 입력했을 경우
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_english_sentence("Hello 123")
        False
        >>> mc.is_validated_english_sentence("Hi!")
        True
        >>> mc.is_validated_english_sentence(".!.")
        False
        >>> mc.is_validated_english_sentence("!.!")
        False
        >>> mc.is_validated_english_sentence("kkkkk... ^^;")
        False
        >>> mc.is_validated_english_sentence("This is Gachon University.")
        True
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = None
    alpa_count = 0
    for i in user_input:
        if 'A' <= i and i <= 'Z':
            alpa_count += 1
            continue
        elif 'a' <= i and i <= 'z':
            alpa_count += 1
            continue
        elif i == '.' or i == ',' or i == '!' or i == '?' or i == ' ':
            continue
        else:
            return False
    if alpa_count == 0:
        return False
    
    return True
    # ==================================


def is_validated_morse_code(user_input):
    """
    Input:
        - user_input : 문자열값으로 사용자가 입력하는 문자
    Output:
        - 입력한 값이 아래에 해당될 경우 False, 그렇지 않으면 True
          1) "-","."," "외 다른 글자가 포함되어 있는 경우
          2) get_morse_code_dict 함수에 정의된 Morse Code 부호외 다른 코드가 입력된 경우 ex)......
    Examples:
        >>> import morsecode as mc
        >>> mc.is_validated_morse_code("..")
        True
        >>> mc.is_validated_morse_code("..-")
        True
        >>> mc.is_validated_morse_code("..-..")
        False
        >>> mc.is_validated_morse_code(". . . .")
        True
        >>> mc.is_validated_morse_code("-- -- -- --")
        True
        >>> mc.is_validated_morse_code("!.1 abc --")
        False
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = None

    input_list = user_input.split()
    morse_code = get_morse_code_dict()
    reverse_morse_code = dict(map(reversed,morse_code.items()))

    for i in input_list:
        for j in i:
            if j == '-' or j == '.': # 공백은 확인 해봐야함
                continue
            else :
                return False
        
        if not i in reverse_morse_code:
            return False

    return True
    # ==================================



def get_cleaned_english_sentence(raw_english_sentence):
    """
    Input:
        - raw_english_sentence : 문자열값으로 Morse Code로 변환 가능한 영어 문장
    Output:
        - 입력된 영어문장에수 4개의 문장부호를 ".,!?" 삭제하고, 양쪽끝 여백을 제거한 문자열 값 반환
    Examples:
        >>> import morsecode as mc
        >>> mc.get_cleaned_english_sentence("This is Gachon!!")
        'This is Gachon'
        >>> mc.get_cleaned_english_sentence("Is this Gachon?")
        'Is this Gachon'
        >>> mc.get_cleaned_english_sentence("How are you?")
        'How are you'
        >>> mc.get_cleaned_english_sentence("Fine, Thank you. and you?")
        'Fine Thank you and you'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    result = None
    raw_english_sentence = raw_english_sentence.strip()
    cleaned_english_sentence = []
    before = None
    for i in raw_english_sentence:
        if i == '?' or i == '!' or i == '.' or i == ',':
            continue
        elif i == ' ' and before == ' ':
            continue
        else:
            cleaned_english_sentence.append(i)
        before = i
    
    return "".join(cleaned_english_sentence)
    # ==================================


def decoding_character(morse_character):
    """
    Input:
        - morse_character : 문자열값으로 get_morse_code_dict 함수로 알파벳으로 치환이 가능한 값의 입력이 보장됨
    Output:
        - Morse Code를 알파벳으로 치환함 값
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_character("-")
        'T'
        >>> mc.decoding_character(".")
        'E'
        >>> mc.decoding_character(".-")
        'A'
        >>> mc.decoding_character("...")
        'S'
        >>> mc.decoding_character("....")
        'H'
        >>> mc.decoding_character("-.-")
        'K'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    reverse_morse_code = dict(map(reversed,morse_code_dict.items()))

    return reverse_morse_code[morse_character]
    # ==================================


def encoding_character(english_character):
    """
    Input:
        - english_character : 문자열값으로 알파벳 한 글자의 입력이 보장됨
    Output:
        - get_morse_code_dict 함수의 반환 값으로 인해 변환된 모스부호 문자열값
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_character("G")
        '--.'
        >>> mc.encoding_character("A")
        '.-'
        >>> mc.encoding_character("C")
        '-.-.'
        >>> mc.encoding_character("H")
        '....'
        >>> mc.encoding_character("O")
        '---'
        >>> mc.encoding_character("N")
        '-.'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    morse_code_dict = get_morse_code_dict()
    
    return morse_code_dict[english_character]
    # ==================================


def decoding_sentence(morse_sentence):
    """
    Input:
        - morse_sentence : 문자열 값으로 모스 부호를 표현하는 문자열
    Output:
        - 모스부호를 알파벳으로 변환한 문자열
    Examples:
        >>> import morsecode as mc
        >>> mc.decoding_sentence("... --- ...")
        'SOS'
        >>> mc.decoding_sentence("--. .- -.-. .... --- -.")
        'GACHON'
        >>> mc.decoding_sentence("..  .-.. --- ...- .  -.-- --- ..-")
        'I LOVE YOU'
        >>> mc.decoding_sentence("-.-- --- ..-  .- .-. .  ..-. ")
        'YOU ARE F'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    word_list = []
    morse_sentence_list = morse_sentence.split("  ")
    for i in morse_sentence_list:
        morse_word_list = i.split(" ")
        for j in morse_word_list:
            word_list.append(decoding_character(j))
        
        word_list.append(" ")
    word_list.pop()

    return "".join(word_list)
    # ==================================


def encoding_sentence(english_sentence):
    """
    Input:
        - english_sentence : 문자열 값으로 모스 부호로 변환이 가능한 영어문장
    Output:
        - 입력된 영어문장 문자열 값을 모스부호로 변환된 알파벳으로 변환한 문자열
          단 양쪽 끝에 빈칸은 삭제한다.
    Examples:
        >>> import morsecode as mc
        >>> mc.encoding_sentence("HI! Fine, Thank you.")
        '.... ..  ..-. .. -. .  - .... .- -. -.-  -.-- --- ..-'
        >>> mc.encoding_sentence("Hello! This is CS fifty Class.")
        '.... . .-.. .-.. ---  - .... .. ...  .. ...  -.-. ...  ..-. .. ..-. - -.--  -.-. .-.. .- ... ...'
        >>> mc.encoding_sentence("We Are Gachon")
        '.-- .  .- .-. .  --. .- -.-. .... --- -.'
        >>> mc.encoding_sentence("Hi! Hi!")
        '.... ..  .... ..'
    """
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당 또는 필요에 따라 자유로운 수정
    cleaned_english_sentence = get_cleaned_english_sentence(english_sentence)
    cleaned_english_sentence = cleaned_english_sentence.upper()

    morse_list = []
    morse_code = get_morse_code_dict()
    for i in cleaned_english_sentence:
        if i != ' ':
            morse_list.append(morse_code[i])
        morse_list.append(' ')
    return ''.join(morse_list)
    # ==================================


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    playing = 1
    while playing == 1:
        input_message = input("Input your message(H - Help, 0 - Exit) : ")
        if is_help_command(input_message):
            print(get_help_message())
        elif is_validated_english_sentence(input_message):
            print(encoding_sentence(input_message))
        elif is_validated_morse_code(input_message):
            print(decoding_sentence(input_message))
        elif input_message == '0':
            playing = 0
        else:
            print("Wrong Input")

    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
