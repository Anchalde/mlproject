## Machine learning project

CSV Header Describer

This project reads column headers from a CSV file and generates short, human-readable descriptions for each. It uses DistilBERT (distilbert-base-uncased) from Hugging Face Transformers because it is a lightweight, open-source model that runs locally without cloud APIs. DistilBERT was chosen as it balances accuracy with small size, making it easy to run even on laptops without a GPU.

How to Run

Clone this repository and navigate into the project folder.

Create a virtual environment and install dependencies:

pip install -r requirements.txt


Place your CSV file in the project directory (e.g., headers.csv).

Run the script:

python generate_descriptions.py


The output will appear in the console and also be saved in output.txt.

Challenges

The main challenge was generating meaningful descriptions using a small offline model. Larger models like GPT-4 produce better text but require cloud APIs or high system resources. To overcome this, I combined a lightweight model with simple prompt-engineering and fallback rules to ensure that every header gets a reasonable description.
