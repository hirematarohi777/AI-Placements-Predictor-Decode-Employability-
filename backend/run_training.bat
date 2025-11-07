@echo off
echo Starting T5 Model Training...
echo Installing required packages...
pip install torch transformers datasets

echo Training model...
python train_model.py

echo Training completed!
pause