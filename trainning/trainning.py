from transformers import BertTokenizer, BertForMaskedLM, Trainer, TrainingArguments
import os

def load_data():
    # Load preprocessed data from file
    with open("trainning\cleaned_data.txt", "r") as file:
        text_data = file.read()
    return text_data

def tokenize_data(text_data, tokenizer):
    # Tokenize the text data
    return tokenizer(text_data, return_tensors="pt", truncation=True, padding=True, max_length=512)

def train_model(train_data):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForMaskedLM.from_pretrained('bert-base-uncased')

    inputs = tokenize_data(train_data, tokenizer)

    training_args = TrainingArguments(
        output_dir='./model',       # Where to save the model
        num_train_epochs=3,        # Number of epochs
        per_device_train_batch_size=16,
        logging_dir='./training/logs',   # Where to save the logs
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=inputs,  # You can add a custom dataset class here for large data
    )

    trainer.train()

if __name__ == "__main__":
    text_data = load_data()
    train_model(text_data)
