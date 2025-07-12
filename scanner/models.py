from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True) # The ID they scan
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"

class ScanRecord(models.Model):
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE) 
    scan_time = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=50, default='Present') 

    def __str__(self):
        return f"{self.employee.name} scanned at {self.scan_time.strftime('%Y-%m-%d %H:%M:%S')} - {self.status}"

    class Meta:
        ordering = ['-scan_time'] 