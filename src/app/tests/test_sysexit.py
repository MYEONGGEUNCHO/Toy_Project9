# Run multiple tests
'''
pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. 
More generally, it follows standard test discovery rules.
'''
import pytest

def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()