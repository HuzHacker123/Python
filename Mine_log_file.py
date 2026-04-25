def check_log_for_python(log_file_path):
    """
    Checks if a log file contains the word 'python' (case-insensitive).

    Args:
        log_file_path: The path to the log file.

    Returns:
        True if 'python' is found, False otherwise.
    """
    try:
        with open(log_file_path, 'r') as file:
            for line_number,line in enumerate(file,1):
                # Check for 'python' (case-insensitive) in the current line
                if "python" in line.lower():
                    print(f"Found 'python' in line {line_number}")
                    return True  # Found it, no need to check the rest of the file
    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}' was not found.")
        return False
    except IOError as e:
        print(f"Error reading file: {e}")
        return False

    return False # Reached the end of the file without finding 'python'

# --- Example Usage ---
# 1. Create a dummy log file for testing (optional, you can skip this part)
try:
    with open("my_app.log", "w") as f:
        f.write("2026-02-05 10:00:00 [INFO] Starting application.\n")
        f.write("2026-02-05 10:05:00 [ERROR] Failed to run python script.\n")
        f.write("2026-02-05 10:10:00 [INFO] Operation complete.\n")
except IOError as e:
    print(f"Could not create dummy log file: {e}")

# 2. Specify the path to your log file
file_to_check = "my_app.log" # Replace with your actual file path

# 3. Run the function and print the result
if check_log_for_python(file_to_check):
    print(f"The log file '{file_to_check}' DOES contain the word 'python'.")    
else:
    print(f"The log file '{file_to_check}' DOES NOT contain the word 'python'.")
