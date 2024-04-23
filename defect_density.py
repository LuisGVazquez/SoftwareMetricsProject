import re

def calculate_defect_density(known_defects, product_size):
    """
    Calculate the defect density based on the number of known defects and product size.
    
    Arguments:
    known_defects -- Number of known defects.
    product_size -- Size of the product (measured in lines of code or function points).
    
    Returns:
    Defect_density -- A float representing the defect density.
    Analysis -- A string containing the analysis message.
    """
    try:
        defect_density = known_defects / product_size
        
        # Analysis
        if defect_density < 0.001:
            analysis = "The defect density is extremely low.\n\nThis indicates a very high level of code quality with minimal defects.\n\nTo improve: Keep up the good work in maintaining a low defect rate.\n\n\n"
        elif defect_density < 0.01:
            analysis = "The defect density is low.\n\nThis suggests that the code quality is good, but there is still room for improvement.\n\nTo improve: Continue focusing on quality assurance and testing processes.\n\n\n"
        elif defect_density < 0.05:
            analysis = "The defect density is moderate.\n\nThis indicates a moderate level of defects relative to the product size.\n\nTo improve: Consider reviewing the code for potential areas of improvement and increasing testing efforts.\n\n\n"
        elif defect_density < 0.1:
            analysis = "The defect density is relatively high.\n\nThis suggests that there may be significant room for improvement in code quality.\n\nTo improve: Prioritize identifying and addressing defects, reviewing development processes, and enhancing testing strategies.\n\n\n"
        else:
            analysis = "The defect density is very high.\n\nThis indicates a significant number of defects relative to the product size.\n\nTo improve: Take immediate action to identify and address defects, review development and testing processes, and consider implementing stricter quality control measures.\n\n\n"
        
        return defect_density, analysis
    except ZeroDivisionError:
        print("Error: Division by zero. Please make sure product_size is not zero.")
        return None, None

# Example usage:
if __name__ == "__main__":
    known_defects = int(input("Enter the number of known defects: "))
    product_size = int(input("Enter the product size (measured in lines of code or function points): "))

    defect_density, analysis = calculate_defect_density(known_defects, product_size)
    if defect_density is not None:
        print("The defect density is:", defect_density)
        print(analysis)
