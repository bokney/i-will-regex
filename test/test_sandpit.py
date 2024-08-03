from src.sandpit import create_pokemon_list
import pytest

def test_function_returns_list():
    result = create_pokemon_list()
    assert isinstance(result, list)