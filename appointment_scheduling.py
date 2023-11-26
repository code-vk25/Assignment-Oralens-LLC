from datetime import datetime, timedelta

class Appointment:
    def __init__(self, start_time, duration, patient_name):
        self.start_time = start_time
        self.end_time = start_time + timedelta(minutes=duration)
        self.duration = duration
        self.patient_name = patient_name

class Doctor:
    def __init__(self, name, availability_start, availability_end):
        self.name = name
        self.availability_start = availability_start
        self.availability_end = availability_end
        self.appointments = []

    def schedule_appointment(self, appointment):
        # Check if the appointment time is within the doctor's availability
        if self.availability_start <= appointment.start_time < self.availability_end:
            # Check for overlapping appointments
            overlapping_appointments = [a for a in self.appointments if
                                        (appointment.start_time < a.end_time and appointment.end_time > a.start_time)]

            if not overlapping_appointments:
                self.appointments.append(appointment)
                return True
            else:
                print("Appointment overlaps with existing appointment.")
        else:
            print("Doctor not available at this time.")

    def display_schedule(self):
        print(f"\nDoctor {self.name}'s Schedule:")
        for appointment in self.appointments:
            print(f"Appointment with {appointment.patient_name} from {appointment.start_time} to {appointment.end_time}")


def schedule_appointment(doctors, patient_name, preferred_time, duration):
    appointment_time = datetime.strptime(preferred_time, "%Y-%m-%d %H:%M")
    appointment = Appointment(appointment_time, duration, patient_name)

    print(f"For {patient_name} :")

    for doctor in doctors:
        if doctor.schedule_appointment(appointment):
            print(f"Appointment scheduled with Doctor {doctor.name} at {appointment.start_time}")
            break
    else:
        print("No available doctor for the requested time.")


if __name__ == "__main__":
    # Create doctors with availability
    doctor1 = Doctor("Dr. Smith", datetime.now() - timedelta(hours = 1000), datetime.now() + timedelta(hours=100))
    doctor2 = Doctor("Dr. Johnson", datetime.now() - timedelta(hours = 1000), datetime.now() + timedelta(hours=100))

    # Create a list of doctors
    doctors = [doctor1, doctor2]

    # Schedule mock appointments
    schedule_appointment(doctors, "John Doe", "2023-11-21 10:45", 30)
    schedule_appointment(doctors, "Jane Doe", "2023-11-26 12:00", 45)
    schedule_appointment(doctors, "Alice", "2023-11-26 11:30", 30)
    schedule_appointment(doctors, "Bob", "2023-11-26 13:30", 60)


    schedule_appointment(doctors, "John Doe", "2023-11-21 10:50", 30)
    schedule_appointment(doctors, "Jane Doe", "2023-11-26 12:05", 45)
    schedule_appointment(doctors, "Alice", "2023-11-26 11:35", 30)
    schedule_appointment(doctors, "Bob", "2023-11-26 13:35", 60)


    # Display doctors' schedules
    for doctor in doctors:
        doctor.display_schedule()
