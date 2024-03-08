from transformers import BertForSequenceClassification, BertTokenizer
import pandas as pd
import torch

df = pd.read_csv("train_dir/train.csv", sep=",")
labels = df["Object"].tolist()

label2id = {label: idx for idx, label in enumerate(set(labels))}
id2label = {idx: label for label, idx in label2id.items()}
encoded_labels = [label2id[label] for label in labels]

# Load your fine-tuned model
model = BertForSequenceClassification.from_pretrained("bert-base-german-cased")
tokenizer = BertTokenizer.from_pretrained("bert-base-german-cased")

# Example: Fine-tuning loop
optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)
loss_fn = torch.nn.CrossEntropyLoss()

for epoch in range(3):
    for batch in dataloader:  # Iterate over your data batches
        inputs, labels = batch
        optimizer.zero_grad()
        outputs = model(**inputs).logits
        loss = loss_fn(outputs, labels)
        loss.backward()
        optimizer.step()