import requests

# FIRST= Creating the Token
def CreateToken():
    # print("Just Creating the token for you")
    url_link = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response_body = requests.post(url=url_link, headers=headers, json=json_payload)
    data = response_body.json()
    token = data["token"]
    print(token)
    return token

# SECOND = Creating the Booking ID
def createBooking():
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
    return Booking_ID

# THIRD = Creating the full update using PUT method

def test_put_request():
    # Booking ID and Token number
    link = "https://restful-booker.herokuapp.com/booking/"
    Booking_ID = str(createBooking())
    Put_link = link + Booking_ID
    Cookie_value = "token=" + CreateToken()
    headers = {"Content-Type": "application/json",
               "Cookie": Cookie_value,
                # "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
               }
    print(headers)
    json = {
        "firstname": "Nikhil",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=Put_link, headers=headers, json=json)

    # Assertions
    assert response.status_code == 200
    # get the response body and Verify the JSON and booking ID is not NONE.
    data = response.json()
    assert data["firstname"] == "Nikhil", "Failed : Incorrect firstname"


def test_delete_ID():
    link = "https://restful-booker.herokuapp.com/booking/"
    Booking_ID = str(createBooking())
    Put_link = link + Booking_ID
    Cookie_value = "token=" + CreateToken()
    headers = {"Content-Type": "application/json",
               "Cookie": Cookie_value,
               # "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
               }
    print(headers)

    response = requests.delete(url=Put_link, headers=headers)

    # Assertions
    assert response.status_code == 201