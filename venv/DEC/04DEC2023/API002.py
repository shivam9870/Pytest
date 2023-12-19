import requests  # to use the HTTP Method

response_body = requests.get("https://restful-booker.herokuapp.com/booking/2062")
print(response_body.text)
print(response_body.headers)

# Verification
# we use Assertion -> Verify the expected result with the actual result

