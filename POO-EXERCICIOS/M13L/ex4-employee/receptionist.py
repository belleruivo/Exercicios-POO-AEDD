from employee import Employee

class Receptionist(Employee):
    def get_job_description(self):
        return "Handles front desk and customer inquiries."

    def __str__(self):
        return f"{super().__str__()} (Receptionist)"
