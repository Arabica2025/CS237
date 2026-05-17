# This assignment was developed for CSE 312 at the University of Washington. 
# Permission to use it is hereby granted to students registered at 
# Boston University in CS237  Spring 2025. No other use, copying, distribution, 
# or modification is permitted."

import random
import csv
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from hw07 import StudentClassifier

# Naive Bayes Spam Classifier class
class SpinnerWheelsClassifier:
        
    # def train(self, emails, labels):
    #     print("Buying two Spinner Wheels...")
    
    # def predict(self, email):
    #     # Preprocess the email
    #     prob_spam = random.random()
    #     prob_non_spam = random.random()
        
    #     # Compare the probabilities
    #     if prob_spam > prob_non_spam:
    #         return 1  # Spam
    #     else:
    #         return 0  # Non-spam
    def __init__(self):
        self.model = StudentClassifier()
        
    def train(self, emails, labels):
        self.model.train(emails, labels)
        
    def predict(self, email):
        return self.model.predict(email)
# Create the classifier and train it
emails = []
labels = []

with open('train.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:  
            emails.append(row[1])
            if row[0] == "spam":
                labels.append(1)# 1 for spam, 0 for non-spam
            else:
                labels.append(0)# 1 for spam, 0 for non-spam

classifier = SpinnerWheelsClassifier()
classifier.train(emails, labels)

total_emails = 0
true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0
with open('test.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:  
            prediction = classifier.predict(row[1])
            prediction= "spam" if prediction == 1 else "ham"
            if row[0]=='spam' and prediction == 'spam':
                true_positives+=1
            elif row[0]=='ham' and prediction == 'spam':
                false_positives+=1
            elif row[0]=='spam' and prediction == 'ham':
                false_negatives+=1
            else:
                true_negatives+=1
            total_emails+=1

print()
print("Accuracy: The overall proportion of correctly classified emails (both spam and not spam) out of all tested emails.")
print("Accuracy =", (true_positives + true_negatives) / (total_emails))
print()
print("Precision: The proportion of emails classified as spam that are actually spam (i.e., how accurate is the model when it predicts spam).")
print("Precision =", (true_positives) / (true_positives+false_positives))
print()
print("Recall:The proportion of actual spam emails that are correctly identified as spam (i.e., how well does the model capture all spam emails).")
print("Recall =",(true_positives) / (true_positives + false_negatives))
print()