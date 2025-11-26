import re

LETTERS = re.compile(r'[a-zA-Z]')
WHITESPACE = re.compile(r'\s')
NUMBERS = re.compile(r'\d')

def tokenizer(input):
    tokens = []
    current = 0
    while current < len(input):
        char = input[current]
        if char == '(' or char == ')':
            tokens.append({
                'type': 'paren',
                'value': char
            })
            current += 1
            continue
        if LETTERS.match(char):
            value = ''
            while LETTERS.match(char):
                value += char
                current += 1
                if current >= len(input):
                    break
                char = input[current]
            tokens.append({
                'type': 'name',
                'value': value
            })
            continue
        if WHITESPACE.match(char):
            current += 1
            continue
        if NUMBERS.match(char):
            value = ''
            while NUMBERS.match(char):
                value += char
                current += 1
                if current >= len(input):
                    break
                char = input[current]
            tokens.append({
                'type': 'number',
                'value': value
            })
            continue
        raise TypeError(f"Unknown char: '{char}'")
    return tokens