#!/usr/bin/env python
import pytest

def test_answer(cmdopt):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type":
        print("second")
    else:
        print('cmdopt中default的值异常')

if __name__ == "__main__":
    pytest.main()
