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
