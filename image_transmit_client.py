import grpc
import image_transmit_pb2_grpc as pb2_grpc
import image_transmit_pb2 as pb2


class ImageTransmitClient(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))

        # bind the client and server
        self.stub = pb2_grpc.TransmitTimeAndGPSStub(self.channel)

    def get_data(self, id):
        message = pb2.TimeGPSRequest(request_id=id)
        return self.stub.SendData(message)


if __name__ == '__main__':
    client = ImageTransmitClient()
    result = client.get_data(id='testid')
    print(f'{result}')
