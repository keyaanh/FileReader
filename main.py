import csv

# Function to load the CSV file
def load_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        # Clean up column names by stripping unwanted characters like BOM and quotes
        reader.fieldnames = [name.strip().replace('"', '').lstrip('\ufeff') for name in reader.fieldnames]
        print("Column names:", reader.fieldnames)  # Print the cleaned column names
        for row in reader:
            data.append(row)
    return data


# Function to answer questions about the CSV file
def answer_question(data, question):
    question = question.lower()

    # Handle listing all exams
    if "list" in question and ("exam" in question or "exams" in question):
        return "Exams listed: " + ", ".join([row['Exam Name'] for row in data])

    # Handle questions about the total number of exams
    if ("how many" in question or "number of") and ("exam" in question or "exams" in question):
        unique_exams = set(row['Exam Name'] for row in data)  # Ensure unique exam names
        return f"There are {len(unique_exams)} unique exams listed in the file."

    # Extract possible exam name from the question
    exams = [row['Exam Name'].lower() for row in data]
    exam_name = next((exam for exam in exams if exam in question), None)

    if not exam_name:
        return "Sorry, I couldn't find a matching exam in your question."

    # Handle questions about minimum score required
    if "minimum score required" in question:
        for row in data:
            if exam_name == row['Exam Name'].lower():
                return f"The minimum score required for {row['Exam Name']} is {row['Minimum Score Required']}."
        return "Sorry, I couldn't find the minimum score for that exam."

    # Handle questions about equivalent course
    if "equivalent course" in question:
        for row in data:
            if exam_name == row['Exam Name'].lower():
                return f"The equivalent course for {row['Exam Name']} is {row['Equivalent Course']}."
        return "Sorry, I couldn't find the equivalent course for that exam."

    # Handle questions about credits
    if "credits" in question or "number of credit" in question:
        for row in data:
            if exam_name == row['Exam Name'].lower():
                return f"The number of credits for {row['Exam Name']} is {row['Number of Credit']}."
        return "Sorry, I couldn't find the number of credits for that exam."

    # Catch-all for unhandled questions
    return "Sorry, I don't understand the question."



# Main function to run the reader
def main():
    file_path = input("Enter the path to the CSV file: ")
    data = load_csv(file_path)
    print("CSV loaded successfully!")
    
    while True:
        question = input("Ask a question about the CSV file (type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        answer = answer_question(data, question)
        print(answer)

if __name__ == "__main__":
    main()
