def participation_cost(attendees,food_per_person,transport_per_person):
    people = attendees*(food_per_person+transport_per_person)
    return people

#Normal Attendees
People = participation_cost(10,800,200)
print (People)

#Zero Attendees
People = participation_cost(0,800,200)
print (People)

"""
Component: participation_cost
Returns: "pparticipation cost for 10 attendees and 0 attendees
Tests: Normal attendees, zero attendees
Issue: none
"""