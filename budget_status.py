#Budget Status
def budget_status(budget, total):
    if total < budget :
        return "Within budget"
    elif total== budget:
        return "Exact budget"
    else:
        return "Over budget"

#within budget
status = budget_status(16000, 15000)
print(status)

#over budget
status = budget_status(16000, 17000)
print(status)

#Exact budget
status = budget_status(16000, 16000)
print(status)

 

"""
Component : budget_status


Return : "within budget" when total <=budget
otherwise "Over budget"

Tests:  
"Within budget"
"Over budget"
"Exact budget"

issues: none
"""