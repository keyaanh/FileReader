# CSV Exam Query Script

This script allows users to interactively query a CSV file containing information about exams, such as minimum scores, equivalent courses, and credits. Users can also ask general questions like how many exams are listed or request a list of all exam names.

---

## Features
- **Load CSV File:** The script prompts the user to input the file path to a CSV file.
- **Interactive Query:** Users can ask questions about the data in natural language.
- **Supported Queries:**
  - List all exam names.
  - Count the total number of unique exams.
  - Retrieve the minimum score required for a specific exam.
  - Find the equivalent course for a specific exam.
  - Get the number of credits for a specific exam.

---

## Prerequisites
- Python 3.x
- The CSV file should have the following column names:
  - `Exam Name`
  - `Minimum Score Required`
  - `Number of Credit`
  - `Equivalent Course`

---

## Installation
1. Clone the repository or download the script.
2. Install Python 3.x if not already installed.
3. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
4. Install dependencies (if any). Currently, no external libraries are required.

---

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Enter the path to your CSV file when prompted.
3. Interact with the script by asking questions. Example questions:
   - "What's the total number of exams?"
   - "What is the minimum score required for AP Biology?"
   - "List all the exams."
   - "What is the equivalent course for AP Physics C: Mechanics?"

4. To exit the interactive session, type `exit`.

---

## Example Interaction
```bash
Enter the path to the CSV file: /path/to/Course_list_export.csv
Column names: ['Exam Name', 'Minimum Score Required', 'Number of Credit', 'Equivalent Course']
CSV loaded successfully!
Ask a question about the CSV file (type 'exit' to quit): How many exams are listed in the file?
There are 30 unique exams listed in the file.

Ask a question about the CSV file (type 'exit' to quit): What is the minimum score required for AP Calculus AB?
The minimum score required for AP Calculus AB is 3.

Ask a question about the CSV file (type 'exit' to quit): exit
```

---

## Customization
You can extend the script by adding more query types or refining the natural language processing logic in the `answer_question` function.

---

## Troubleshooting
- **CSV Load Error:** Ensure the CSV file exists and has the correct column names.
- **Unrecognized Questions:** If the script doesn't understand a question, try rephrasing it or checking the `answer_question` function logic.

---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the script.

