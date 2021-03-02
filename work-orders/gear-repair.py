gearbox = {
    'manufacturer': input("Gear Manufacturer: "),
    'model': input("Gear Model: "),
    'sn': input("Gear Serial #: ")
}

gldd_poc ={
    'name': input("GLDD contact name: ").title(),
    'phone': input("GLDD contact phone #: "),
    'email': input('GLDD contact email: ')
}

title = f"{gearbox.get('model')} Gear Inspection (SN: {gearbox.get('sn')})"

work_scope = f"""Requirements:
Provide the labor, material and equipment as required to accomplish the following:
  1. Tear down GLDD-provided {gearbox.get('model')} for inspection by GLDD representative {gldd_poc.get('name')}.
\ta. Rebuild will be determined after complete inspection of gear.
  2. Upon completion of inspection, submit findings and estimate to GLDD representative {gldd_poc.get('name')} for further guidance and, if agreed, PO revision.
\ta. Discussed repairs shall not commence until a revised PO has been received from GLDD's Purchasing Department.
\tb. If more than 5 days pass without receiving an updated PO, notify {gldd_poc.get('name')}, who will inquire further.

Notes:
  1. GLDD Point of Contact:
\ta. {gldd_poc.get('name')}, {gldd_poc.get('phone')}, {gldd_poc.get('email')}.
  2. Upon completion, email invoice to {gldd_poc.get('name')} for review and processing.

Deliverables:
  1. Inspection report with findings, recommendations and an estimate for repair.

Owner-Furnished Material:
  1. One {gearbox.get('manufacturer')} {gearbox.get('model')} (SN: {gearbox.get('sn')})

References:
  1. None.
"""

def main():
    print()
    print()

    print(title)
    print(work_scope)

main()