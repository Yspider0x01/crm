from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=260)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Record(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    tall = models.IntegerField()
    weight = models.IntegerField()
    address = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + "" + self.last_name
    
    class Meta:
        ordering = ["-created_at"]