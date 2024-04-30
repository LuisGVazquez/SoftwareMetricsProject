import ast

class ComplexityVisitor(ast.NodeVisitor):
    """
    AST node visitor that counts the nodes contributing to cyclomatic complexity.
    """
    def __init__(self):
        super().__init__()
        self.complexity = 1  # Start with a base complexity of 1

    def visit_If(self, node):
        # Each 'if' and 'elif' statement increases complexity
        self.complexity += 1
        # This also counts 'elif' parts because each 'elif' is an 'if' node
        self.generic_visit(node)

    def visit_For(self, node):
        # Each 'for' loop increases complexity
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        # Each 'while' loop increases complexity
        self.complexity += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        # Boolean operations ('and', 'or') increase complexity
        # This does not double-count conditions already accounted for in visit_If
        self.complexity += len(node.values) - 1
        self.generic_visit(node)
        
def calculate_cyclomatic_complexity_ast(filepath):
    """
    Calculate the cyclomatic complexity of the given Python file using AST parsing.
    
    :param filepath: Path to the Python file to analyze.
    :return: A tuple containing the calculated cyclomatic complexity and analysis.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read(), filename=filepath)
            
        visitor = ComplexityVisitor()
        visitor.visit(tree)
        complexity = visitor.complexity
        
        # Analysis
        if complexity < 5:
            analysis = "The cyclomatic complexity is very low, indicating simple code with linear control flow.\n\nThis suggests that the code is straightforward and easy to understand.\n\nTo improve: Maintain clarity by writing self-documenting code and avoiding unnecessary branching.\n\n\n"
        elif complexity < 10:
            analysis = "The cyclomatic complexity is low, suggesting relatively simple code.\n\nThis indicates that the codebase is manageable and not overly complex.\n\nTo improve: Consider refactoring to break down complex functions into smaller, more manageable ones.\n\n\n"
        elif complexity < 15:
            analysis = "The cyclomatic complexity is moderate, indicating moderately complex code.\n\nThis suggests that the codebase is becoming more intricate and may require additional attention.\n\nTo improve: Refactor complex functions to improve readability and maintainability.\n\n\n"
        elif complexity < 20:
            analysis = "The cyclomatic complexity is high, suggesting complex code that may be hard to understand and maintain.\n\nThis indicates that the codebase is quite complex and may benefit from restructuring.\n\nTo improve: Refactor the code to reduce complexity. Break down functions and optimize control flow.\n\n\n"
        else:
            analysis = "The cyclomatic complexity is very high, indicating highly complex code with convoluted control flow.\n\nThis suggests that the codebase is overly complex and challenging to maintain.\n\nTo improve: It's crucial to refactor the code extensively. Simplify logic, reduce nesting, and modularize complex parts.\n\n\n"
        
        return complexity, analysis
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None, None
    except SyntaxError as e:
        print(f"Syntax error in the file: {e}")
        return None, None

# Example usage if the file is run directly
if __name__ == "__main__":
    filepath = input("Enter the path to the Python file to analyze: ")
    complexity, analysis = calculate_cyclomatic_complexity_ast(filepath)
    if complexity is not None:
        print(f"The cyclomatic complexity of {filepath} is {complexity}")
        print(f"Analysis: {analysis}")
    else:
        print("Cannot calculate cyclomatic complexity for the given file.")
