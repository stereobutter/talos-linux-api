# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cluster/cluster.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta
from typing import (
    TYPE_CHECKING,
    AsyncIterator,
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
class HealthCheckRequest(betterproto.Message):
    wait_timeout: timedelta = betterproto.message_field(1)
    cluster_info: "ClusterInfo" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ClusterInfo(betterproto.Message):
    control_plane_nodes: List[str] = betterproto.string_field(1)
    worker_nodes: List[str] = betterproto.string_field(2)
    force_endpoint: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class HealthCheckProgress(betterproto.Message):
    metadata: "_common__.Metadata" = betterproto.message_field(1)
    message: str = betterproto.string_field(2)


class ClusterServiceStub(betterproto.ServiceStub):
    async def health_check(
        self,
        health_check_request: "HealthCheckRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["HealthCheckProgress"]:
        async for response in self._unary_stream(
            "/cluster.ClusterService/HealthCheck",
            health_check_request,
            HealthCheckProgress,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response


class ClusterServiceBase(ServiceBase):
    async def health_check(
        self, health_check_request: "HealthCheckRequest"
    ) -> AsyncIterator["HealthCheckProgress"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_health_check(
        self, stream: "grpclib.server.Stream[HealthCheckRequest, HealthCheckProgress]"
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.health_check,
            stream,
            request,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cluster.ClusterService/HealthCheck": grpclib.const.Handler(
                self.__rpc_health_check,
                grpclib.const.Cardinality.UNARY_STREAM,
                HealthCheckRequest,
                HealthCheckProgress,
            ),
        }
