import re

# Token specification for Zara language
token_specs = [
    ('KEYWORD', r'\b(if|else|do|while|for|method)\b'),  # Zara keywords
    ('OPERATOR', r'[+\-*/=<>]'),  # Operators (+, -, *, /, =, <, >)
    ('NUMBER', r'\b\d+\b'),  # Numbers (integers)
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),  # Identifiers
    ('LPAREN', r'\('),  # Left parenthesis
    ('RPAREN', r'\)'),  # Right parenthesis
    ('LBRACE', r'\{'),  # Left brace
    ('RBRACE', r'\}'),  # Right brace
    ('SEMICOLON', r';'),  # Semicolon
    ('NEWLINE', r'\n'),  # Newline
    ('SKIP', r'[ \t]+'),  # Skip spaces and tabs
    ('MISMATCH', r'.'),  # Any other character (for errors)
]

# Compile the token specifications into a single regex pattern
token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)

# Tokenizer function
def tokenize(code):
    tokens = []  # To store the recognized tokens
    for match in re.finditer(token_regex, code):  # Find all matches using the compiled regex
        token_type = match.lastgroup  # Get the token type (from the group name)
        token_value = match.group()  # Get the actual value of the token

        # Skip over spaces and tabs
        if token_type == 'SKIP':
            continue
        # Raise an error if an unexpected character is found
        elif token_type == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {token_value} at position {match.start()}')
        else:
            tokens.append((token_type, token_value))  # Add the token (type, value) to the list

    return tokens

# Test Zara code (combined in the same file)
if __name__ == "__main__":
    zara_code = '''
    if (x == 10) {
        y = y + 1;
    } else {
        y = y - 1;
    }
    for (i = 0; i < 10; i = i + 1) {
        sum = sum + i;
    }
    do {
        z = z + 1;
    } while (z < 5);
    '''

    # Tokenize the Zara code
    try:
        tokens = tokenize(zara_code)
        print("Tokens:", tokens)  # Print the tokens
    except RuntimeError as e:
        print(e)  # Print any runtime errors (e.g., unexpected characters)
