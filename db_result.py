from config import client

result = client.query('select * from orders;')
print("Result: {0}".format(result))