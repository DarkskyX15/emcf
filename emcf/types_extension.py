
"""
非基础变量的封装，与游戏相关度更高。
"""

from .types import *
from .core import MCF
from ._utils import console, iterable
from ._exceptions import *
from ._writers import *
from ._components import builtin_components as built_cps
from typing import (
    TypeAlias, Any, Union, Self, Literal, Iterable,
    Generic, TypeVar, overload, Optional, Callable
)

__all__ = [
    'Entity',
    'Player',
    'Block',
]


# Entity Implementation
# Based on selector

class Entity(MCFVariable):
    def __init__(
        self,
        init_val: Optional['TextConvertible | Entity'] = "@s",
        void: bool = False
    ):
        MCF.useComponent('entity', built_cps.entity)
        super().__init__(init_val, void)

    def assign(self, value: 'TextConvertible | Entity'):
        if isinstance(value, str):
            Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").value(f'"{value}"')
        elif isinstance(value, Text):
            value.move(f"mem.{self._mcf_id}")
        elif isinstance(value, Entity):
            value.move(f"mem.{self._mcf_id}")
        else:
            console.error(
                MCFTypeError(
                    f"Can not assign variable of type {type(value)} to an Entity."
                )
            )

    def move(self, dist: str):
        Data.storage(MCF.storage).modify_set(dist).via(
            Data.storage(MCF.storage), f"mem.{self._mcf_id}"
        )

    def collect(self, src: str):
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").via(
            Data.storage(MCF.storage), src
        )

    def extract(self, dist: str):
        """Extract to NBT as UUID in int-array form."""
        Data.storage(MCF.storage).modify_set("call.m0").via(
            Data.storage(MCF.storage), f"mem.{self._mcf_id}"
        )
        Data.storage(MCF.storage).modify_set("call.m1").value(
            MCF.builtinSign("entity.extract")
        )
        Function(MCF.builtinSign("entity.call")).with_args(
            Data.storage(MCF.storage), "call"
        )
        Data.storage(MCF.storage).modify_set(dist).via(
            Data.storage(MCF.storage), "register"
        )

    def construct(self, src: str):
        """Construct from int-array form UUID in NBT."""
        Data.storage(MCF.storage).modify_set("cache.src").via(
            Data.storage(MCF.storage), src
        )
        Function(MCF.builtinSign("entity.construct")).call()
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").via(
            Data.storage(MCF.storage), "register"
        )

    @staticmethod
    def macro_construct(slot: str, mcf_id: str) -> 'Entity':
        temp = Entity(None, True)
        temp._mcf_id = mcf_id
        Data.storage(MCF.storage).modify_set(f"mem.{mcf_id}", True).via(
            Data.storage(MCF.storage), f"mem.$({slot})"
        )
        return temp

    @staticmethod
    def duplicate(
        init_val: Optional['TextConvertible | Entity'] = "@s",
        void: bool = False
    ) -> 'Entity':
        return Entity(init_val, void)

    def rm(self):
        Data.storage(MCF.storage).remove(f"mem.{self._mcf_id}")


    # custom methods
    
    def exec_function(
        self,
        mcfunction: Callable[..., MCFVariable | None],
        use_location: bool = False
    ) -> MCFVariable | None:
        pass
    
    # events

    def on_hurt_by_entity(
        self, 
    ) -> None:
        pass

    # static methods



# Player Implementation
# Subclass of Entity

class Player(Entity):
    pass


# Block Implementation
# Based on coordinates

class Block(MCFVariable):
    def __init__(
        self,
        init_val: 'TextConvertible | Block' = "~ ~ ~",
        void: bool = False
    ):
        MCF.useComponent('block', built_cps.block)
        super().__init__(init_val, void)
    
    def assign(self, value: 'TextConvertible | Block'):
        if isinstance(value, str):
            Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").value(r'{}')
            Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}.src").value(
                f'"{value}"'
            )
        elif isinstance(value, Text):
            Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").value(r'{}')
            value.move(f"mem.{self._mcf_id}.src")
        elif isinstance(value, Block):
            value.move(f"mem.{self._mcf_id}")
        else:
            console.error(
                MCFTypeError(
                    f"Can not assign variable of type {type(value)} to a Block."
                )
            )

    def move(self, dist: str):
        Data.storage(MCF.storage).modify_set(dist).via(
            Data.storage(MCF.storage), f"mem.{self._mcf_id}"
        )

    def collect(self, src: str):
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}").via(
            Data.storage(MCF.storage), src
        )

    @staticmethod
    def duplicate(
        init_val: 'TextConvertible | Block' = "~ ~ ~",
        void: bool = False
    ) -> 'Block':
        return Block(init_val, void)

    def rm(self):
        Data.storage(MCF.storage).remove(f"mem.{self._mcf_id}")

    def is_block(self, block_id: str):
        pass

    def query_state(self) -> None:
        """Get full data of current block."""
        Data.storage(MCF.storage).modify_set("call.m0").via(
            Data.storage(MCF.storage), f"mem.{self._mcf_id}.src"
        )
        Data.storage(MCF.storage).modify_set("call.m1").value(
            '"' + MCF.builtinSign('block.get_state') + '"'
        )
        Function(MCF.builtinSign('block.position_call')).with_args(
            Data.storage(MCF.storage), "call"
        )
        Data.storage(MCF.storage).modify_set(f"mem.{self._mcf_id}.data").via(
            Data.storage(MCF.storage), "cache.result"
        )
