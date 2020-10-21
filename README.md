# Fleet Repairs
This is a collection of python scripts I use during my everyday work as a Maintenance Superintendent. The idea is to automate common work orders, removing superfluous typing and/or copy-pasting by only specifying the common variables that change.


## Propeller Repair
`prop_repair.py`

This simple script takes user input defining different aspects of boat propellers, using the information to create a repair work order.
The repair spec can then be used to generate a PO for the work.

### Propeller Aspects
* wcp_lh and wcp_rh: 'wcp' denotes a given propeller's serial number. This should be unique for historical tracking purposes.
* diameter: Propeller's overall diameter
* pitch: Propeller's desired pitch
* bore: Propeller's bore size (I.D.)
* hub: Propeller's hub length
* num_blades: Propeller's number of blades/flukes.

## Condition Survey
`condition_survey.py`

This script is used to create an annual condition survey work order.