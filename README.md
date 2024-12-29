# Rename Files and Directories

This Python script renames files and directories by applying specific transformations to their names. It ensures that file and directory names are standardized, readable, and free from unwanted characters.

## Features

The script performs the following transformations:

1. **Spaces and Hyphens:**
   - Replaces spaces (` `) and hyphens (`-`) with underscores (`_`).

2. **Uppercase to Lowercase:**
   - Converts all uppercase letters to lowercase.

3. **Accents Removal:**
   - Removes accents from characters (e.g., `é` becomes `e`, `ñ` becomes `n`).

4. **Duplicate Underscores:**
   - Replaces multiple consecutive underscores (`__`) with a single underscore (`_`).

5. **Trailing Underscore Before Extension:**
   - Removes trailing underscores (`_`) directly before a file extension (e.g., `file_name_.pdf` becomes `file_name.pdf`).

6. **Dot Preservation for Extensions:**
   - Preserves the dot (`.`) in file extensions, ensuring it is not replaced by an underscore (e.g., `.pdf`, `.txt`).

7. **Recursive Renaming:**
   - Applies all the above transformations to all files and directories in the specified root directory, including subdirectories.

## Usage

1. Clone or download the script to your local machine.
2. Run the script using Python:

   ```bash
   python rename_files.py
   ```

3. Enter the directory path when prompted. The script will recursively rename all files and directories within the specified path.

## Example

Input:

```
My Directory/
├── My File.PDF
├── sub-folder/
│   ├── another File_.txt
│   └── spaced file - example.html
```

Output:

```
my_directory/
├── my_file.pdf
├── sub_folder/
│   ├── another_file.txt
│   └── spaced_file_example.html
```

## Notes

- Ensure you have appropriate permissions to rename files and directories in the specified path.
- Use the script with caution, as renaming cannot be undone automatically.

