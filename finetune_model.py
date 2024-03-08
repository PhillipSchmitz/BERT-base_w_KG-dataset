from transformers import BertForSequenceClassification, BertTokenizer
import pandas as pd

df = pd.read_csv("train_dir/train.csv", sep=",")
labels = df["Object"].tolist()

label2id = {label: idx for idx, label in enumerate(set(labels))}
id2label = {idx: label for label, idx in label2id.items()}
encoded_labels = [label2id[label] for label in labels]

# Load your fine-tuned model
model = BertForSequenceClassification.from_pretrained("bert-base-german-cased")
tokenizer = BertTokenizer.from_pretrained("bert-base-german-cased")

# Encode a sentence
sentence = "Your input sentence here."
encoded_dict = tokenizer.encode_plus(
    sentence,
    add_special_tokens=True,
    max_length=128,
    padding="max_length",
    truncation=True,
    return_tensors="pt",
)

# Get the model's prediction
logits = model(**encoded_dict).logits
predicted_label_id = logits.argmax().item()
predicted_label = id2label[predicted_label_id]


