# encoding: utf-8
# @Time   : 2021/8/3 15:20
# @author : zza
# @Email  : 740713651@qq.com
# @File   : eventsourcing_demo.py
from typing import Tuple
from uuid import UUID

from eventsourcing.domain import Aggregate, event
from eventsourcing.application import Application


class World(Aggregate):
    @event('Created')
    def __init__(self, name: str) -> None:
        self.name = name
        self.history = ()

    @event('SomethingHappened')
    def make_it_so(self, what: str) -> None:
        self.history += (what,)


class Universe(Application):
    def create_world(self, name: str) -> UUID:
        world = World(name)
        self.save(world)
        return world.id

    def make_it_so(self, world_id: UUID, what: str) -> None:
        world = self._get_world(world_id)
        world.make_it_so(what)
        self.save(world)

    def get_history(self, world_id) -> Tuple:
        return self._get_world(world_id).history

    def _get_world(self, world_id) -> World:
        world = self.repository.get(world_id)
        assert isinstance(world, World)
        return world


application = Universe()

world_id = application.create_world('Earth')
application.make_it_so(world_id, 'dinosaurs')
application.make_it_so(world_id, 'trucks')
application.make_it_so(world_id, 'internet')
history = application.get_history(world_id)
assert history == ('dinosaurs', 'trucks', 'internet')
