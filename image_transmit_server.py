import grpc
from concurrent import futures
import time
import image_transmit_pb2_grpc as pb2_grpc
import image_transmit_pb2 as pb2


class ImageTransmitServer(pb2_grpc.TransmitTimeAndGPSServicer):

    def __init__(self, *args, **kwargs):
        pass

    def SendData(self, request, context):
        # get the string from the incoming request
        message = request.request_id
        result = {'request_id': message, 'timestamp': str(time.time()), 'gpscoords': 'some coords here'}
        print(f'Handling request {message}')
        return pb2.TimeGPSResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TransmitTimeAndGPSServicer_to_server(ImageTransmitServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
