import requests

def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/2762")
    assert response_body.status_code == 200
    # we use assertion to verify the response code


if __name__ == '__main__':
    main()