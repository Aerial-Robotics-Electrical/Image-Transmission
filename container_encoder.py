import hashlib as hl  # Used for checksums

# Read the image to be added to a container
input_file = open('files/example.ARW', 'rb')
data = input_file.read()
input_file.close()

# Read the NMEA Message to be added to a container
file_header = open('files/test.txt', 'rb')
data_header = file_header.read()
file_header.close()

# Pad the NMEA Message to keep things at an even length for decoding
if len(data_header) < 100:
    print("Padding")
    while len(data_header) < 100:
        data_header += b' '

# Create the bytes for the file
whole_byte_file = data_header + data

# Checksum the file and convert to bytes using SHA1
checksum = hl.sha1(whole_byte_file).hexdigest()
checksum_bytes = checksum.encode('ascii')
# print(len(checksum_bytes))

# Write the checksum and file to the container in .part custom format
output_file = open('transfer.part', 'wb')
output_file.write(checksum_bytes + whole_byte_file)
output_file.close()
