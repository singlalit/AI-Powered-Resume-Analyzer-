import spacy
import nltk
from nltk.tokenize import word_tokenize

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined list of skills (can be expanded)
SKILL_SET = {"Python", "Java", "SQL", "Excel", "Machine Learning", "AI", "Power BI", "Communication", "Leadership"}

def extract_skills(text):
    """
    Extract skills from the given resume text.
    """
    extracted_skills = set()
    
    # Tokenize words
    words = word_tokenize(text)
    
    # Check for matching skills
    for word in words:
        if word in SKILL_SET:
            extracted_skills.add(word)

    return list(extracted_skills)

# Example usage
if __name__ == "__main__":
    sample_text = "I have experience in Python, SQL, and Machine Learning. Strong leadership and communication skills."
    print(extract_skills(sample_text))
