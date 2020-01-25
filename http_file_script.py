import urllib3
http = urllib3.PoolManager() # Threadsafe connection manager
response = http.request('GET', 'http://localhost:8080/transfer.part')  # Get the container
filename = 'transfer_test.part'
file = open(filename, 'wb')
file.write(response.data)  # Write the container
print("wrote", filename)
file.close()
