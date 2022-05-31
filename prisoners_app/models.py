from django.db import models


class Crime(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    detention_period = models.IntegerField()

    def __str__(self):
        return self.name

CELL_STATUS_CHOICES = (
    ("Empty", "Empty"),
    ("Visible", "Visible"),
    ("Full", "Full")
)

class Cell(models.Model):
    name = models.CharField(max_length=10)
    max_inmates = models.IntegerField(default=4)
    status = models.CharField(max_length=10,choices=CELL_STATUS_CHOICES,default="Empty",blank=True)

    def __str__(self):
        return self.name

PRISONER_STATUS_CHOICES = (
    ("INMATE", "INMATE"),
    ("OUTMATE", "OUTMATE")
)

GENDER_CHOICES = (
    ("1", "Male"),
    ("2", "Female")
)

MARITAL_CHOICES = (
    ("Single", "Single"),
    ("Married", "Married"),
    ("Divorced", "Divorced")
)


class Prisoner(models.Model):
    firstname = models.CharField(max_length=30, default='None')
    lastname = models.CharField(max_length=30, default='None')
    email = models.EmailField(null=True)
    identification = models.IntegerField()
    phone = models.IntegerField(null=True)
    crime = models.ForeignKey(Crime, on_delete=models.SET_NULL,null=True)
    cell = models.ForeignKey(Cell, on_delete=models.SET_NULL,null=True,blank=True)
    entry_date = models.DateField()
    release_date = models.DateField(null=True, blank=True)
    marital_status = models.TextField(max_length=10, choices = MARITAL_CHOICES)
    gender = models.TextField(max_length=10, choices = GENDER_CHOICES)
    address = models.CharField(max_length=20)
    status = models.CharField(max_length=10,choices=PRISONER_STATUS_CHOICES,default="INMATE",blank=True)
    photo = models.ImageField(upload_to='photos/', default='avatar.png')

    def __str__(self):
        return str(self.firstname + ' ' + self.lastname)

class Visitor(models.Model):
    firstname = models.CharField(max_length=30, default='None')
    lastname = models.CharField(max_length=30, default='None')
    identification = models.IntegerField()
    phone = models.IntegerField()  
    date = models.DateField()  
    reason = models.TextField()

    def __str__(self):
        return self.firstname + ' ' + self.lastname


LEAVE_STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Active", "Active"),
    ("Expired", "Expired")
)


class Leave(models.Model):
    prisoner = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approval = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=LEAVE_STATUS_CHOICES,default="Pending")

    def __str__(self):
        return str(self.pk)

WHERE_FROM_CHOICES = (
    ("1", "Karubanda Prison"),
)
WHERE_TO_CHOICES = (
    ("Mageregere", "Mageregere"),
    ("Muhanga prison", "Muhanga prison"),
    ("Ririma prison", "Ririma prison"),
    ("Huye prison", "Huye prison"),
    ("Nyagatare prison", "Nyagatare prison"),
    ("Kacyiru", "Kacyiru"),
    ("Wawa", "Wawa"),
)

class Transfer(models.Model):
    prisoner = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    date = models.DateField()
    where_from = models.TextField(max_length=20,choices= WHERE_FROM_CHOICES)
    where_to = models.TextField(max_length=20,choices= WHERE_TO_CHOICES)
    reason = models.TextField()

    def __str__(self):
        return str(self.prisoner)

COMPLAIN_STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Replied", "Replied")
)


class Complain(models.Model):
    prisoner = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    date = models.DateField()
    summary = models.TextField()
    replied = models.BooleanField(default=False)
    status = models.TextField(max_length=10, choices= COMPLAIN_STATUS_CHOICES)

    def __str__(self):
        return str(self.prisoner)

class Reply(models.Model):
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE, null=True)
    summary = models.TextField()

