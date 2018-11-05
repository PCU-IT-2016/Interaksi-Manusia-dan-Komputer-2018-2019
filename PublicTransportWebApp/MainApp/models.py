from django.db import models

class Category(models.Model):
    name                    = models.CharField(max_length=16)
    image                   = models.CharField(max_length=64, null=True)
    descriptions            = models.TextField()
    def __str__(self):
        return self.name

class Transportation(models.Model):
    name                    = models.CharField(max_length=64)
    image                   = models.TextField(null=True)
    category_id             = models.ForeignKey(Category, on_delete=models.CASCADE)
    status                  = models.CharField(max_length=16)
    description             = models.TextField()
    def __str__(self):
        return self.name

class City(models.Model):
    name                    = models.CharField(max_length=32)
    code_name               = models.CharField(max_length=8, default="DEF")
    def __str__(self):
        return self.name

class Infrastructure(models.Model):
    name                    = models.CharField(max_length=32)
    description             = models.TextField()
    def __str__(self):
        return self.name

class Place(models.Model):
    name                    = models.CharField(max_length=128)
    infrastructure_id       = models.ForeignKey(Infrastructure, on_delete=models.CASCADE)
    city                    = models.ForeignKey(City, on_delete=models.CASCADE)
    address                 = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Schedule(models.Model):
    date_time               = models.DateTimeField()
    transportation_id       = models.ForeignKey(Transportation, on_delete=models.CASCADE)
    place_from_id           = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place_from')
    place_destination_id    = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place_destination')
    depart_status           = models.CharField(max_length=16)
    cost                    = models.IntegerField(null=True)
    def __str__(self):
        return self.transportation_id.name + " " + str(self.date_time)

class Account(models.Model):
    username                = models.CharField(max_length=32)
    password                = models.CharField(max_length=32)
    email                   = models.CharField(max_length=64)
    def __str__(self):
        return self.email

class Transaction(models.Model):
    account_id              = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_time               = models.DateTimeField()
    cost = models.IntegerField()
    def __str__(self):
        return "Transaction by " + self.account_id

class Transactions_Detail(models.Model):
    transaction_id          = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    schedule_id             = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    def __str__(self):
        show_format = "Transaction detail on transaction {}, schedule {}".format(self.transaction_id, self.schedule_id)
        return show_format
