vessel_info = {
    'name': input('Vessel name: '),
    'location': input('Vessel location: ')
    }

gldd_poc = {
    'name': input('GLDD point of contact (name): '),
    'phone': input('GLDD point of contact (phone): '),
    'email': input('GLDD point of contact (email): ')
    }

additional_requirement = input('Additional line item to be completed (beyond standard inspection): ')


print('='*20)
print(f'''Annual Mircom Panel / Portable Fire Extinguisher Inspection
Requirements:
Provide the labor, material and equipment as required to accomplish the following: 
  1. Travel to the vessel located at {vessel_info.get('location')}.
  2. Inspect the Mircom FA-300 Panel, addressing any issues, renewing the battery if needed, and any other
  services required.
  3. Inspect all onboard portable fire extinguishers. {additional_requirement}

Notes:
  1. GLDD POC:
     a. Name: {gldd_poc.get('name')}
     b. Phone: {gldd_poc.get('phone')}
     c. Email: {gldd_poc.get('email')}
  2. Vessel information:
     a. Name: {vessel_info.get('name')}

Deliverables:
  1. Upon completion, forward annual inspection certificates in PDF form to GLDD point of contact listed above.

Owner-Furnished Material:
  1. None.

References:
  1. ''')
