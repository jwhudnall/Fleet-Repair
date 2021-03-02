wcp_lh = input("Enter LH WCP: ")
wcp_rh = input("Enter RH WCP: ")
diameter = float(input("Propeller Diameter (in inches): "))
pitch = float(input("Propeller Pitch (in inches): "))
bore = float(input("Propeller Bore (in inches): "))
hub = float(input("Propeller Hub (in inches): "))
num_blades = float(input("Number of Blades: "))
title = f"Propeller Repair - {wcp_lh} & {wcp_rh}"


gldd_contact = {
'name': input('GLDD contact name: '),
'phone': input('GLDD contact phone: '),
'email': input('GLDD contact email: ')
}

work_scope = f'''
Requirements:
Provide the labor, material and equipment as required to accomplish the following:
1. Inspect and assess one set of {diameter}" Diameter x {pitch}" Pitch x {bore}" Bore, {hub}" Hub, {num_blades} - blade NiBrAl propellers.                                    
2. Provide a scan report, including a written description of findings, along with repair recommendations, to {gldd_contact.get('name')}.                               
3. Recondition both propellers to ISO class 2, targeting the directed pitch of {pitch}".                                           
4. Weld all missing material and diameter back to {diameter}".                                  
5. Clean and verify balance.     
6. Remove any old improper stampings on both propeller hubs. Re-stamp as directed with no heat and correct DIA X pitch and weight of prop.   
7. Perform bore taper inspection and report findings to {gldd_contact.get('name')}.  
8. Package in reuseable crate and provide shipping dimensions and weight to GLDD representative.                             

Quality Control / Quality Assurance
1. Upon completion of repairs include final scan report on repaired propeller set using Prop Scan E4 Technology to ensure respective tolerances and measurements.                                       
                                 
Notes: 
1. Contact {gldd_contact.get('name')} ({gldd_contact.get('phone')}; {gldd_contact.get('email')}) for shipping instructions upon completion.
'''

def print_work_order():
	print('_' * 15 + '\n')
	print(title)
	print(work_scope)
	print('_' * 15)

print_work_order()





