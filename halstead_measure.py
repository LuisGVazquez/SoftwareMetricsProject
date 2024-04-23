import math

def calculate_halstead_measure(code):
    operators = {'+', '-', '*', '/', '**', '//', '%', '<<', '>>', '&', '|', '^', '~', '<', '>', '<=', '>=', '==', '!=', '<>', 'in', 'not in', 'is', 'is not', 'and', 'or', 'not', '=', '+=', '-=', '*=', '/=', '//=', '%=', '**=', '&=', '|=', '^=', '>>=', '<<=', '**=', '//=', '|=', '&='}
    operands = set()
    total_operators = 0
    total_operands = 0

    # Count unique operators and operands
    for line in code.split('\n'):
        line = line.strip()
        if line.startswith('#'):
            continue  # skip comments
        if line:
            for word in line.split():
                if word in operators:
                    total_operators += 1
                elif word not in {'def', 'if', 'else', 'elif', 'for', 'while', 'try', 'except', 'finally', 'return', 'break', 'continue', 'pass', 'raise', 'import', 'from', 'as', 'class', 'global', 'nonlocal', 'lambda', 'del'}:
                    operands.add(word)
                    total_operands += 1

    # Calculate Halstead measures
    unique_operators = len(operators)
    unique_operands = len(operands)
    program_length = total_operators + total_operands
    vocabulary_size = unique_operators + unique_operands
    volume = program_length * math.log2(vocabulary_size)

    return volume

def calculate_halstead_measure_from_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    halstead_measure = calculate_halstead_measure(code)
    analysis = analyze_halstead_measure(halstead_measure)
    return halstead_measure, analysis

def analyze_halstead_measure(halstead_measure):
    """
    Perform analysis based on the Halstead measure.

    :param halstead_measure: The calculated Halstead measure.
    :return: Analysis of the Halstead measure.
    """
    if halstead_measure < 50:
        return "The Halstead Measure indicates extremely low program complexity.\n\nThis suggests that the program may be overly simple or lacking in functionality.\n\nTo improve: Consider reviewing the code to ensure it meets requirements and handles edge cases.\n\n\n"
    elif halstead_measure < 100:
        return "The Halstead Measure indicates low program complexity.\n\nThis suggests that the code is relatively simple and straightforward.\n\nTo improve: Continue writing clear and concise code.\n\n\n"
    elif halstead_measure < 300:
        return "The Halstead Measure indicates moderate program complexity.\n\nThis suggests that the code may contain some complexity, but it's still manageable.\n\nTo improve: Consider refactoring to break down complex operations and improve readability.\n\n\n"
    elif halstead_measure < 500:
        return "The Halstead Measure indicates relatively high program complexity.\n\nThis suggests that the code may be becoming difficult to understand and maintain.\n\nTo improve: Review the code for opportunities to simplify operations and improve clarity.\n\n\n"
    else:
        return "The Halstead Measure indicates very high program complexity.\n\nThis suggests that the code is likely difficult to understand and maintain.\n\nTo improve: Refactor the code to simplify operations and reduce cognitive load. Consider breaking down large functions or methods into smaller, more manageable ones.\n\n\n"

# Example usage:
if __name__ == "__main__":
    file_path = input("Enter the path to the Python file: ")
    halstead_measure = calculate_halstead_measure_from_file(file_path)
    print("Halstead Measure:", halstead_measure)
    
    # Perform analysis
    analysis = analyze_halstead_measure(halstead_measure)
    print("Analysis:", analysis)
