from django.db import models


# Food Types...
class FoodTypes(models.Model):
    food_type = models.CharField(max_length=50)

    class Meta:
        db_table = 'Food Types Table'

    def __str__(self):
        return self.food_type


# Food Categories...
class FoodCategory(models.Model):
    category = models.CharField(max_length=20)

    class Meta:
        db_table = 'Food Categories'

    def __str__(self):
        return self.category


# Food Items...
class FoodItems(models.Model):
    food_item = models.CharField(max_length=100)

    class Meta:
        db_table = 'Food Items Table'

    def __str__(self):
        return self.food_item


# Foods Main Database...
class Foods(models.Model):
    food_type = models.ForeignKey(FoodTypes, on_delete=models.PROTECT)
    food_category = models.ForeignKey(FoodCategory, on_delete=models.PROTECT)
    food_item = models.ForeignKey(FoodItems, on_delete=models.PROTECT)
    item_available = models.CharField(max_length=20)
    item_required = models.CharField(max_length=20)

    class Meta:
        db_table = 'Food Database Table'

    def __str__(self):
        return self.food_type.food_type + self.food_item.food_item
