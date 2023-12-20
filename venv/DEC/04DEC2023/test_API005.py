import pytest
import requests


def test_sample():
    assert 4 == 4


def test_sample2():
    assert 5 == 5


def test_Getdata():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1690")
    assert response_body.status_code == 200
    # we use assertion to verify the response code

    data = response_body.json()

    # Assertion
    # VERIFICATION OF KEYS
    assert 'firstname' in data, "Incorrect firstname"
    assert 'lastname' in data, "LastName key is present"
    # VERIFICATION OF DATA
    assert data['firstname'] == "Jim", "Incorrect first name"
    assert data['lastname'] == "Brown", "Incorrect last name"
    # to verify the check-in
    assert data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect message"
