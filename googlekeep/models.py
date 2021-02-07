from django.db import models


class Note(models.Model):
    note_id = models.AutoField
    title = models.CharField(max_length=50)
    note = models.CharField(max_length=150)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Note #{}'.format(self.id)
