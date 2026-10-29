# Participants_cost
def participant_cost(attendees,food_per_person,transport_per_person):
    people = attendees*(food_per_person+transport_per_person)
    return people


#Normal Attendees
People = participant_cost(10,800,200)
print (People)

#Zero Attendees
People = participant_cost(0,800,200)
print (People)

"""
Component: participant_cost
Returns: "participant cost for 10 attendees and 0 attendees"
Tests: Normal attendees, zero attendees
Issue: none
"""

#Event total

def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    people_cost = participant_cost(attendees, food_per_person, transport_per_person)
    return people_cost + venue_cost

# Normal case
print(event_total(10, 800, 200, 5000))# For normal attendee

# Zero case
print(event_total(0, 800, 200, 5000))# For zero attendee case

"""
Component: event_total
Returns: Calls participant_cost, adds venue_cost, returns the combined total.
Tests: 
    Normal attendee cost plus venue
    Zero attendees with a non-zero venue
Issue: Code would not run due to its dependance on the participant_cost function
"""

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

#Event_summary
def event_summary (event_name, total, status):
    return f" {event_name} : total {total} naira. {status}"

#Study Day Event
summary = event_summary ("Study Day",15000,"Within budget.")
print (summary)
#Training Day Event
summary=event_summary("Training Day",16000,"Exact budget.")
print (summary)

"""
component: event_summary
returns: Study Day : total 15000 naira. Within budget. for example case
Tests: the required example, one different event name and total
Issues: none
"""
