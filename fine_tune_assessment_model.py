import json
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
from datasets import Dataset
import os

def load_dataset(file_path):
    """Load the training dataset from JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Create a simple list of dictionaries for training
    train_data = []
    for item in data:
        train_data.append({
            'input': item['input'],
            'output': item['output']
        })

    return train_data

def preprocess_function(examples, tokenizer, max_input_length=512, max_target_length=512):
    """Preprocess the dataset for T5 training."""
    inputs = examples['input']
    targets = examples['output']

    model_inputs = tokenizer(inputs, max_length=max_input_length, truncation=True, padding="max_length")

    # Setup the tokenizer for targets
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(targets, max_length=max_target_length, truncation=True, padding="max_length")

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

def fine_tune_model():
    """Fine-tune the T5-small model on the assessment question generation dataset."""

    # Load dataset
    train_data = load_dataset('train.json')

    # Load tokenizer and model
    model_name = "t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # Prepare training data
    train_encodings = []
    train_labels = []

    for item in train_data:
        # Tokenize input
        input_encoding = tokenizer(item['input'], truncation=True, padding='max_length', max_length=512, return_tensors="pt")
        # Tokenize output
        label_encoding = tokenizer(item['output'], truncation=True, padding='max_length', max_length=512, return_tensors="pt")

        train_encodings.append({
            'input_ids': input_encoding['input_ids'].squeeze(),
            'attention_mask': input_encoding['attention_mask'].squeeze(),
            'labels': label_encoding['input_ids'].squeeze()
        })

    # Create dataset
    from torch.utils.data import Dataset

    class CustomDataset(Dataset):
        def __init__(self, encodings):
            self.encodings = encodings

        def __getitem__(self, idx):
            return self.encodings[idx]

        def __len__(self):
            return len(self.encodings)

    train_dataset = CustomDataset(train_encodings)

    # Training arguments
    training_args = TrainingArguments(
        output_dir="./models/assessment_model",
        num_train_epochs=3,  # Reduced for faster training
        per_device_train_batch_size=2,
        warmup_steps=100,
        weight_decay=0.01,
        logging_dir="./logs",
        logging_steps=10,
        save_strategy="epoch",
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
    )

    # Train the model
    print("Starting fine-tuning...")
    trainer.train()

    # Save the fine-tuned model
    model.save_pretrained("./models/assessment_model")
    tokenizer.save_pretrained("./models/assessment_model")

    print("Model fine-tuned and saved to ./models/assessment_model")

if __name__ == "__main__":
    # Create models directory if it doesn't exist
    os.makedirs("./models/assessment_model", exist_ok=True)
    fine_tune_model()
