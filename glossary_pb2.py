# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: glossary.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'glossary.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eglossary.proto\x12\ndictionary\"\x07\n\x05\x45mpty\"4\n\x04Term\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04term\x18\x02 \x01(\t\x12\x12\n\ndefinition\x18\x03 \x01(\t\",\n\tTermsList\x12\x1f\n\x05terms\x18\x01 \x03(\x0b\x32\x10.dictionary.Term\"0\n\x0e\x41\x64\x64TermRequest\x12\x1e\n\x04term\x18\x01 \x01(\x0b\x32\x10.dictionary.Term\"\"\n\x0f\x41\x64\x64TermResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\x0eGetTermRequest\x12\x0c\n\x04term\x18\x01 \x01(\t\"1\n\x0fGetTermResponse\x12\x1e\n\x04term\x18\x01 \x01(\x0b\x32\x10.dictionary.Term\"3\n\x11UpdateTermRequest\x12\x1e\n\x04term\x18\x01 \x01(\x0b\x32\x10.dictionary.Term\"%\n\x12UpdateTermResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x11\x44\x65leteTermRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"%\n\x12\x44\x65leteTermResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xee\x02\n\x11\x44ictionaryService\x12\x37\n\x0bGetAllTerms\x12\x11.dictionary.Empty\x1a\x15.dictionary.TermsList\x12\x42\n\x07\x41\x64\x64Term\x12\x1a.dictionary.AddTermRequest\x1a\x1b.dictionary.AddTermResponse\x12\x42\n\x07GetTerm\x12\x1a.dictionary.GetTermRequest\x1a\x1b.dictionary.GetTermResponse\x12K\n\nUpdateTerm\x12\x1d.dictionary.UpdateTermRequest\x1a\x1e.dictionary.UpdateTermResponse\x12K\n\nDeleteTerm\x12\x1d.dictionary.DeleteTermRequest\x1a\x1e.dictionary.DeleteTermResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'glossary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=30
  _globals['_EMPTY']._serialized_end=37
  _globals['_TERM']._serialized_start=39
  _globals['_TERM']._serialized_end=91
  _globals['_TERMSLIST']._serialized_start=93
  _globals['_TERMSLIST']._serialized_end=137
  _globals['_ADDTERMREQUEST']._serialized_start=139
  _globals['_ADDTERMREQUEST']._serialized_end=187
  _globals['_ADDTERMRESPONSE']._serialized_start=189
  _globals['_ADDTERMRESPONSE']._serialized_end=223
  _globals['_GETTERMREQUEST']._serialized_start=225
  _globals['_GETTERMREQUEST']._serialized_end=255
  _globals['_GETTERMRESPONSE']._serialized_start=257
  _globals['_GETTERMRESPONSE']._serialized_end=306
  _globals['_UPDATETERMREQUEST']._serialized_start=308
  _globals['_UPDATETERMREQUEST']._serialized_end=359
  _globals['_UPDATETERMRESPONSE']._serialized_start=361
  _globals['_UPDATETERMRESPONSE']._serialized_end=398
  _globals['_DELETETERMREQUEST']._serialized_start=400
  _globals['_DELETETERMREQUEST']._serialized_end=431
  _globals['_DELETETERMRESPONSE']._serialized_start=433
  _globals['_DELETETERMRESPONSE']._serialized_end=470
  _globals['_DICTIONARYSERVICE']._serialized_start=473
  _globals['_DICTIONARYSERVICE']._serialized_end=839
# @@protoc_insertion_point(module_scope)