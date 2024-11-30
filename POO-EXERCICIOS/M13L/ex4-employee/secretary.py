from employee import Employee

class Secretary(Employee):
    def get_job_description(self):
        return "Manages schedules and administrative tasks."

    def __str__(self):
        return f"{super().__str__()} (Secretary)"
