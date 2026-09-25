class Patient:
    def __init__(
            self, 
            patient_id: str,
            name: str,
            contact_details: str,
    ): 
        if not patient_id:
            raise ValueError("Patient ID Required")

        if not name:
            raise ValueError("Patient Name Required")

        self.patient_id = patient_id
        self.name = name
        self.contact_details = contact_details
        self.appointments = [] 


class Practitioner:
    def __init__(
            self, 
            practitioner_id: str, 
            name: str, 
            specialty: str, 
    ):
        if not practitioner_id:
            raise ValueError("Practitioner ID Required") 

        if not name:
            raise ValueError("Practitioner Name Required") 

        if not specialty:
            raise ValueError("Practitioner Specialty Required") 

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty
        self.appointments = [] 


