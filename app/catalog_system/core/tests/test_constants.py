from catalog_system.core.constants import Constants


def test_constants_structure():
    class Numbers(Constants):
        class Meta:
            hidden_constants = ["INFINITE"]

        ONE = 1
        TWO = 2
        THREE = 3
        INFINITE = "inf"

    assert list(Numbers) == [1, 2, 3]
    assert Numbers.__dict__ == {"ONE": 1, "TWO": 2, "THREE": 3, "INFINITE": "inf"}  # noqa: E501;

    # Checking regular value exists in the Constant
    assert Numbers.ONE == 1
    assert 1 in Numbers

    # Checking that hidden is accesible through
    # the Constant, but is not part of the exposed list
    assert Numbers.INFINITE == "inf"
    assert "inf" not in Numbers

    # define another class to make sure metaclass state isn't persisted
    class Letters(Constants):
        class Meta:
            hidden_constants = ["ALL"]

        A = "a"
        B = "b"
        C = "c"
        ALL = "all"

    assert "a" in Letters
    assert "all" not in Letters
    assert Letters.__dict__ == {"A": "a", "B": "b", "C": "c", "ALL": "all"}
