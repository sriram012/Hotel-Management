from django.db import models
from django.contrib.auth.models import User


# Floors...
class Floor(models.Model):
    floor = models.IntegerField(blank=False, unique=True)

    class Meta:
        db_table = 'List of Floors'

    def __str__(self):
        return str(self.floor) + ' floor'


# Blocks...
class BlockFloor(models.Model):
    block = models.CharField(max_length=2, blank=False)
    floor = models.ForeignKey(Floor, on_delete=models.PROTECT)

    class Meta:
        db_table = 'List of Blocks and respective Floors'

    def __str__(self):
        return self.block + ' block, ' + str(self.floor.floor) + ' floor'


# Rooms Database...
class Room(models.Model):
    block_floor = models.ForeignKey(BlockFloor, on_delete=models.PROTECT)
    room_number = models.IntegerField(blank=False)
    room_status = models.BooleanField(default=0)

    class Meta:
        db_table = "Assigned Rooms"
        order_with_respect_to = 'room_status'

    def __str__(self):
        return str(self.block_floor.block) + ', ' +\
               str(self.block_floor.floor) + ', ' + str(self.room_number)
