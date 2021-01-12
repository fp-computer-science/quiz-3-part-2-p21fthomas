
together = [0]
def force_equation(younglings,race):
    together = [0]
    for x in younglings:
        together.append(x)
        for y in race:
            together.append(y)
    return together

print(force_equation(['Petro', 'Katooni', 'Byph', 'Ganodi', 'Zatt', 'Gungi'],['Human', 'Tholothian', 'Ithorian', 'Rodian', 'Nautolan', 'Wookie']))
