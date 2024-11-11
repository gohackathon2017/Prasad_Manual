from django.db import models

class Phase2Student(models.Model):
    roll_no = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    student_mobile = models.CharField(max_length=15)
    father_mobile = models.CharField(max_length=15)
    email = models.EmailField(blank=True)

    def __str__(self):
        return str(self.roll_no) 



# Community Medicinetomy Subject Table

class CommunityMedicine(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase2Student, to_field='roll_no', on_delete=models.CASCADE)
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



# Pathology  Subject Table


class Pathology(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase2Student, to_field='roll_no', on_delete=models.CASCADE)
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




# Microbiology Subject Table

class Microbiology(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase2Student, to_field='roll_no', on_delete=models.CASCADE)
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



# Pharmacology Subject Table

class Pharmacology(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase2Student, to_field='roll_no', on_delete=models.CASCADE)
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


# Forensic Med And TC Subject Table

class ForensicMedAndTC(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase2Student, to_field='roll_no', on_delete=models.CASCADE)
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




# Medicine Subject Table

class Medicine(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase2Student, to_field='roll_no', on_delete=models.CASCADE)
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




# Surgery Subject Table

class Surgery(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase2Student, to_field='roll_no', on_delete=models.CASCADE)
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




# Obs And Gyn Subject Table

class ObsAndGyn(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    roll_number = models.ForeignKey(Phase2Student, to_field='roll_no', on_delete=models.CASCADE)
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

    roll_number = models.ForeignKey(Phase2Student, to_field='roll_no', on_delete=models.CASCADE)
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


