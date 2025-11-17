@echo off
echo Creating virtual environment if it does not exist...
IF NOT EXIST venv (
    python -m venv venv
)

echo Activating environment...
call venv\Scripts\activate

echo Installing requirements...
pip install -r requirements.txt

echo Starting the game...
python main.py

pause
