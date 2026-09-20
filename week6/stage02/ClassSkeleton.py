class Patient: 
    def __init__(self, patient_id, name, contact_details):
        self.patient_id = patient_id
        self.name = name 
        self.contact_details = contact_details 
        self.appointments = [] 

    def book_appointment(self):
        pass 

    def view_appointments(self):
        pass 

    def pay_fee(self):
        pass 

class Practitioner:
    def __init__(self, practitioner_id, name, specialty):
        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty 
        self.appointments = []

    def view_schedule(self):
        pass 

    def check_patient(self):
        pass 

    def update_availability(self):
        pass 

class Appointment:
    def __init__(self, appointment_id,date_time, status):
        self.appointment_id = appointment_id
        self.date_time = date_time 
        self.status = status
        self.patient = None
        self.practitioner = None

    def create_appointment(self):
        pass 

    def update_appointment(self):
        pass 

    def cancel_appointment(self):
        pass 


