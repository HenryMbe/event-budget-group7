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