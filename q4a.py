# Name: Lam Ching Rou
# Email ID: crlam.2020

def trace_contacts(patient, history):
    # Replace the code below with your implementation.
    patient_date = []
    patient_list = []
    # direct contact
    for tup in history: # tup is (name1, name2, day of meeting patient 0)
            if tup[0] == patient and -5 <= tup[2] < 0:
                if tup[1] not in patient_list:
                    patient_list.append(tup[1])
                    patient_date.append((tup[1], tup[2]))
            elif tup[1] == patient and -5 <= tup[2] < 0:
                if tup[0] not in patient_list:
                    patient_list.append(tup[0])
                    patient_date.append((tup[0], tup[2]))

    # indirect contact
    for tup2 in patient_date:
        for tup in history: #tup 2 is (name of infected, date)
            if tup2[0] == tup[0] and tup2[1] + 2 <= tup[2] < tup2[1] + 7:
                if tup[1] not in patient_list:
                    patient_list.append(tup[1])
                    patient_date.append((tup[1], tup[2]))
            elif tup2[0] == tup[1] and tup2[1] + 2 <= tup[2] < tup2[1] + 7:
                 if tup[0] not in patient_list:
                    patient_list.append(tup[0])
                    patient_date.append((tup[0], tup[2]))

    if patient in patient_list:
        patient_date.remove(patient) # return list should not include patient 0

    return patient_list
        
    
    


    


    
         
        