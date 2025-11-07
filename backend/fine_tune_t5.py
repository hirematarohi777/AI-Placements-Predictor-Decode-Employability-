import json
from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
from torch.utils.data import Dataset
import torch

class QuestionDataset(Dataset):
    def __init__(self, data, tokenizer, max_length=512):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        input_text = f"Generate quiz question for {item['skill']} difficulty {item['difficulty']}"
        target_text = json.dumps({
            "question": item["question"],
            "options": item["options"],
            "correct_answer": item["correct_answer"],
            "topic": item["topic"]
        })
        
        inputs = self.tokenizer(input_text, max_length=self.max_length, truncation=True, padding="max_length", return_tensors="pt")
        targets = self.tokenizer(target_text, max_length=self.max_length, truncation=True, padding="max_length", return_tensors="pt")
        
        return {
            "input_ids": inputs["input_ids"].flatten(),
            "attention_mask": inputs["attention_mask"].flatten(),
            "labels": targets["input_ids"].flatten()
        }

# Sample training data
training_data = [
    {
        "skill": "data-structures",
        "difficulty": "easy",
        "question": "What is the time complexity of accessing an element in an array by index?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
        "correct_answer": "O(1)",
        "topic": "arrays"
    },
    {
        "skill": "data-structures", 
        "difficulty": "medium",
        "question": "Which data structure uses LIFO principle?",
        "options": ["Queue", "Stack", "Tree", "Graph"],
        "correct_answer": "Stack",
        "topic": "stacks"
    }
]

def fine_tune_model():
    # Load pre-trained model
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    
    # Create dataset
    dataset = QuestionDataset(training_data, tokenizer)
    
    # Training arguments
    training_args = TrainingArguments(
        output_dir="./models/assessment_model",
        num_train_epochs=3,
        per_device_train_batch_size=2,
        save_steps=500,
        save_total_limit=2,
        logging_steps=100,
    )
    
    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer,
    )
    
    # Fine-tune
    trainer.train()
    
    # Save model
    model.save_pretrained("./models/assessment_model")
    tokenizer.save_pretrained("./models/assessment_model")

if __name__ == "__main__":
    fine_tune_model()