@echo off
set PYTHONPATH=.;%PYTHONPATH%
python tests/test_retrieval_qa.py
pause 