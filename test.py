import re
import math

def preprocess_email(email):
    email = email.lower()
    email = re.sub(r'[^a-z\s]', '', email)
    words = email.split()
    return words

class StudentClassifier:
    def __init__(self):
        self.word_probs_spam = {}
        self.word_probs_non_spam = {}
        self.p_spam = 0.0
        self.p_non_spam = 0.0
        self.vocab = set()
    
    def train(self, emails, labels): 
        num_emails = len(emails)
        num_spam = sum(labels)
        num_non_spam = num_emails - num_spam
        
        # Priors
        self.p_spam = num_spam / num_emails
        self.p_non_spam = num_non_spam / num_emails
        
        # Dictionaries to count how many EMAILS a word appears in
        spam_word_counts = {}
        non_spam_word_counts = {}
        
        tokenized_emails = [preprocess_email(e) for e in emails]
        
        for i in range(num_emails):
            # Crucial: Use set() here so we only count a word ONCE per email
            unique_words = set(tokenized_emails[i])
            label = labels[i]
            
            for word in unique_words:
                self.vocab.add(word)
                if label == 1:
                    spam_word_counts[word] = spam_word_counts.get(word, 0) + 1
                else:
                    non_spam_word_counts[word] = non_spam_word_counts.get(word, 0) + 1
        
        # Calculate Conditional Probabilities with Laplace Smoothing
        # Formula: (Count of emails with word + 1) / (Total emails in class + 2)
        for word in self.vocab:
            self.word_probs_spam[word] = (spam_word_counts.get(word, 0) + 1) / (num_spam + 2)
            self.word_probs_non_spam[word] = (non_spam_word_counts.get(word, 0) + 1) / (num_non_spam + 2)
                
    def predict(self, email):
        words = preprocess_email(email)
        # Use distinct words from the new email as per instructions
        d_words = set(words)
        
        # Start with log of priors
        prob_s = math.log(self.p_spam)
        prob_s_bar = math.log(self.p_non_spam)
        
        for word in d_words:
            if word in self.vocab:
                # Sum of logs prevents underflow
                prob_s += math.log(self.word_probs_spam[word])
                prob_s_bar += math.log(self.word_probs_non_spam[word])
        
        return 1 if prob_s > prob_s_bar else 0

# --- Test ---
emails = ["Buy cheap meds now", "Grab lunch tomorrow", "Limited offer fast", "Meeting at noon"]
labels = [1, 0, 1, 0]

classifier = StudentClassifier()
classifier.train(emails, labels)
print(classifier.predict("Huge meds discount limited time")) # Should likely be 1

new_email = "Huge discount on meds, limited time offer!"
prediction = classifier.predict(new_email)
print("Spam" if prediction == 1 else "Not Spam")