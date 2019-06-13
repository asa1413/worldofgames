FROM python:3
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install forex_python flask

Copy CurrencyRouletteGame.py /CurrencyRouletteGame.py
Copy MainGame.py /MainGame.py
copy asa.txt /asa.txt
Copy templates /templates
Copy GuessGame.py /GuessGame.py
Copy Live.py /Live.py
Copy MainScores.py /MainScores.py
Copy MemoryGame.py /MemoryGame.py
Copy Score.py /Score.py
Copy Utils.py /Utils.py

CMD python MainScores.py
