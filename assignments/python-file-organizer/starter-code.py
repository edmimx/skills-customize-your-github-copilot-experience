from pathlib import Path


def organize_files(folder_path):
    """Sort files in a folder into categories based on file extension."""
    folder = Path(folder_path)

    # TODO: Create category folders for common file types
    # TODO: Loop through files in the folder
    # TODO: Move or copy each file to the correct directory
    # TODO: Print a summary of what was organized
    pass


def analyze_text_file(file_path):
    """Read a text file and print simple statistics."""
    path = Path(file_path)

    # TODO: Read the file contents
    # TODO: Count words, characters, and lines
    # TODO: Return or print the results
    pass


def main():
    """Run the organizer and analyzer from the terminal."""
    # TODO: Ask the user for a folder path
    # TODO: Call organize_files()
    # TODO: Ask the user which text file to analyze
    # TODO: Call analyze_text_file()
    pass


if __name__ == "__main__":
    main()
