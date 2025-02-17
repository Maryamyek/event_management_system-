from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    max_attendees = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    event = models.ForeignKey(Event, related_name='tickets', on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, related_name='tickets', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.attendee.name} - {self.event.title}"