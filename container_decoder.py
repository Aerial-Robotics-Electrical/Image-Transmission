import hashlib as hl  # Used for checksums

# Read the container file
input_file = open('transfer_test.part', 'rb')
checksum = input_file.read(40)  # Read the checksum bytes
data_header = input_file.read(100)  # Read the NMEA Message
data = input_file.read()  # Read the image data
input_file.close()

# Checksum the file
checksum_generated = hl.sha1(data_header+data).hexdigest()

# Verify file integrity
if checksum.decode('ascii') != checksum_generated:
    raise Exception('Checksum no match')

# Write the NEMA string with padding
header_file = open('files/transfer_header.txt', 'wb')
header_file.write(data_header)
header_file.close()

# Write the image data
data_file = open('files/transfer_data.ARW', 'wb')
data_file.write(data)
data_file.close()
