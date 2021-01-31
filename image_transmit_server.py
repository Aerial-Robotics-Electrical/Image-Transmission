import grpc
from concurrent import futures
import time
import ImageTransmission.image_transmit_pb2_grpc as pb2_grpc
import ImageTransmission.image_transmit_pb2 as pb2


class ImageTransmitServer(pb2_grpc.TransmitImageAndDataServicer):

    def __init__(self, *args, **kwargs):
        pass

    def SendData(self, request, context):
        # get the string from the incoming request
        message = request.request_id

        # TODO set the status code (0 for success)
        st_code = 0

        # TODO add some way to grab gps data here (NMEA?)
        # Use GPRMC for compatibility
        gps_coords = '$GPRMC,042608.994,A,4025.718,N,08654.827,W,,,310121,000.0,W*6B'

        # TODO set the timestamp of the image
        time_stamp = str(time.time())

        # TODO load and set image bytes
        # FIXME use a with statement here
        file = open('tests/test_img.jpg', 'rb')
        image_bytes = file.read()
        file.close()

        response = {'request_id': message, 'status_code': st_code,
                    'time_stamp': time_stamp, 'nmea_gprmc': gps_coords,
                    'image_data': image_bytes}
        print(f'Handling request {message}')
        return pb2.ImageDataResponse(**response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    # Shouldn't be making more than 1 or 2 request at a time

    pb2_grpc.add_TransmitImageAndDataServicer_to_server(ImageTransmitServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
