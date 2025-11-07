# AI Learner Backend

FastAPI backend with MongoDB for the AI-powered learning platform.

## Features

- JWT Authentication with role-based access
- MongoDB integration with Motor (async)
- Gemini AI integration for quiz generation
- ML-based placement prediction
- RESTful API endpoints
- Docker containerization

## Setup

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables in `.env`:
```
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=ailearner
SECRET_KEY=your-secret-key-here
GEMINI_API_KEY=your-gemini-api-key-here
```

3. Start MongoDB (or use Docker):
```bash
docker run -d -p 27017:27017 --name mongodb mongo:7.0
```

4. Run the application:
```bash
python run.py
```

### Docker Deployment

1. Start services:
```bash
docker-compose up -d
```

2. Access API at `http://localhost:8000`

## API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user

### Assessments
- `GET /assessments/questions/{skill}` - Get quiz questions
- `POST /assessments/submit` - Submit assessment

### Progress
- `GET /progress/analyze` - Analyze student progress

### Learning Path
- `POST /learning-path/generate` - Generate personalized learning path
- `GET /learning-path/current` - Get current learning path

### Predictions
- `GET /predictions/calculate` - Calculate placement probability

### Feedback
- `POST /feedback/send` - Send feedback (professors only)
- `GET /feedback/received` - Get received feedback
- `GET /feedback/sent` - Get sent feedback (professors only)

### Analytics
- `GET /analytics/batch` - Batch performance analytics
- `GET /analytics/student/{student_id}` - Individual student analytics

## Database Collections

- `users` - User accounts and profiles
- `assessments` - Quiz submissions and scores
- `student_progress` - Progress tracking
- `learning_paths` - Personalized study plans
- `predictions` - Placement predictions
- `feedback` - Professor-student feedback
- `analytics` - Batch performance data
- `quiz_questions` - Generated quiz questions

## AI Integration

- **Gemini API**: Dynamic quiz question generation
- **ML Models**: Placement probability prediction using scikit-learn
- **RAG System**: Personalized learning recommendations

## Optional: Hugging Face Transformers (CodeBERT / DialoGPT)

This repo provides optional integrations with Hugging Face `transformers` to
use models like `microsoft/codebert-base` (for code embeddings/analysis) and
`microsoft/DialoGPT-medium` (for conversational lesson generation). These
are optional — the code will fall back to Gemini-based generation when the
transformers library or models are not installed.

If you want to enable the Transformers paths locally, install the packages
and models. On Windows, installing `torch` is platform-specific — follow the
official instructions at https://pytorch.org/get-started/locally/.

Example (PowerShell):

```powershell
# Create venv and activate (if not already done)
python -m venv .venv; .\.venv\Scripts\Activate.ps1

# Install transformers and torch (choose the torch build that matches your CUDA)
pip install transformers
# For CPU-only Windows builds, you can install a CPU wheel or use:
# pip install torch --index-url https://download.pytorch.org/whl/cpu

# Then run the backend as usual
& ".\.venv\Scripts\python.exe" "backend\run.py"
```

Notes:
- If `transformers` or the specific model weights are missing, the services
	will gracefully fall back to using the Gemini model configured by
	`GEMINI_API_KEY`.
