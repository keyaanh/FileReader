import csv

def load_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [name.strip().replace('"', '').lstrip('\ufeff') for name in reader.fieldnames]
        print("Column names:", reader.fieldnames) 
        for row in reader:
            data.append(row)
    return data


def answer_question(data, question):
    question = question.lower()


    if "list" in question and ("exam" in question or "exams" in question):
        return "Exams listed: " + ", ".join([row['Exam Name'] for row in data])


    if ("how many" in question or "number of") and ("exam" in question or "exams" in question):
        unique_exams = set(row['Exam Name'] for row in data)
        return f"There are {len(unique_exams)} unique exams listed in the file."

 
    exams = [row['Exam Name'].lower() for row in data]
    exam_name = next((exam for exam in exams if exam in question), None)

    if not exam_name:
        return "Sorry, I couldn't find a matching exam in your question."


    if "minimum score required" in question:
        for row in data:
            if exam_name == row['Exam Name'].lower():
                return f"The minimum score required for {row['Exam Name']} is {row['Minimum Score Required']}."
        return "Sorry, I couldn't find the minimum score for that exam."


    if "equivalent course" in question:
        for row in data:
            if exam_name == row['Exam Name'].lower():
                return f"The equivalent course for {row['Exam Name']} is {row['Equivalent Course']}."
        return "Sorry, I couldn't find the equivalent course for that exam."


    if "credits" in question or "number of credit" in question:
        for row in data:
            if exam_name == row['Exam Name'].lower():
                return f"The number of credits for {row['Exam Name']} is {row['Number of Credit']}."
        return "Sorry, I couldn't find the number of credits for that exam."


    return "Sorry, I don't understand the question."



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
