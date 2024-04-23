import re

def calculate_portability(ET, ER):
    """
    Calculate the portability of software based on the given resources.
    
    Arguments:
    ET -- Resources needed to move the system to the target environment.
    ER -- Resources needed to create the system for the resident environment.
    
    Returns:
    Portability -- A float representing the portability score.
    Analysis -- A string containing the analysis message.
    """
    try:
        portability = 1 - (ET / ER)
        
        # Analysis
        if portability > 0.9:
            analysis = "The portability score is very high, indicating strong potential for portability.\n\nThis suggests that the system is highly adaptable and can be easily deployed across different environments.\n\nTo improve: Continue ensuring that the system is designed and developed with portability in mind, considering factors such as platform independence and compatibility."
        elif portability > 0.7:
            analysis = "The portability score is high, suggesting good potential for portability.\n\nThis indicates that the system can be deployed across different environments with minimal modifications.\n\nTo improve: Regularly assess and mitigate dependencies on specific environments or technologies to enhance portability."
        elif portability > 0.5:
            analysis = "The portability score is moderate, indicating some level of portability but with room for improvement.\n\nThis suggests that while the system can be deployed across different environments, there may be some challenges or limitations.\n\nTo improve: Identify and address potential barriers to portability, such as platform-specific dependencies or tightly coupled components."
        else:
            analysis = "The portability score is low, suggesting limited portability.\n\nThis indicates that the system may have significant dependencies on specific environments or technologies, making it difficult to deploy in different contexts.\n\nTo improve: Prioritize efforts to refactor and redesign the system to increase portability. Consider adopting standard protocols, formats, and architectures to facilitate easier deployment across different environments."
        
        return portability, analysis
    except ZeroDivisionError:
        print("Error: Division by zero. Please make sure ER is not zero.")
        return None, None

# Example usage:
if __name__ == "__main__":
    ET = float(input("Enter the resources needed to move the system to the target environment (ET): "))
    print("ET input:", ET)  # Debugging statement
    ER_input = input("Enter the resources needed to create the system for the resident environment (ER): ")

    # Use regular expression to filter out non-numeric characters
    ER = float(re.sub("[^0-9]", "", ER_input))
    print("ER input:", ER)  # Debugging statement

    portability_score, analysis = calculate_portability(ET, ER)
    if portability_score is not None:
        print("The portability score is:", portability_score)
        print(analysis)
