def speeding_ticket(speed, is_birthday):
    # Adjust speed limits if it's the driver's birthday
    adjustment = 5 if is_birthday else 0

    # Determine ticket type based on adjusted speed limits
    if speed <= 60 + adjustment:
        return "No Ticket"
    elif 61 <= speed <= 80 + adjustment:
        return "Small Ticket"
    else:
        return "Big Ticket"

# Example Test Cases
print(speeding_ticket(60, False))  # Expected: "No Ticket"
print(speeding_ticket(75, False))  # Expected: "Small Ticket"
print(speeding_ticket(85, False))  # Expected: "Big Ticket"
print(speeding_ticket(65, True))   # Expected: "No Ticket"
print(speeding_ticket(85, True))   # Expected: "Small Ticket"
