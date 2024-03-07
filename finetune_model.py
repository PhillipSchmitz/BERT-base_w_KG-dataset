from transformers import BertTokenizer, TFBertForSequenceClassification
import pandas as pd
import tensorflow as tf

df = pd.read_csv("train_dir/train.csv", sep=",")
df['input_sequence'] = df['Subject'] + ' ' + df['Object']

model_name = "bert-base-german-cased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = TFBertForSequenceClassification.from_pretrained(model_name)

print(df["input_sequence"]) # Hnandling of null value columns
inputs = tokenizer(df['input_sequence'].tolist(), padding='max_length', truncation=True, max_length=128, return_tensors='tf', return_attention_mask=True)

