# Python Testing Framework - > 1.Unit Test 2.Nose 3.PyTest
# Every test will start with -> test_<name>.py
# pytest -h
# pytest -k = match substrings - pytest -k "name" -> test_name.py
# pytest -v logs

# Let's create a booking using CRUD method ;

# Create a booking -> POST

import requests
import pytest


@pytest.mark.positive
def test_createBooking_positive():
    print("Create Positive Booking testcase")
    link = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=link, headers=headers, json=json)
    print(type(link))
    print(type(headers))
    print(type(json))

    # Assertions
    assert response.status_code == 200
    # get the response body and Verify the JSON and booking ID is not NONE.
    data = response.json()
    print(data)
    Booking_ID = data["bookingid"]
    Name1 = data["booking"]["firstname"]
    Name2 = data["booking"]["lastname"]
    print("Your name is :", Name1 + " " + Name2)
    print("Your Booking ID is :", Booking_ID)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Jim", "Failed : Incorrect firstname"


@pytest.mark.negative
def test_createBooking_negative():
    print("Create Positive Booking testcase")
    link = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}

    response = requests.post(url=link, headers=headers, )
    print(type(link))
    print(type(headers))

    # Assertions
    assert response.status_code == 500
