@echo off
python -m venv bot_env

call bot_env\Scripts\activate.bat

pip install --upgrade pip
pip install discord

python pyTICKET.py

pause
