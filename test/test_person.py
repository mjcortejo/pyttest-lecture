import pytest
from package.person import Person

def test_initialize():
    person = Person("a", "b", "c", 100, "male", "09/27/1920")
    assert person.first_name == "a"
    assert person.middle_name == "b"
    assert person.last_name == "c"
    assert person.age == 100
    assert person.gender == "male"
    assert person.birthday == "09/27/1920"

def test_invalid_name():
    with pytest.raises(Exception):
        person = Person("a", "b", "c", "100s", "male", "09/27/1920")

def test_invalid_gender():
    with pytest.raises(Exception, match=r"Invalid Gender notmale"):
        person = Person("a", "b", "c", 100, "notmale", "09/27/1920")
