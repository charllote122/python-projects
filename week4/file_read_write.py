
def modify_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, "r") as f:
            lines = f.readlines()

        # Modify the content (example: add line numbers and make uppercase)
        modified_lines = [f"{i+1}: {line.strip().upper()}\n" for i, line in enumerate(lines)]

        # Write to a new file
        with open(output_file, "w") as f:
            f.writelines(modified_lines)

        print(f"Modified content has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



modify_file("input.txt", "output.txt")
