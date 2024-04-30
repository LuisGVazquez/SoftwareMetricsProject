import ast
import math

def calculate_halstead_measure(code):
    operator_counts = {}
    operand_counts = {}
    
    # Parse the code
    tree = ast.parse(code)

    # Traverse the abstract syntax tree to count operators and operands
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp):
            operator = type(node.op).__name__
            operator_counts[operator] = operator_counts.get(operator, 0) + 1
        elif isinstance(node, ast.Name):
            operand = node.id
            operand_counts[operand] = operand_counts.get(operand, 0) + 1
        elif isinstance(node, ast.Constant):
            operand = node.value
            operand_counts[operand] = operand_counts.get(operand, 0) + 1

    # Calculate Halstead measures
    total_operators = sum(operator_counts.values())
    total_operands = sum(operand_counts.values())
    unique_operators = len(operator_counts)
    unique_operands = len(operand_counts)
    program_length = total_operators + total_operands
    vocabulary_size = unique_operators + unique_operands
    volume = program_length * math.log2(vocabulary_size)

    return volume, operator_counts, operand_counts

def calculate_halstead_measure_from_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    halstead_measure, operator_counts, operand_counts = calculate_halstead_measure(code)
    analysis = analyze_halstead_measure(halstead_measure)
    return halstead_measure, operator_counts, operand_counts, analysis


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
    halstead_measure, operator_counts, operand_counts, analysis = calculate_halstead_measure_from_file(file_path)
    print("Halstead Measure:", halstead_measure)
    print("Operator Counts:", operator_counts)
    print("Operand Counts:", operand_counts)
    print("Analysis:", analysis)
