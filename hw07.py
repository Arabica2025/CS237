# You can import many Python libraries, except numpy
import re
import math

# Function to preprocess and clean the emails
def preprocess_email(email):
    # Convert to lowercase
    email = email.lower()
    # Remove non-alphabetical characters (punctuation, numbers, etc.)
    email = re.sub(r'[^a-z\s]', '', email)
    # Split into words
    words = email.split()
    return words

# Naive Bayes Spam Classifier class
class StudentClassifier:
    # You can add more attributes to this class
    def __init__(self):
        # Probabilities for each word: P(w_i | S)
        self.word_probs_spam = {}

        # Probabilities for each word: P(w_i | ~S)
        self.word_probs_non_spam = {}

        # Likelihood of spam based on the total number of spams from the total number of e-mails
        self.p_spam = 0.0

        # Likelihood of non-spam based on the total number of non-spams from the total number of e-mails
        self.p_non_spam = 0.0

        # Vocabulary is the set of possible words
        self.vocab = set()
    
    # emails: list of email contents
    # labels: corresponding list of 0 (non-spam) or 1 (spam)
    def train(self, emails, labels): 
        # Calculate total number of emails
        total_emails = len(emails)
        # Separate spam and non-spam emails   
        s = []
        s_bar = []    
        for idx, labl in enumerate(labels):
            if labl == 1:
                s.append(idx)
            else:
                s_bar.append(idx)
        # Compute the likelihood for spam and non-spam   
        # Likelihood of spam based on the total number of spams from the total number of e-mails: P[S]
        self.p_spam = len(s) / total_emails
        
        # Likelihood of non-spam based on the total number of non-spams from the total number of e-mails: P[~S]
        self.p_non_spam = len(s_bar) / total_emails
        
        # Calculate the conditional probabilities for each word: P(w_i | S) and P(w_i | ~S)
        # tokenize the email to get the word from the email
        # list of tokenized emails (1 email in each idx of list)
        # [[tokenized each email],[tokenized each email],...]
        tokenized = [preprocess_email(email) for email in emails]
        
        # vocab list update
        for words in tokenized:
            for w in words:
                self.vocab.add(w) # self.vocab is a set so does not include the repeated words in each email
        
        # count words
        s_count = {}
        s_bar_count = {}
        
        for i in s: # s: []
            rm_repeat_w_in_tknzd = set(tokenized[i]) # in list, there are redundant words, so we need to remove those repeating words
            for word in rm_repeat_w_in_tknzd: # in each idx because it has list of words for each email
                s_count[word] = s_count.get(word,0)+1
            

                
        for i in s_bar:
            rm_repeat_w_in_tknzd = set(tokenized[i])
            for word in rm_repeat_w_in_tknzd:
                s_bar_count[word] = s_bar_count.get(word, 0)+1
                

                
        # condiitonal prob
        # P(w_i | S)
        self.word_probs_spam = {}
        # P(w_i | ~S)
        self.word_probs_non_spam = {}

        total_s = len(s)
        total_s_bar = len(s_bar)
        # conditional probability for each word in self.vocab
        for w in self.vocab:
            self.word_probs_spam[w] = (s_count.get(w,0) + 1) / (total_s + 2)
            self.word_probs_non_spam[w] = (s_bar_count.get(w,0)+1) / (total_s_bar + 2)
            
                
    # Preprocess each new e-mail
    # This is the only function we will call
    def predict(self, email):
        # Preprocess the email
        words = preprocess_email(email)
        # distinct words
        d_words = set(words) # removes the repeated words in each email
        # Compute the likelihood for being spam and non-spam using the words from the new e-mail
        # Review Problem 5 from the homework
        # use math.log to initialize the prior probabilities of an e-mail being spam and non-spam.
        prob_s = math.log(self.p_spam)
        prob_s_bar = math.log(self.p_non_spam)
        
        # implemented formula from Problem 2-(b)
        # log addition instead of multiplication
        for word in d_words:
            if word in self.vocab:
                prob_s += math.log(self.word_probs_spam[word])
                prob_s_bar += math.log(self.word_probs_non_spam[word])
                
        
                
       
        # Compare the probabilities
        if prob_s > prob_s_bar:
            return 1  # Spam
        else:
            return 0  # Non-spam

# Example usage:
# Let's say you have a small dataset of emails and their labels
emails = [
    "Buy cheap meds now",  # Spam
    "Hey, let's grab lunch tomorrow",  # Non-spam
    "Limited time offer, act fast!",  # Spam
    "Are you coming to the meeting?"  # Non-spam
]
labels = [1, 0, 1, 0]  # 1 for spam, 0 for non-spam

# Create the classifier and train it
classifier = StudentClassifier()
classifier.train(emails, labels)

# Now predict for a new email
new_email = "Huge discount on meds, limited time offer!"
prediction = classifier.predict(new_email)
print("Spam" if prediction == 1 else "Not Spam")
