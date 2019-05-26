import string, re 

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    # Your code here
    fill = fill_in(formula)
    for f in fill:
        if valid(f):
            return f   
    return None
    
def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    #letters = ''.join(list(set([elem for elem in formula if elem.isalpha()]))) #should be a string
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    # find all n letter combinations of digits where n is the number of letters in our formula
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)
  
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False