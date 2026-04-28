types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def unique_tickets(ticket_list):
    unique = []
    for ticket in ticket_list:
        if ticket not in unique:
            unique.append(ticket)
    return unique


def build_tickets_by_type(types_dict, tickets_dict):
    tickets_by_type = {}
    used_tickets = set()

    for level in sorted(types_dict.keys()):
        unique = unique_tickets(tickets_dict.get(level, []))
        filtered = []
        for ticket in unique:
            if ticket not in used_tickets:
                filtered.append(ticket)
                used_tickets.add(ticket)
        tickets_by_type[types_dict[level]] = filtered

    return tickets_by_type


tickets_by_type = build_tickets_by_type(types, tickets)
print(tickets_by_type)
