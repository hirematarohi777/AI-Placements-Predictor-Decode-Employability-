import json
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments
from torch.utils.data import Dataset
import os

class QuizDataset(Dataset):
    def __init__(self, data, tokenizer, max_length=512):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        
        # Create input prompt
        input_text = f"Generate quiz question for {item['skill']} topic {item['topic']} difficulty {item['difficulty']}"
        
        # Create target output
        target_text = json.dumps({
            "question": item["question"],
            "options": item["options"],
            "correct_answer": item["correct_answer"],
            "explanation": item["explanation"]
        })

        # Tokenize
        inputs = self.tokenizer(input_text, max_length=self.max_length, padding="max_length", truncation=True, return_tensors="pt")
        targets = self.tokenizer(target_text, max_length=self.max_length, padding="max_length", truncation=True, return_tensors="pt")

        return {
            "input_ids": inputs["input_ids"].flatten(),
            "attention_mask": inputs["attention_mask"].flatten(),
            "labels": targets["input_ids"].flatten()
        }

def train_model():
    # Load custom dataset
    with open("custom_dataset.json", "r") as f:
        data = json.load(f)

    # Initialize tokenizer and model
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    model = T5ForConditionalGeneration.from_pretrained("t5-small")

    # Create dataset
    dataset = QuizDataset(data, tokenizer)

    # Training arguments
    training_args = TrainingArguments(
        output_dir="./quiz_model",
        num_train_epochs=3,
        per_device_train_batch_size=2,
        save_steps=500,
        save_total_limit=2,
        logging_steps=100,
        remove_unused_columns=False
    )

    # Create trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer
    )

    # Train
    trainer.train()
    
    # Save model
    model.save_pretrained("./quiz_model")
    tokenizer.save_pretrained("./quiz_model")
    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train_model()