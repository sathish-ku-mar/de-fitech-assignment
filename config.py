from influxdb import InfluxDBClient
API_ENDPOINT = "https://ftx.com/api/"
FTX_API_KEY = '5h_f5GqjEBtKMTp_GfUNWgKSVGRumwiwN7KYkYA0'
FTX_SECRET_KEY = 'GNoNhNb33Day3Ulmk08K08dCvEvINuyXR_-kE3gz'

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'test')
client.create_database('test')
