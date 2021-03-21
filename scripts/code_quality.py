import os


def check_import_order():
    os.system("isort --check ./covid_cajamar/ --skip __init__.py --gitignore --dont-follow-links --verbose")


def check_code_formatting():
    os.system("black --check ./covid_cajamar/ --exclude __init__.py --verbose")


def sort_import_order():
    os.system("isort ./covid_cajamar/ ./tests/ --skip __init__.py --gitignore --dont-follow-links --verbose")


def do_code_formatting():
    os.system("black ./covid_cajamar/ ./tests/ --exclude __init__.py --verbose")


def linter():
    os.system("pylama ./covid_cajamar/ ./tests/")


def run_tests():
    os.system("pytest ./tests/ --verbose --color=yes --code-highlight=yes")
