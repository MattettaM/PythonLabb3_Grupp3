import csv
from dataclasses import dataclass


@dataclass
class Support_Ticket:
    errand_number: int
    customer_name: str
    category: str
    priority: int
    status: str

    def close_ticket(self):
        self.status = "Stängt"

    def update_status(self, new_status: str):
        self.status = new_status

def print_open_tickets(tickets: list[Support_Ticket]):
    for ticket in tickets:
        if ticket.status != "Stängt":
            print(ticket)

def priority_string_to_number(priority_string):
    if priority_string == "Hög":
        return 2
    elif priority_string == "Medel":
        return 1
    else: # priortiy == "Låg"
        return 0

def sort_tickets_by_priority(tickets: list[Support_Ticket], high_to_low = True):
    return sorted(tickets, key=lambda ticket: ticket.priority, reverse= high_to_low)


#Program start
support_tickets: list[Support_Ticket] = []
with open("supportarenden.csv", encoding="utf-8") as data:
    reader = csv.reader(data)
    next(reader)
    for row in reader:
        ticket = Support_Ticket(int(row[0]), row[1], row[2],
                                priority_string_to_number(row[3]), row[4])
        support_tickets.append(ticket)

support_tickets[0].close_ticket()
support_tickets[1].update_status("Öppet")
print_open_tickets(sort_tickets_by_priority(support_tickets))