products=[
{"name":"Headphone","price": 100}
    ,{"name":"tablet","price": 500},
    {"name":"phone","price": 100000},
    {"name":"watch","price":5000}]

#print the items whose price is greater then 500

def affordable_products(items):
    return items["price"] > 500

aff_prod=list(filter(affordable_products,products))
print(aff_prod)