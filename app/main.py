import os
import shutil


def move_file(command: str) -> None:
    # Split the command into parts
    parts = command.split()

    # Ensure the command is in the correct format (e.g., "mv <source> <destination>")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use: mv <source> <destination>.")

    _, source, destination = parts

    # Check if the source file exists
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    # Check if the destination is a directory (if it ends with a separator)
    if destination.endswith(os.sep):
        destination_dir = destination.rstrip(os.sep)
        destination_file = os.path.basename(source)
    else:
        destination_dir, destination_file = os.path.split(destination)

    # Ensure the destination directory exists (create it if it doesn't)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Use shutil.move to move the file and handle cross-filesystem moves safely
    shutil.move(source, os.path.join(destination_dir, destination_file))