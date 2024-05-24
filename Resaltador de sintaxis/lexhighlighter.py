import re
import os

def receive_cpp_file(path):
    try:
        with open(path, 'r') as file:
            cpp_code = file.read()
        return cpp_code
    except FileNotFoundError:
        print(f"FileNotFoundError: No such file or directory: '{path}'")
        return None

def extract_keywords(cpp_code):
    if cpp_code is None:
        return []
    
    keywords = [
        '#include', 'int', 'float', 'char', 'double', 'long', 'if', 'else', 'switch', 'case', 'for', 'while', 'do',
        'break', 'continue', 'return', 'void', 'const', 'static', 'public', 'private', 'protected',
        'class', 'struct', 'union', 'enum', 'typename', 'namespace', 'using', 'virtual',
        'override', 'this', 'nullptr', 'true', 'false', 'new', 'delete', 'try', 'catch', 'throw',
        'template', 'friend', 'inline', 'operator', 'explicit', 'constexpr', 'mutable',
        'register', 'volatile', 'asm', 'export', 'import', 'sizeof', 'dynamic_cast',
        'static_cast', 'reinterpret_cast', 'const_cast', 'typeid', 'decltype', 'noexcept', 
        '(', ')', '[', ']', '{', '}', ';', ',', '.', '::', '->', '?', ':'
    ]
    
    operators = [
        '+', '-', '*', '/', '%', '++', '--', '=', '+=', '-=', '*=', '/=', '%=', '==', '!=', '>', '<', '>=', '<=',
        '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', '<<=', '>>=', '&=', '|=', '^='
    ]

    comment_patterns = [
        r'//.*',
        r'/\*(.|\n)*?\*/' 
    ]

    escaped_keywords = [re.escape(keyword) for keyword in keywords]
    escaped_operators = [re.escape(operator) for operator in operators]

    all_patterns = comment_patterns + escaped_keywords + escaped_operators
    pattern = r'(' + '|'.join(all_patterns) + r')'
    
    matches = re.findall(pattern, cpp_code)
    return matches

path_to_cpp_file = 'lexcat.cpp'

cpp_code = receive_cpp_file(path_to_cpp_file)
keywords = extract_keywords(cpp_code)
print(keywords)
