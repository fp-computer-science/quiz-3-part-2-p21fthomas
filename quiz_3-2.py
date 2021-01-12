output = [0]
output2 = [0]

def unzip(ledger):
    output = [0]
    output2 = [0]
    for w in ledger:
        for x in w:
            if x == int:
                output.append(x)
            elif x == str:
                output.append(x)
    return output

print(unzip([['Sebulba', 100, 200, 400], ['Skywalker', 500, 100, 20000], ['Reeso', 200, 700, 100]]))
#print(output2)