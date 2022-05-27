from django.db import models


class Case(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    detention_period = models.IntegerField()

    def __str__(self):
        return self.name


PRISONER_STATUS_CHOICES = (
    ("1", "IN_MATE"),
    ("2", "OUT_MATE")
)

GENDER_CHOICES = (
    ("1", "Male"),
    ("2", "Female")
)


class Prisoner(models.Model):
    firstname = models.CharField(max_length=30, default='Not_provided')
    lastname = models.CharField(max_length=30, default='Not_provided')
    email = models.EmailField()
    identification = models.IntegerField()
    phone = models.IntegerField()
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=PRISONER_STATUS_CHOICES)
    date = models.DateField()
    gender = models.TextField(max_length=10, choices = GENDER_CHOICES)
    address = models.CharField(max_length=20,null=True )
    release_date = models.DateField()
    photo = models.ImageField(upload_to='photos/', default='avatar.png')

    def __str__(self):
        return str(self.firstname + ' ' + self.lastname)

class Visitor(models.Model):
    firstname = models.CharField(max_length=30, default='Not_provided')
    lastname = models.CharField(max_length=30, default='Not_provided')
    identification = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return self.firstname + ' ' + self.lastname

RELATIONSHIP_CHOICES = (
    ('1', 'Parent'),
    ('2', 'Child'),
    ('3', 'Relative'),
    ('4', 'Friend')
)


class Visit(models.Model):
    visitors = models.ManyToManyField(Visitor)
    prisoner = models.ManyToManyField(Prisoner)
    date = models.DateField()
    relationship = models.CharField(max_length=10, choices=RELATIONSHIP_CHOICES)

    def __str__(self):
        return str(self.pk)


LEAVE_STATUS_CHOICES = (
    ("1", "Active"),
    ("2", "Expired")
)


class Leave(models.Model):
    prisoner = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approval = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=LEAVE_STATUS_CHOICES)

    def __str__(self):
        return str(self.pk)

class Transfer(models.Model):
    prisoner = models.ForeignKey(Prisoner, on_delete=models.CASCADE)
    date = models.DateField()
    where_from = models.TextField(max_length=50)
    where_to = models.TextField(max_length=50)
    reason = models.TextField()

    def __str__(self):
        return str(self.prisoner)

COMPLAIN_STATUS_CHOICES = (
    ("1", "Pending"),
    ("2", "Replied")
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

