# Name: Lam Ching Rou
# Email ID: crlam.2020

def trace_contacts(patient, history):
    # Replace the code below with your implementation.

    patient_list = []
    return_list = []
    # direct contact
    for tup in history: # tup is (name1, name2, day of meeting patient 0)
        for tup2 in patient_list:
            if tup[0] == patient and -5 <= tup[2] < 0:
                if tup[1] != tup2[0]:
                    patient_list.append((tup[1], tup[2]))
            elif tup[1] == patient and -5 <= tup[2] < 0:
                if tup[0] != tup2[0]:
                    patient_list.append((tup[0], tup[2]))

    # indirect contact
    for tup2 in patient_list:
        for tup in history: #tup 2 is (name of infected, date)
            if tup2[0] == tup[0] and tup2[1] + 2 <= tup[2] < tup2[1] + 7:
                if tup[1] != tup2[0]:
                    patient_list.append((tup[1], tup[2]))
            elif tup2[0] == tup[1] and tup2[1] + 2 <= tup[2] < tup2[1] + 7:
                 if tup[0] != tup2[0]:
                    patient_list.append((tup[0], tup[2]))


    for tup2 in patient_list:
        return_list.append(tup2[0])

    if patient in return_list:
        patient_list.remove(patient)

    return return_list
        
    
    


    


    
         
        