from challenges.challenge_encrypt_message import encrypt_message
import pytest

VALID_MESSAGE = "valid"
INVALID_MESSAGE = 5

VALID_KEY = 2
INVALID_KEY = "invalid"

OOD_INDEX = 3
EVEN_INDEX = 4
OUT_OF_RANGE_INDEX = 9


def test_encrypt_message():
    assert encrypt_message(VALID_MESSAGE, 3) == "lav_di"
    assert encrypt_message(VALID_MESSAGE, 4) == "d_ilav"
    assert encrypt_message(VALID_MESSAGE, 9) == "dilav"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(VALID_MESSAGE, INVALID_KEY)

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(INVALID_MESSAGE, VALID_KEY)
