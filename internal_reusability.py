import re
from collections import defaultdict

def extract_functions_and_calls(code):
    def_pattern = re.compile(r'^\s*def (\w+)\(')
    call_pattern = re.compile(r'\b(\w+)\(')
    
    defs = set()
    calls = defaultdict(int)
    main_block = False  # Flag to track if we are inside the __name__ == "__main__" block

    for line in code.splitlines():
        # Check if the line is the start of the __name__ == "__main__" block
        if line.strip() == 'if __name__ == "__main__":':
            main_block = True
            continue

        # Match function definitions outside the main block
        def_match = def_pattern.search(line)
        if def_match and not main_block:
            defs.add(def_match.group(1))
            continue

        # If we're not in the main block, count the function calls
        if not main_block:
            for call in call_pattern.findall(line):
                calls[call] += 1

    return defs, calls

def calculate_internal_reusability(filepath):
    with open(filepath, 'r') as file:
        code = file.read()

    defs, calls = extract_functions_and_calls(code)
    
    n = len(defs)  # Number of unique functions/methods defined
    e = sum(calls[func] for func in defs if func in calls)  # Number of internal function/method calls
    
    reusability = e - n + 1  # Calculate reusability
    
    # Analysis
    if reusability < 0:
        analysis = "Internal reusability is negative, indicating a lack of reuse or excessive duplication.\n\nThis suggests that the codebase may suffer from high coupling and low cohesion.\n\nTo improve: Focus on identifying opportunities for code reuse and reducing duplication. Consider modularizing code and promoting separation of concerns.\n\n\n"
    elif reusability == 0:
        analysis = "Internal reusability is minimal, suggesting little to no internal code reuse.\n\nThis may lead to code redundancy and increased maintenance efforts.\n\nTo improve: Consider refactoring code to promote reuse and modularity. Identify common functionalities and extract them into reusable components.\n\n\n"
    elif reusability < 10:
        analysis = "Internal reusability is moderate, indicating some degree of code reuse.\n\nThis suggests that the codebase has begun to embrace reuse but may still have room for improvement.\n\nTo improve: Continue identifying and promoting reusable components. Encourage developers to leverage existing functionalities rather than reinventing the wheel.\n\n\n"
    else:
        analysis = "Internal reusability is high, suggesting extensive internal code reuse.\n\nThis indicates a strong emphasis on modular design and reuse of existing components.\n\nTo improve: Keep up the good work in promoting code reuse and modularity. Encourage documentation and sharing of reusable components among developers.\n\n\n"
    
    return reusability, analysis

def main():
    filepath = input("Enter the path to the Python file to analyze: ")
    reusability, analysis = calculate_internal_reusability(filepath)
    print(f"Internal Reusability (rG): {reusability}")
    print(analysis)

if __name__ == "__main__":
    main()
