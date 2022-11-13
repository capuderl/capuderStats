

def updateBudget(b, car,subscriptions,groceries,misc,rest,bills, adventure):

    b['car'].append(car)
    b['subscriptions'].append(subscriptions)
    b['groceries'].append(groceries)
    b['misc'].append(misc)
    b['rest'].append(rest)
    b['bills'].append(bills)
    b['adventure'].append(adventure)
    
    return b
