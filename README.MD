# Image Transmission System

This repository will handle image transmission requests and send images, GPS coordinates, and timestamps from the UAS 
to the ground station. Requests and responses are handled through gRPC. 

## Requirements
Use the 'requirements.txt' file to install the Python 3 packages needed. If you prefer to do it manually,
you will need 2 packages.

1. grpcio
2. aiogrpc
3. grpcio-tools

## To compile a new protobuf file
Use the following command to compile new .proto files into the requisite Python classes:

_Use `python` or `python3` depending on your system_

`python3 -m grpc_tools.protoc --proto_path=./protos --python_out=./ImageTransmission 
--grpc_python_out=./ImageTransmission <proto file>`

Also, you will need to edit the `ImageTransmission/image_transmit_pb2_grpc.py` file's import. This is a well-documented
problem with no expected fix. Change the import to `ImageTransmission.image_transmit_pb2` for the code to function.