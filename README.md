# python-unittest-presentation
Presentation and examples of Unit Testing in Python

# Usage

## Sieve of Eratosthenes

```bash
$ cd code/sieve

$ # Manual Tests
$ python3 main.py (1|2|3)

$ # Unit Tests
$ python3 -m unittest sieve_test.py
```

## Simple Tagger

```bash
$ cd code/nlp

$ pip3 install -r requirements.txt

$ # Unittest
$ python3 -m unittest tests/unittest_nlp.py

$ # nose2
$ nosetests tests/unittest_nlp.py

$ # py.test
$ py.test tests/pytest_nlp.py
$ py.test tests/unittest_nlp.py
```

## Battleship

```bash
$ cd code/exercise

$ # Unit Tests
$ python3 -m unittest discover
```

