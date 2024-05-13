from Bloodbank import Bloodbank

print("Welcome to Vijay Blood Bank")

def get_blood_type(num):
    blood_dictionary = {1: "A+", 2: "A-", 3: "B+", 4: "B-", 5: "O+", 6: "O-", 7: "AB+", 8: "AB-"}
    return blood_dictionary.get(num)

try:
    options = int(input("Choose the Available Facilities: \n"
                        "1. Add Donor Details\n"
                        "2. Request Blood\n"))

    blood_bank = Bloodbank()  # Instantiate Bloodbank object

    if options == 1:
        # ADD DONOR LOGIC
        donor_name = input("Enter Donor Name: ")
        donor_age = int(input("Enter Donor Age: "))
        temp = int(input("""Choose Blood Type:
                          1. A+
                          2. A-
                          3. B+
                          4. B-
                          5. O+
                          6. O-
                          7. AB+
                          8. AB-\n"""))
        donor_blood_type = get_blood_type(temp)
        blood_bank.donor_details(donor_name, donor_age, donor_blood_type)




    elif options == 2:
        # REQUEST BLOOD LOGIC
        hospital_name = input("Enter Hospital Name: ")
        patient_name = input("Enter Patient Name: ")
        patient_age = int(input("Enter Patient Age: "))
        temp = int(input("""Choose Patient Blood Type:
                           1. A+
                           2. A-
                           3. B+
                           4. B-
                           5. O+
                           6. O-
                           7. AB+
                           8. AB-\n"""))
        patient_blood_type = get_blood_type(temp)
        donor_name = input("Enter Donor Name: ")
        donor_age = int(input("Enter Donor Age: "))
        temp = int(input("""Choose Donor Blood Type:
                           1. A+
                           2. A-
                           3. B+
                           4. B-
                           5. O+
                           6. O-
                           7. AB+
                           8. AB-\n"""))
        donor_blood_type = get_blood_type(temp)
        blood_bank.request_blood(hospital_name,patient_name, patient_age, patient_blood_type,
                                  donor_name, donor_age, donor_blood_type)

    else:
        print("Enter a Valid Input")

except Exception as e:
    print("Error:", e)
