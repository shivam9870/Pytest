# API
# Request Lib
import requests  # to use the HTTP Method


def main():
    # GET- URL
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/2062")
    # print(response_body.text)
    # print(response_body.status_code)

    if response_body.status_code == 200:
        print("TC#1 is done successful")
    else:
        print("TC#1 is not done successful")

if __name__ == "__main__":
    main()
