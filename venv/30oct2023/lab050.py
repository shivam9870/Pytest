#dict

phonebook={"batman":123456,"superman":456789,"deadpool": 696969}

print(len(phonebook))
print(phonebook["batman"])
print(phonebook["deadpool"])
#You can access the elements by KEY only.

phonebook2=dict(batman=1221,flash=5252,GB=4587)
print(phonebook2)
print(phonebook2["flash"])
print(phonebook2.get("flash"))
# print(phonebook2["4587"])-> ERROR You can access by only by KEY

data={'a':1,'b':2,'c':21,'a':45}
print(data) #the latest value will display i.e a=45


