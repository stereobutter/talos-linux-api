# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: time/time.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from .. import common as _common__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class TimeRequest(betterproto.Message):
    """The response message containing the ntp server"""

    server: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class Time(betterproto.Message):
    metadata: "_common__.Metadata" = betterproto.message_field(1)
    server: str = betterproto.string_field(2)
    localtime: datetime = betterproto.message_field(3)
    remotetime: datetime = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class TimeResponse(betterproto.Message):
    """The response message containing the ntp server, time, and offset"""

    messages: List["Time"] = betterproto.message_field(1)


class TimeServiceStub(betterproto.ServiceStub):
    async def time(
        self,
        betterproto_lib_google_protobuf_empty: "betterproto_lib_google_protobuf.Empty",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "TimeResponse":
        return await self._unary_unary(
            "/time.TimeService/Time",
            betterproto_lib_google_protobuf_empty,
            TimeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def time_check(
        self,
        time_request: "TimeRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "TimeResponse":
        return await self._unary_unary(
            "/time.TimeService/TimeCheck",
            time_request,
            TimeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class TimeServiceBase(ServiceBase):
    async def time(
        self,
        betterproto_lib_google_protobuf_empty: "betterproto_lib_google_protobuf.Empty",
    ) -> "TimeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def time_check(self, time_request: "TimeRequest") -> "TimeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_time(
        self,
        stream: "grpclib.server.Stream[betterproto_lib_google_protobuf.Empty, TimeResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.time(request)
        await stream.send_message(response)

    async def __rpc_time_check(
        self, stream: "grpclib.server.Stream[TimeRequest, TimeResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.time_check(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/time.TimeService/Time": grpclib.const.Handler(
                self.__rpc_time,
                grpclib.const.Cardinality.UNARY_UNARY,
                betterproto_lib_google_protobuf.Empty,
                TimeResponse,
            ),
            "/time.TimeService/TimeCheck": grpclib.const.Handler(
                self.__rpc_time_check,
                grpclib.const.Cardinality.UNARY_UNARY,
                TimeRequest,
                TimeResponse,
            ),
        }
