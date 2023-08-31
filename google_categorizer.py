# Imports the Google Cloud client library
from google.cloud import language_v2
import pandas as pd
import json
from tqdm import tqdm

# Instantiates a client
client = language_v2.LanguageServiceClient()

pheme = pd.read_csv('datasets\pheme2.csv')

def classify(text, verbose=True):
    """Classify the input text into categories."""

    language_client = language_v2.LanguageServiceClient()

    document = language_v2.Document(
        content=text, type_=language_v2.Document.Type.PLAIN_TEXT
    )
    response = language_client.classify_text(request={"document": document})
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print("=" * 20)
            print("{:<16}: {}".format("category", category.name))
            print("{:<16}: {}".format("confidence", category.confidence))

    return result

def parse_table(table):
    results = {}
    entry_number = 0
    for text in tqdm(table):
        try:
            result = classify(text, verbose=False)
            results[entry_number] = result
            entry_number += 1
        except Exception:
            print(f"Error processing Entry Number {entry_number}")
            entry_number += 1
    with open(write_file, "w", encoding="utf-8") as f:
        f.write(json.dumps(results, ensure_ascii=False))
    print(f"Categorized {len(table)} entries")
    return results

write_file = "pheme_categories.json"
parse_table(pheme["text"])


"""
# The text to analyze
text = "Hello, world!"
document = language_v1.types.Document(
    content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print(f"Text: {text}")
print(f"Sentiment: {sentiment.score}, {sentiment.magnitude}")"""