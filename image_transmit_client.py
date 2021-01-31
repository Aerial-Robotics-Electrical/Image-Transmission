import grpc
import ImageTransmission.image_transmit_pb2_grpc as pb2_grpc
import ImageTransmission.image_transmit_pb2 as pb2


class ImageTransmitClient(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')

        # bind the client and server
        self.stub = pb2_grpc.TransmitImageAndDataStub(self.channel)

    def get_data(self, r_id):
        message = pb2.ImageDataRequest(request_id=r_id)
        return self.stub.SendData(message)


def decode_data(response):
    if response.status_code:
        print(f'request {response.request_id} returned a non-zero status code')
    with open('tests/metadata.txt', 'w') as file:
        file.write(f'request_id: {response.request_id}\n')
        file.write(f'time_stamp: {response.time_stamp}\n')
        file.write(f'nmea_gprmc: {response.nmea_gprmc}\n')
    with open('tests/received_img.jpg', 'wb') as file:
        file.write(response.image_data)
    print(f'request {response.request_id} received')


if __name__ == '__main__':
    client = ImageTransmitClient()
    result = client.get_data(r_id='req_0')
    decode_data(result)
