import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'SQRT',
    'EXPONENT',
    'IDENTIFIER',
    'EQUALS',
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EXPONENT = r'\^'
t_EQUALS = r'='
t_SQRT = r'sqrt'


# Define a rule for IDENTIFIER
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t


# Define a rule for NUMBER
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

# Define a rule for newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Invalid character '{t.value[0]}'")
    t.lexer.skip(1)



# Define a rule to ignore spaces and tabs
t_ignore = ' \t'


# Build the lexer
lexer = lex.lex()
