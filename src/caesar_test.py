import pytest
from caesar import caesar_encrpt, caesar_decrypt, caesar_brute


#Tests what happens with invalid input
def test_invalid():
    with pytest.raises(TypeError):
        assert caesar_encrpt(2,'hi')
    with pytest.raises(TypeError):
        assert caesar_encrpt('hi','hi')
    with pytest.raises(TypeError):
        assert caesar_encrpt(2,2)
    with pytest.raises(TypeError):
        assert caesar_encrpt('','')
    with pytest.raises(TypeError):
        assert caesar_brute(52)

#Tests limits of shift
def test_shifting():
    assert caesar_encrpt('xyz', 1) == 'yza'
    assert caesar_encrpt('abc', -1) == 'zab'
    assert caesar_encrpt('xyz', 27) == 'yza'
    assert caesar_encrpt('abc', -27) == 'zab'

#Example of sentence
def test_sentence():
    assert caesar_encrpt('A space', 26) == 'A space'
    assert caesar_encrpt('An_Underscore', 0) == 'An_Underscore'

def test_decrypt():
    cypher = caesar_encrpt('xyz', 1)
    assert cypher == 'yza'
    assert caesar_decrypt(cypher, 1) == 'xyz'

    cypher = caesar_encrpt('A space', 26)
    assert cypher == 'A space'
    assert caesar_decrypt(cypher, 26)

def test_brute():
    assert 'How did you know?' in caesar_brute(caesar_encrpt('How did you know?', 2))
    assert 'Single_Word' in caesar_brute(caesar_encrpt('Single_Word', 7))
    assert 'Bat' in caesar_brute(caesar_encrpt('Bat', 21))
