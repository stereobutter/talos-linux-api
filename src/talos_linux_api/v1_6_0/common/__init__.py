# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: common/common.proto
# plugin: python-betterproto
import builtins
from dataclasses import dataclass
from typing import List

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf

from ..google import rpc as _google_rpc__


class Code(betterproto.Enum):
    FATAL = 0
    LOCKED = 1
    CANCELED = 2


class ContainerDriver(betterproto.Enum):
    CONTAINERD = 0
    CRI = 1


class ContainerdNamespace(betterproto.Enum):
    NS_UNKNOWN = 0
    NS_SYSTEM = 1
    NS_CRI = 2


@dataclass(eq=False, repr=False)
class Error(betterproto.Message):
    code: "Code" = betterproto.enum_field(1)
    message: str = betterproto.string_field(2)
    details: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class Metadata(betterproto.Message):
    """Common metadata message nested in all reply message types"""

    hostname: str = betterproto.string_field(1)
    """hostname of the server response comes from (injected by proxy)"""

    error: str = betterproto.string_field(2)
    """
    error is set if request failed to the upstream (rest of response is
    undefined)
    """

    status: "_google_rpc__.Status" = betterproto.message_field(3)
    """error as gRPC Status"""


@dataclass(eq=False, repr=False)
class Data(betterproto.Message):
    metadata: "Metadata" = betterproto.message_field(1)
    bytes: builtins.bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class DataResponse(betterproto.Message):
    messages: List["Data"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Empty(betterproto.Message):
    metadata: "Metadata" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class EmptyResponse(betterproto.Message):
    messages: List["Empty"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Url(betterproto.Message):
    full_path: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class PemEncodedCertificateAndKey(betterproto.Message):
    crt: bytes = betterproto.bytes_field(1)
    key: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class PemEncodedKey(betterproto.Message):
    key: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class NetIp(betterproto.Message):
    ip: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class NetIpPort(betterproto.Message):
    ip: bytes = betterproto.bytes_field(1)
    port: int = betterproto.int32_field(2)


@dataclass(eq=False, repr=False)
class NetIpPrefix(betterproto.Message):
    ip: bytes = betterproto.bytes_field(1)
    prefix_length: int = betterproto.int32_field(2)
