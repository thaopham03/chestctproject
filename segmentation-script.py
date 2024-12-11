import os
import re

def clean_text(text):
    # Normalize whitespaces
    text = re.sub(r"\s+", " ", text)
    # Ensure proper segmentation
    return text.strip()

def merge_reports(input_folder, output_file):
    merged_reports = []
    for file_name in os.listdir(input_folder):
        with open(os.path.join(input_folder, file_name), 'r', encoding='utf-8') as file:
            report = clean_text(file.read())
            merged_reports.append(report)
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n###END###\n".join(merged_reports))


def main():
    pass

if __name__ == "__main__":
    main()