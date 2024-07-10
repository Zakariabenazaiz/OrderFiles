import os
from PyQt5.QtWidgets import QApplication, QFileDialog

def order_lines_alphabetically(input_file_path, output_file_path):
    # Read the content of the input file line by line
    with open(input_file_path, 'r') as input_file:
        lines = []
        for line in input_file:
            lines.append(line.strip())

    # Sort the lines alphabetically based on the first letter
    sorted_lines = sorted(lines, key=lambda x: x.lower())

    # Save the sorted lines to the output file
    with open(output_file_path, 'w') as output_file:
        for line in sorted_lines:
            output_file.write(line + '\n')

    print(f"Sorted lines saved to: {output_file_path}")

def main():
    app = QApplication([])

    # Open a file dialog to choose the input .txt file
    input_file_path, _ = QFileDialog.getOpenFileName(None, "Open Input Text File", "", "Text Files (*.txt)")

    # Check if an input file was selected
    if input_file_path:
        # Open a file dialog to choose the output .txt file
        output_file_path, _ = QFileDialog.getSaveFileName(None, "Save Sorted Text File", "", "Text Files (*.txt)")

        # Check if an output file was selected
        if output_file_path:
            order_lines_alphabetically(input_file_path, output_file_path)
        else:
            print("No output file selected.")
    else:
        print("No input file selected.")

    app.quit()

if __name__ == "__main__":
    main()