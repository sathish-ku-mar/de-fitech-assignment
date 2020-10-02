from config import client

result = client.query('select * from cpu_load;')
print("Result: {0}".format(result))