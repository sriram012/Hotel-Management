from django.db import models
from Customers.models import Customers


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
    booked_customer = models.ForeignKey(Customers, on_delete=models.PROTECT, null=True, blank=True)
    booked_time = models.DateTimeField(default=None, null=True, blank=True)
    booked_hours = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        db_table = "Assigned Rooms"
        order_with_respect_to = 'block_floor'

    def __str__(self):
        if self.booked_customer is None:
            return str(self.block_floor.block) + ', ' +\
                   str(self.block_floor.floor) + ', ' + str(self.room_number) + ' ( Not booked )'
        else:
            return str(self.block_floor.block) + ', ' + str(self.block_floor.floor) + ', ' + str(self.room_number) + \
                   ' ( Booked by ' + self.booked_customer.user.username + ' )'
