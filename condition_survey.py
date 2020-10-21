title = 'Annual Condition Survey'

vessel_info = {'name': input('Vessel Name: '),
                'length': input('GLDD length (in ft): '),
                'location': input('Vessel Location: ')
}

gldd_contact = {'name': input('GLDD contact name: '),
                'phone': input('GLDD contact phone: '),
                'email': input('GLDD contact email: ')
}

operator_contact = {'name': input('Operator Name: '),
                    'number': input('Operator Number: ')
    }

work_scope = f'''
Requirements:
Provide the labor, material and equipment as required to accomplish the following: 
  1. Travel to the vessel located at {vessel_info.get('location')}.
  2. Perform an annual vessel condition survey, verifying the vessel's seaworthiness and ability to perform its duties.
  3. Submit electronic report to GLDD representative {gldd_contact.get('name')}.

Notes:
  1. Survey can be performed in water.
  2. GLDD Point of Contact: {gldd_contact.get('name')} ({gldd_contact.get('phone')}; {gldd_contact.get('email')})

Deliverables:
  1. Annual condition survey in electronic form (PDF or Word format).

Owner-Furnished Material:
  1. None.

References:
  1. Vessel Information:
     a. Name: {vessel_info.get('name')}
     b. LOA: {vessel_info.get('length')} ft.
     c. Location: {vessel_info.get('location')}
  2. Vessel Contact:
     a. Name: {operator_contact.get('name')}
     b. Phone: {operator_contact.get('number')}
'''

def print_work_order():
    print('_' * 15)
    print(title)
    print(work_scope)
    print('_' * 15)

print_work_order()

