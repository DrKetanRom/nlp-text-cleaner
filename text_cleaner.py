import re
import pandas as pd

# A comprehensive list of core English stopwords to keep the script self-contained
STOPWORDS = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", 
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", 
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", 
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", 
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", 
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", 
    "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", 
    "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", 
    "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
])

def fetch_sample_data():
    """
    Simulates fetching a text dataset.
    For an external dataset, swap this with: pd.read_csv('URL_OR_PATH_TO_CSV')
    """
    print("-> Loading sample dataset...")
    data = {
        'review_id': [1, 2, 3, 4, 5],
        'original_text': [
            "I absolutely loved this product! It worked flawlessly and saved me hours of work.",
            "Horrible experience. The item arrived broken and customer service was completely unhelpful.",
            "It's okay, does the job. Nothing spectacular but not bad either for the price.",
            "Wow, simply amazing! Exceeded all my expectations. Highly recommend to everyone!",
            "Don't waste your money. It stopped working after just two days of normal use."
        ]
    }
    return pd.DataFrame(data)

def clean_text(text):
    """
    Cleans a text string by lowercasing, removing punctuation, 
    tokenizing, and removing stopwords.
    """
    if not isinstance(text, str):
        return ""
        
    # 1. Lowercase
    text = text.lower()
    
    # 2. Tokenize & Remove Punctuation
    # re.findall extracts strings of alphanumeric characters, splitting on punctuation & spaces
    tokens = re.findall(r'\b\w+\b', text)
    
    # 3. Remove Stopwords
    cleaned_tokens = [word for word in tokens if word not in STOPWORDS]
    
    # Re-join tokens into a space-separated string for easy CSV storage
    return " ".join(cleaned_tokens)

def main():
    # Step 1: Fetch data
    df = fetch_sample_data()
    
    # Step 2: Clean text
    print("-> Cleaning and tokenizing text data...")
    df['cleaned_text'] = df['original_text'].apply(clean_text)
    
    # Step 3: Save to CSV
    output_filename = 'cleaned_dataset.csv'
    df.to_csv(output_filename, index=False)
    print(f"-> Success! Cleaned data saved to '{output_filename}'")
    
    # Display a quick preview in the console
    print("\n=== Data Preview ===")
    print(df[['original_text', 'cleaned_text']].to_string(index=False))

if __name__ == "__main__":
    main()
