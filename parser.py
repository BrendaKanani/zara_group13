import re

# Define Token Specification
token_specification = [
    ('NUMBER', r'\d+'),  # Integer literals
    ('IDENTIFIER', r'[A-Za-z_]\w*'),  # Identifiers
    ('OPERATOR', r'[+\-*/=><]'),  # Operators
    ('LPAREN', r'\('),  # Left parenthesis
    ('RPAREN', r'\)'),  # Right parenthesis
    ('LBRACE', r'\{'),  # Left brace
    ('RBRACE', r'\}'),  # Right brace
    ('SEMICOLON', r';'),  # Semicolon
    ('KEYWORD', r'\b(if|else|for|do|while|void|int|float|return)\b'),  # Keywords
    ('COMMA', r','),  # Comma for parameter separation
    ('WHITESPACE', r'\s+'),  # Skip whitespace
]

# Lexical Analysis
def tokenize(code):
    tokens = []
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'WHITESPACE':
            continue
        tokens.append((kind, value))
    return tokens

# Recursive Descent Parser for Zara Grammar
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, token_type):
        token = self.current_token()
        if token and token[0] == token_type:
            self.pos += 1
        else:
            raise SyntaxError(f"Expected {token_type}, got {token}")

    def parse(self):
        while self.current_token():
            self.parse_declaration_or_statement()

    def parse_declaration_or_statement(self):
        token = self.current_token()
        if token[1] in ('int', 'float', 'void'):
            self.parse_method_declaration()
        else:
            self.parse_statement()

    def parse_method_declaration(self):
        print("Parsing method declaration...")
        # Parse return type (int, float, void)
        self.eat('KEYWORD')
        # Parse method name (identifier)
        self.eat('IDENTIFIER')
        # Parse parameters
        self.eat('LPAREN')
        if self.current_token()[0] != 'RPAREN':
            self.parse_parameters()
        self.eat('RPAREN')
        # Parse method body
        self.eat('LBRACE')
        self.parse_statements()
        self.eat('RBRACE')
        print("Method declaration parsed successfully.")

    def parse_parameters(self):
        self.eat('IDENTIFIER')  # First parameter
        while self.current_token() and self.current_token()[0] == 'COMMA':
            self.eat('COMMA')
            self.eat('IDENTIFIER')  # Next parameter

    def parse_if(self):
        self.eat('KEYWORD')  # 'if'
        self.eat('LPAREN')  # '('
        self.parse_expression()  # Condition
        self.eat('RPAREN')  # ')'
        self.eat('LBRACE')  # '{'
        self.parse_statements()  # if block
        self.eat('RBRACE')  # '}'
        if self.current_token() and self.current_token()[1] == 'else':
            self.eat('KEYWORD')  # 'else'
            self.eat('LBRACE')  # '{'
            self.parse_statements()  # else block
            self.eat('RBRACE')  # '}'

    def parse_for(self):
        self.eat('KEYWORD')  # 'for'
        self.eat('LPAREN')  # '('
        self.parse_expression()  # Initialization
        self.eat('SEMICOLON')  # ';'
        self.parse_expression()  # Condition
        self.eat('SEMICOLON')  # ';'
        self.parse_expression()  # Increment
        self.eat('RPAREN')  # ')'
        self.eat('LBRACE')  # '{'
        self.parse_statements()  # for block
        self.eat('RBRACE')  # '}'

    def parse_do_while(self):
        self.eat('KEYWORD')  # 'do'
        self.eat('LBRACE')  # '{'
        self.parse_statements()  # do block
        self.eat('RBRACE')  # '}'
        self.eat('KEYWORD')  # 'while'
        self.eat('LPAREN')  # '('
        self.parse_expression()  # Condition
        self.eat('RPAREN')  # ')'
        self.eat('SEMICOLON')  # ';'

    def parse_expression(self):
        # A simple expression parser
        if self.current_token()[0] == 'IDENTIFIER':
            self.eat('IDENTIFIER')
            if self.current_token() and self.current_token()[0] == 'OPERATOR':
                self.eat('OPERATOR')
                self.eat('NUMBER')

    def parse_statements(self):
        while self.current_token() and self.current_token()[0] != 'RBRACE':
            self.parse_statement()

    def parse_statement(self):
        token = self.current_token()
        if token[1] == 'if':
            self.parse_if()
        elif token[1] == 'for':
            self.parse_for()
        elif token[1] == 'do':
            self.parse_do_while()
        else:
            self.parse_expression()

# Testing Zara Code
if __name__ == '__main__':
    zara_code = """
    void myFunction(x, y) {
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
    }

    int anotherFunction(a, b) {
        return a + b;
    }
    """

    tokens = tokenize(zara_code)
    print("Tokens:", tokens)

    parser = Parser(tokens)
    try:
        parser.parse()
        print("Parsing completed successfully.")
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
