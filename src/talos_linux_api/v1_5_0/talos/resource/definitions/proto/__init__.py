# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: resource/definitions/proto/proto.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass(eq=False, repr=False)
class Mount(betterproto.Message):
    """Mount specifies a mount for a container."""

    destination: str = betterproto.string_field(1)
    type: str = betterproto.string_field(2)
    source: str = betterproto.string_field(3)
    options: List[str] = betterproto.string_field(4)