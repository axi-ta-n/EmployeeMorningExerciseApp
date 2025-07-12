from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Employee, ScanRecord
from datetime import datetime, time

def scan_page(request):
    scanned_employee = None
    last_scan_time = None
    last_scan_status = None

    # Last 50 Scans
    recent_scans = ScanRecord.objects.select_related('employee').all()[:50]

    if 'last_scanned_employee_id' in request.session:
        try:
            employee_id = request.session['last_scanned_employee_id']
            scanned_employee = Employee.objects.get(employee_id=employee_id)
            
            last_scan_for_employee = ScanRecord.objects.filter(employee=scanned_employee).order_by('-scan_time').first()
            if last_scan_for_employee:
                last_scan_time = last_scan_for_employee.scan_time
                last_scan_status = last_scan_for_employee.status
            
            del request.session['last_scanned_employee_id']
        except Employee.DoesNotExist:
            pass 

    context = {
        'scanned_employee': scanned_employee,
        'last_scan_time': last_scan_time,
        'last_scan_status': last_scan_status,
        'recent_scans': recent_scans,
    }
    return render(request, 'index.html', context)

@require_POST
def scan_employee(request):
    employee_id = request.POST.get('employee_id')

    if not employee_id:
        messages.error(request, "Employee ID cannot be empty.")
        return redirect('scan_page')

    try:
        employee = Employee.objects.get(employee_id=employee_id)

        # Before 9 AM is Present, after is Late)
        now = datetime.now().time()
        morning_cut_off = time(9, 00) # 7:50 AM

        status = 'Present'
        if now > morning_cut_off:
            status = 'Late'

        ScanRecord.objects.create(employee=employee, status=status)
        messages.success(request, f"Scan successful for {employee.name} (ID: {employee.employee_id}). Status: {status}")

        request.session['last_scanned_employee_id'] = employee.employee_id

    except Employee.DoesNotExist:
        messages.error(request, f"Employee with ID '{employee_id}' not found.")
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")

    return redirect('scan_page')