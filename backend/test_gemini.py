import asyncio
import json
import os

from app.services.gemini_service import gemini_service

async def main():
    print("Starting Gemini quiz generation test...")
    qs = await gemini_service.generate_quiz_questions("probability", "medium", 2)
    # Convert Pydantic models to dicts for readable printing
    out = []
    for q in qs:
        if hasattr(q, 'model_dump'):
            out.append(q.model_dump())
        elif hasattr(q, 'dict'):
            out.append(q.dict())
        else:
            out.append(q.__dict__)
    print(json.dumps(out, indent=2, default=str))

if __name__ == '__main__':
    asyncio.run(main())
