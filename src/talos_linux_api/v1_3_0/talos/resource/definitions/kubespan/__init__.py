# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: resource/definitions/kubespan/kubespan.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import List

import betterproto

from ..... import common as ____common__
from .. import enums as _enums__


@dataclass(eq=False, repr=False)
class ConfigSpec(betterproto.Message):
    """ConfigSpec describes KubeSpan configuration.."""

    enabled: bool = betterproto.bool_field(1)
    cluster_id: str = betterproto.string_field(2)
    shared_secret: str = betterproto.string_field(3)
    force_routing: bool = betterproto.bool_field(4)
    advertise_kubernetes_networks: bool = betterproto.bool_field(5)
    mtu: int = betterproto.uint32_field(6)
    endpoint_filters: List[str] = betterproto.string_field(7)


@dataclass(eq=False, repr=False)
class EndpointSpec(betterproto.Message):
    """EndpointSpec describes Endpoint state."""

    affiliate_id: str = betterproto.string_field(1)
    endpoint: "____common__.NetIpPort" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class IdentitySpec(betterproto.Message):
    """
    IdentitySpec describes KubeSpan keys and address. Note: IdentitySpec is
    persisted on disk in the STATE partition, so YAML serialization should be
    kept backwards compatible.
    """

    address: "____common__.NetIpPrefix" = betterproto.message_field(1)
    subnet: "____common__.NetIpPrefix" = betterproto.message_field(2)
    private_key: str = betterproto.string_field(3)
    public_key: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class PeerSpecSpec(betterproto.Message):
    """PeerSpecSpec describes PeerSpec state."""

    address: "____common__.NetIp" = betterproto.message_field(1)
    allowed_ips: List["____common__.NetIpPrefix"] = betterproto.message_field(2)
    endpoints: List["____common__.NetIpPort"] = betterproto.message_field(3)
    label: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class PeerStatusSpec(betterproto.Message):
    """PeerStatusSpec describes PeerStatus state."""

    endpoint: "____common__.NetIpPort" = betterproto.message_field(1)
    label: str = betterproto.string_field(2)
    state: "_enums__.KubespanPeerState" = betterproto.enum_field(3)
    receive_bytes: int = betterproto.int64_field(4)
    transmit_bytes: int = betterproto.int64_field(5)
    last_handshake_time: datetime = betterproto.message_field(6)
    last_used_endpoint: "____common__.NetIpPort" = betterproto.message_field(7)
    last_endpoint_change: datetime = betterproto.message_field(8)