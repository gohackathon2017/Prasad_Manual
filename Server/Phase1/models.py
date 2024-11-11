from django.db import models

class Phase1Student(models.Model):
    roll_no = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    student_mobile = models.CharField(max_length=15)
    father_mobile = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return str(self.roll_no) 



# Anatomy Subject Table

class Anatomy(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase1Student, to_field='roll_no', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100, editable=False) 
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    def save(self, *args, **kwargs):
        # Automatically populate student_name from the related student record
        if self.roll_number:
            self.student_name = self.roll_number.name
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('roll_number', 'date')
        
    def __str__(self):
        return f"{self.student_name} - {self.date} - {self.get_status_display()}"



# Physicology  Subject Table


class Physicology(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase1Student, to_field='roll_no', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100, editable=False) 
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    def save(self, *args, **kwargs):
        # Automatically populate student_name from the related student record
        if self.roll_number:
            self.student_name = self.roll_number.name
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('roll_number', 'date')
        
    def __str__(self):
        return f"{self.student_name} - {self.date} - {self.get_status_display()}"




# Biochemistry Subject Table

class Biochemistry(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase1Student, to_field='roll_no', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100, editable=False) 
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    def save(self, *args, **kwargs):
        
        if self.roll_number:
            self.student_name = self.roll_number.name
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('roll_number', 'date')
        
    def __str__(self):
        return f"{self.student_name} - {self.date} - {self.get_status_display()}"



# Community Medicine Subject Table

class CommunityMedicine(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase1Student, to_field='roll_no', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100, editable=False) 
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    def save(self, *args, **kwargs):
       
        if self.roll_number:
            self.student_name = self.roll_number.name
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('roll_number', 'date')
        
    def __str__(self):
        return f"{self.student_name} - {self.date} - {self.get_status_display()}"


# Foundation Course Subject Table

class FoundationCourse(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase1Student, to_field='roll_no', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100, editable=False) 
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    def save(self, *args, **kwargs):
        
        if self.roll_number:
            self.student_name = self.roll_number.name
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('roll_number', 'date')
        
    def __str__(self):
        return f"{self.student_name} - {self.date} - {self.get_status_display()}"




# ECA Subject Table

class ECA(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase1Student, to_field='roll_no', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100, editable=False) 
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    def save(self, *args, **kwargs):
        
        if self.roll_number:
            self.student_name = self.roll_number.name
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('roll_number', 'date')
        
    def __str__(self):
        return f"{self.student_name} - {self.date} - {self.get_status_display()}"
