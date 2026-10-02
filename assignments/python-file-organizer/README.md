# 📘 Assignment: Python File Organizer and Text Analyzer

## 🎯 Objective

Practice Python fundamentals by writing a script that organizes files into folders and summarizes the text inside them. You will use functions, loops, conditionals, dictionaries, and file input/output to build a practical tool.

## 📝 Tasks

### 🛠️ Organize Files by Type

#### Description
Write a script that scans a folder and sorts files into categories such as Documents, Images, Code, and Other based on their file extension.

#### Requirements
Completed program should:

- Accept a folder path from the user.
- Group files by extension type.
- Create destination folders if they do not already exist.
- Move or copy each file into the matching category folder.
- Print a summary showing how many files were organized.

### 🛠️ Analyze a Text File

#### Description
Read a text file and calculate basic statistics about its content, such as word count, character count, and line count.

#### Requirements
Completed program should:

- Open a text file and read its contents.
- Count the total number of characters, words, and lines.
- Ignore empty lines when counting words if needed.
- Print a readable report like:

```python
File: sample.txt
Words: 128
Characters: 742
Lines: 15
```

### 🛠️ Combine the Features

#### Description
Create a final script that organizes files in a folder and then analyzes one or more text files in the same directory.

#### Requirements
Completed program should:

- Use the file organizer to sort files into categories.
- Identify text files in the folder after organizing.
- Report the analysis results for each text file.
- Keep the program easy to run from the terminal with a clear menu or simple input flow.
