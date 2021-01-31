# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image-transmit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='image-transmit.proto',
  package='ImageTransmission',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14image-transmit.proto\x12\x11ImageTransmission\"&\n\x10ImageDataRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\"x\n\x11ImageDataResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x12\n\ntime_stamp\x18\x03 \x01(\t\x12\x12\n\nnmea_gprmc\x18\x04 \x01(\t\x12\x12\n\nimage_data\x18\x05 \x01(\x0c\x32o\n\x14TransmitImageAndData\x12W\n\x08SendData\x12#.ImageTransmission.ImageDataRequest\x1a$.ImageTransmission.ImageDataResponse\"\x00\x62\x06proto3'
)




_IMAGEDATAREQUEST = _descriptor.Descriptor(
  name='ImageDataRequest',
  full_name='ImageTransmission.ImageDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='ImageTransmission.ImageDataRequest.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=81,
)


_IMAGEDATARESPONSE = _descriptor.Descriptor(
  name='ImageDataResponse',
  full_name='ImageTransmission.ImageDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='ImageTransmission.ImageDataResponse.request_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_code', full_name='ImageTransmission.ImageDataResponse.status_code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='ImageTransmission.ImageDataResponse.time_stamp', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nmea_gprmc', full_name='ImageTransmission.ImageDataResponse.nmea_gprmc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_data', full_name='ImageTransmission.ImageDataResponse.image_data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=203,
)

DESCRIPTOR.message_types_by_name['ImageDataRequest'] = _IMAGEDATAREQUEST
DESCRIPTOR.message_types_by_name['ImageDataResponse'] = _IMAGEDATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageDataRequest = _reflection.GeneratedProtocolMessageType('ImageDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEDATAREQUEST,
  '__module__' : 'image_transmit_pb2'
  # @@protoc_insertion_point(class_scope:ImageTransmission.ImageDataRequest)
  })
_sym_db.RegisterMessage(ImageDataRequest)

ImageDataResponse = _reflection.GeneratedProtocolMessageType('ImageDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEDATARESPONSE,
  '__module__' : 'image_transmit_pb2'
  # @@protoc_insertion_point(class_scope:ImageTransmission.ImageDataResponse)
  })
_sym_db.RegisterMessage(ImageDataResponse)



_TRANSMITIMAGEANDDATA = _descriptor.ServiceDescriptor(
  name='TransmitImageAndData',
  full_name='ImageTransmission.TransmitImageAndData',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=205,
  serialized_end=316,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendData',
    full_name='ImageTransmission.TransmitImageAndData.SendData',
    index=0,
    containing_service=None,
    input_type=_IMAGEDATAREQUEST,
    output_type=_IMAGEDATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSMITIMAGEANDDATA)

DESCRIPTOR.services_by_name['TransmitImageAndData'] = _TRANSMITIMAGEANDDATA

# @@protoc_insertion_point(module_scope)