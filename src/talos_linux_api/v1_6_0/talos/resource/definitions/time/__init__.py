# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: resource/definitions/time/time.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta

import betterproto


@dataclass(eq=False, repr=False)
class AdjtimeStatusSpec(betterproto.Message):
    """AdjtimeStatusSpec describes Linux internal adjtime state."""

    offset: timedelta = betterproto.message_field(1)
    frequency_adjustment_ratio: float = betterproto.double_field(2)
    max_error: timedelta = betterproto.message_field(3)
    est_error: timedelta = betterproto.message_field(4)
    status: str = betterproto.string_field(5)
    constant: int = betterproto.int64_field(6)
    sync_status: bool = betterproto.bool_field(7)
    state: str = betterproto.string_field(8)


@dataclass(eq=False, repr=False)
class StatusSpec(betterproto.Message):
    """StatusSpec describes time sync state."""

    synced: bool = betterproto.bool_field(1)
    epoch: int = betterproto.int64_field(2)
    sync_disabled: bool = betterproto.bool_field(3)
