@echo off
echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Starting MongoDB (make sure MongoDB is installed)
echo If MongoDB is not installed, download from: https://www.mongodb.com/try/download/community
echo.

echo Starting FastAPI server...
python run.py