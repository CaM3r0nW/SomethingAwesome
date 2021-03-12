import pytest
import caesar as e


#Tests what happens with invalid type input
def test_invalid():
    assert e.caesar_encrpt('cat',26) == 'cat'
