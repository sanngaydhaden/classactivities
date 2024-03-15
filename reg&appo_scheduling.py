from queue import Queue
import sys

def main():
    patient_queue = Queue()
    while True:
        print("\nDesk Manager - Patient Registration and Appointment System1")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            register_patient(patient_queue)
        elif choice == '2':
            remove_patient(patient_queue)
        elif choice == '3':
            display_patient_queue(patient_queue)
        elif choice == '4':
            print("Exiting the program. Have a nice day!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def register_patient(patient_queue):
    patient_name = input("Enter the patient's name to register: ")
    patient_queue.put(patient_name)
    print(f"Patient {patient_name} registered successfully.")

def remove_patient(patient_queue):
    if patient_queue.empty():
        print("There are no patients in the queue.")
    else:
        removed_patient = patient_queue.get()
        print(f"Patient {removed_patient} has been removed from the queue after meeting the doctor.")

def display_patient_queue(patient_queue):
    if patient_queue.empty():
        print("There are no patients in the queue.")
    else:
        print("Current Patient Queue:")
        # Making a copy of the queue to display
        temp_queue = Queue()
        while not patient_queue.empty():
            patient = patient_queue.get()
            print(patient)
            temp_queue.put(patient)
        # Restoring the original queue
        while not temp_queue.empty():
            patient_queue.put(temp_queue.get())

if __name__ == "__main__":
    main()
