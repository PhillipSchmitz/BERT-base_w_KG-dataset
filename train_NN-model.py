import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.models import Sequential
from keras.layers import Dense

# Load your CSV data (replace 'your_data.csv' with your actual file)
data = pd.read_csv('train_dir/train.csv')

# Extract subject and predicate columns
subjects = data['Subject'].values
predicates = data['Predicate'].values
objects = data['Object'].values

# Initialize TfidfVectorizer
vectorizer = TfidfVectorizer()

# Fit and transform subjects and predicates
encoded_subjects = vectorizer.fit_transform(subjects)
encoded_predicates = vectorizer.transform(predicates)

# Combine encoded subject and predicate vectors
combined_input = np.concatenate([encoded_subjects.toarray(), encoded_predicates.toarray()], axis=1)

# Define your model architecture
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=combined_input.shape[1]))  # Adjust input dimension
model.add(Dense(len(objects), activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(combined_input, objects, epochs=10, validation_split=0.2)

# Predict the object for a new triple
#new_encoded_subject = vectorizer.transform([your_subject])  # Encode your subject
#new_encoded_predicate = vectorizer.transform([your_predicate])  # Encode your predicate
#combined_new_input = np.concatenate([new_encoded_subject.toarray(), new_encoded_predicate.toarray()], axis=1)
#predicted_object = model.predict(combined_new_input)

#print("Predicted object:", predicted_object)