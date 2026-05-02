import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from preprocessing import clean_text


def test_clean_text_basic():
    assert clean_text("Hello, WORLD!!!") == "hello world"

def test_clean_text_numbers():
    assert clean_text("Test123") == "test"

def test_clean_text_already_clean():
    assert clean_text("hello world") == "hello world"

def test_clean_text_extra_spaces():
    assert clean_text("  HELLO  ") == "hello"
