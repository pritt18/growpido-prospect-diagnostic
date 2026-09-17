@echo off
echo ======================================================================
echo GROWPIDO PROSPECT TO DIAGNOSTIC ENGINE - TRACK B
echo ======================================================================
echo.
echo 1. Running automated unit test suite...
python -m pytest tests/
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Tests failed! Exiting.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo 2. Running CLI Pipeline for Noor Sweid...
python cli.py --subject "Noor Sweid" --url "https://www.linkedin.com/in/noorsweid"

echo.
echo 3. Launching Interactive Streamlit Dashboard...
streamlit run app.py
