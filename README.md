# Metrics Tool

This Metrics Tool is a Python application built using the Tkinter library, designed to calculate various software metrics for Python codebases. It provides insights into code size, cyclomatic complexity, internal reusability, portability, defect density, and Halstead measure.

## Prerequisites

- Python 3.x installed on your system
- pip package manager

## Installation

1. Clone this repository to your local machine.

2. Navigate to the project directory.

3. Create a virtual environment (optional but recommended):

```
python3 -m venv venv
```

4. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

5. Install dependencies:
```
pip install -r requirements.txt
```
## Usage

1. Run the Metrics Tool application:

```
python gui.py
```

2. Use the navigation bar to select the metric you want to calculate.
3. Follow the on-screen instructions to input any required parameters.
4. Click on the corresponding button to calculate the metric.
5. Analyze the results or view combined metrics for the entire codebase.
6. You can clear results, analyze them, or exit the application using the provided buttons.

## Creating an Executable File

You can create an executable file using PyInstaller to run the Metrics Tool without needing to install Python or any dependencies. Follow these steps:

1. Install PyInstaller:

```
pip install pyinstaller
```

2. Navigate to the project directory.

3. Create the executable file:

```
pyinstaller --onefile --noconsole gui.py
```

4. The executable file will be generated in the `dist` directory.

## Additional Information

- This application uses the Tkinter library for the GUI.
- Various software metrics algorithms are implemented in separate Python files.
- The tool provides both individual metric calculations and a combined view for better analysis.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
