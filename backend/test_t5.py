import asyncio
from app.services.t5_service import t5_service

async def test_t5_service():
    """Test the T5 service for quiz question generation."""
    print("Testing T5 service for quiz question generation...")

    try:
        # Test generating questions for different skills and difficulties
        skills = ["algorithms", "data-structures", "programming"]
        difficulties = ["easy", "medium", "hard"]

        for skill in skills:
            for difficulty in difficulties:
                print(f"\nGenerating questions for {skill} at {difficulty} difficulty...")
                questions = await t5_service.generate_quiz_questions(skill, difficulty, 2)

                print(f"Generated {len(questions)} questions:")
                for i, q in enumerate(questions, 1):
                    print(f"  {i}. {q.question}")
                    print(f"     Options: {q.options}")
                    print(f"     Correct: {q.correct_answer}")
                    print(f"     Topic: {q.topic}")

    except Exception as e:
        print(f"Error testing T5 service: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_t5_service())
