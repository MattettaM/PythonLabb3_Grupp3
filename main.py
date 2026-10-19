import csv
import json
from dataclasses import dataclass


@dataclass
class Support_Ticket:
    errand_number: int
    customer_name: str
    category: str
    priority: int
    status: str

    def convert_to_dictionary(self):
        return {
                "Kundens namn": self.customer_name,
                "Kategori": self.category,
                "Prioritet": self.priority,
                "Status": self.status
                }

    def close_ticket(self):
        self.status = "Stängt"

    def update_status(self, new_status: str):
        self.status = new_status

def get_open_tickets(tickets: list[Support_Ticket]):
    open_tickets = []
    for ticket in tickets:
        if ticket.status != "Stängt":
            open_tickets.append(ticket)
    return open_tickets

def priority_string_to_number(priority_string):
    if priority_string == "Hög":
        return 2
    elif priority_string == "Medel":
        return 1
    else: # priortiy == "Låg"
        return 0

def print_ticket_with_status(ticket: Support_Ticket, status: str):
    if ticket.status == status:
        print(ticket)

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
sorted_tickets = sort_tickets_by_priority(support_tickets)
open_tickets: list[Support_Ticket] = get_open_tickets(sorted_tickets)

open_tickets_dictionary = {}
for ticket in open_tickets:
    print(ticket)
    open_tickets_dictionary[str(ticket.errand_number)] = ticket.convert_to_dictionary()

with open("open_tickets.json", "w", encoding="utf-8") as output:
    json.dump(open_tickets_dictionary, output, indent=4, ensure_ascii=False)