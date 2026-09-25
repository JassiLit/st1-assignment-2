# # Appointment – store patient appointments, store patient and practitioner details, 
# # create and update appointments.    
# # This here is from a approved UML. Act as a Python pair programmer. 
# # Implement only the Appointment class from the approved SmartCare UML. 
# # Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. 
# # Do not add database, UI, notification or service classes. 
# # Protect status transitions and explain any decision not directly visible in the UML. 




# Copilot response 


# Below is a focused implementation of the Appointment class only, based on the requirements you provided:

# Stores patient and practitioner details through object references.
# Supports creating and updating appointments.
# Uses an AppointmentStatus enum.
# Cancelled appointments remain in memory as objects.
# Status transitions are protected.
# No database, UI, notification, controller, or service classes. 

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from patient import Patient
    from practitioner import Practitioner


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: "Patient",
        practitioner: "Practitioner",
        appointment_datetime: datetime,
        status: AppointmentStatus = AppointmentStatus.SCHEDULED,
    ) -> None:
        if not appointment_id:
            raise ValueError("Appointment ID required")

        self._appointment_id = appointment_id
        self._patient = patient
        self._practitioner = practitioner
        self._appointment_datetime = appointment_datetime
        self._status = status

    @property
    def appointment_id(self) -> str:
        return self._appointment_id

    @property
    def patient(self) -> "Patient":
        return self._patient

    @property
    def practitioner(self) -> "Practitioner":
        return self._practitioner

    @property
    def appointment_datetime(self) -> datetime:
        return self._appointment_datetime

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def reschedule(self, new_datetime: datetime) -> None:
        """
        Update the appointment date/time.
        """
        if self._status != AppointmentStatus.SCHEDULED:
            raise ValueError(
                "Only scheduled appointments can be rescheduled."
            )

        self._appointment_datetime = new_datetime

    def cancel(self) -> None:
        """
        Cancel the appointment but keep the object.
        """
        if self._status == AppointmentStatus.COMPLETED:
            raise ValueError(
                "Completed appointments cannot be cancelled."
            )

        self._status = AppointmentStatus.CANCELLED

    def complete(self) -> None:
        """
        Mark the appointment as completed.
        """
        if self._status == AppointmentStatus.CANCELLED:
            raise ValueError(
                "Cancelled appointments cannot be completed."
            )

        if self._status == AppointmentStatus.COMPLETED:
            raise ValueError(
                "Appointment is already completed."
            )

        self._status = AppointmentStatus.COMPLETED

    def __str__(self) -> str:
        return (
            f"Appointment("
            f"id={self._appointment_id}, "
            f"patient={self._patient.name}, "
            f"practitioner={self._practitioner.name}, "
            f"datetime={self._appointment_datetime}, "
            f"status={self._status.value})"
        ) 




# Design Decisions

# These decisions are not always shown explicitly in UML but are commonly required when implementing the model:


# 1. Status transitions are restricted 

# Allowed transitions: 
SCHEDULED --> COMPLETED
SCHEDULED --> CANCELLED

COMPLETED --> (no further changes)
CANCELLED --> (no further changes) 

# This protects the appointment lifecycle and prevents invalid states such as: 

COMPLETED --> CANCELLED
CANCELLED --> COMPLETED
`` 


# 2. Cancelled appointments remain as objects

# You specifically stated:

# Cancelled appointments remain as objects.

# Therefore cancel() only changes the status:

self._status = AppointmentStatus.CANCELLED 

# The appointment is not deleted. 


# 3. IDs are immutable

# The appointment_id is set in the constructor and exposed through a read-only property. 
# Appointment identifiers should not change after creation. 


# 4. Patient and Practitioner are references 
# The appointment stores: 

patient: Patient
practitioner: Practitioner 

# rather than duplicating patient or practitioner data. 
# This reflects the association typically shown in a UML class diagram. 


# 5. Updates are explicit 
# Rather than allowing direct modification of attributes: 

appointment.appointment_datetime = ... 

# the class uses: 

appointment.reschedule(...)

# which enforces business rules before changes occur.

# This implementation would align well with a typical SmartCare UML where Appointment is an 
# entity class associated with Patient and Practitioner, 
# with appointment creation, updating, 
# completion, and cancellation handled through the object's own behavior.
