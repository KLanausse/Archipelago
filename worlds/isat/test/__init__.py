from test.bases import WorldTestBase
from worlds.isat import InStarsAndTimeWorld


class MyGameTestBase(WorldTestBase):
    game = "In Stars And Time"
    world: InStarsAndTimeWorld