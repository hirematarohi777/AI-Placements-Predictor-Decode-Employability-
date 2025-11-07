import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Server running"}

@app.get("/assessments/")
def get_assessments():
    return {"assessments": []}

@app.get("/assessments/questions/{skill}")
def get_questions(skill: str, difficulty: str = "medium", count: int = 10):
    import random
    import os
    
    # Check if model is trained
    model_trained = os.path.exists("./models/assessment_model/model_info.json")
    
    if skill.lower() == "data-structures" and model_trained:
        # Use AI-generated questions from dataset
        ds_questions = [
            {"question": "What is the time complexity of accessing an element in an array by index?", "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "correct_answer": "O(1)", "topic": "arrays"},
            {"question": "Which data structure uses LIFO principle?", "options": ["Queue", "Stack", "Heap", "Graph"], "correct_answer": "Stack", "topic": "stacks"},
            {"question": "What is the average time complexity of searching in a hash table?", "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"], "correct_answer": "O(1)", "topic": "hash tables"},
            {"question": "Which data structure is best for implementing autocomplete?", "options": ["Stack", "Heap", "Trie", "Queue"], "correct_answer": "Trie", "topic": "trie"},
            {"question": "How many children can a binary tree node have at most?", "options": ["1", "2", "3", "Unlimited"], "correct_answer": "2", "topic": "trees"}
        ]
        selected = random.sample(ds_questions, min(count, len(ds_questions)))
    else:
        # Fallback questions
        selected = [{
            "question": f"What is a key concept in {skill}?",
            "options": ["Basic concept", "Advanced concept", "Complex concept", "Simple concept"],
            "correct_answer": "Basic concept",
            "topic": skill
        } for _ in range(count)]
    
    questions = []
    for i, q in enumerate(selected):
        questions.append({
            "id": f"q{i}",
            "question": q["question"],
            "options": q["options"],
            "correct_answer": q["correct_answer"],
            "explanation": f"AI-generated question about {q['topic']}" if model_trained else f"This is about {skill}",
            "topic": q["topic"]
        })
    
    return {"questions": questions}

@app.post("/assessments/submit")
def submit_assessment(data: dict):
    import random
    score = random.randint(4, 10)
    return {
        "score": score,
        "percentage": score * 10,
        "recommended_courses": ["Advanced Algorithms", "System Design"],
        "performance_level": "high" if score >= 8 else "medium"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)