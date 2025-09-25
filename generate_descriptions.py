import csv
from transformers import pipeline

def read_csv_headers(file_path):
    """Read headers from first line of CSV file."""
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)  # read first row
    return headers

def generate_descriptions(headers, model_name="distilbert-base-uncased"):
    """Generate short descriptions for headers using a local model."""
    # Load a small fill-mask model (runs offline after first download)
    nlp = pipeline("fill-mask", model=model_name)

    descriptions = {}
    for header in headers:
        # Simple natural language pattern
        prompt = f"{header} means [MASK]."
        try:
            result = nlp(prompt, top_k=1)[0]["sequence"]
            # Clean up the output
            desc = result.replace(prompt.replace("[MASK]", ""), "").strip()
        except Exception:
            # Fallback heuristic if model fails
            desc = f"A descriptive field for {header.lower().replace('_',' ')}"
        descriptions[header] = desc
    return descriptions

def save_output(descriptions, output_file="output.txt"):
    """Save descriptions to file."""
    with open(output_file, "w", encoding="utf-8") as f:
        for key, value in descriptions.items():
            line = f"{key} → {value}"
            print(line)  # Console output
            f.write(line + "\n")

if __name__ == "__main__":
    csv_file = "headers.csv"  # your input file
    headers = read_csv_headers(csv_file)
    descriptions = generate_descriptions(headers)
    save_output(descriptions)
