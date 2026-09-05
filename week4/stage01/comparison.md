#task 1
# Create and run a simple Python file with basic input,output statements

print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")


#task1enhanced
# Use lists, dictionaries and functions to enhance the Python file

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()



#AI version 

def create_appointment(patient_name, practitioner_name, appointment_time):
    """
    Stores appointment information in a dictionary.

    No database or GUI is used.
    """

    appointment = {
        "patient_name": patient_name,
        "practitioner_name": practitioner_name,
        "appointment_time": appointment_time
    }

    return appointment


# Example usage
appointment = create_appointment(
    "John Smith",
    "Dr. Brown",
    "2026-09-10 14:30"
)

print(appointment) 

{
    'patient_name': 'John Smith',
    'practitioner_name': 'Dr. Brown',
    'appointment_time': '2026-09-10 14:30'
}


Part E - Compare Human and AI Versions
Question	Human version	AI version
Easy to understand?	Yes	Yes
Runs successfully?	Yes	Yes
Uses only required features?	Yes	Yes
Adds assumptions?	No	No
Handles errors?	No	No
Could I explain it?	Yes	Yes 

