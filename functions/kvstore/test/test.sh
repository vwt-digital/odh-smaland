cp ../config.json.example config.json

pytest -o log_cli=true -o log_cli_level=INFO main_test.py

