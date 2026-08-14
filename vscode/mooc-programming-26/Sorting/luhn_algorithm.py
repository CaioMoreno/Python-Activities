def verify_card_number(digits: list):
    card = [int(digit) for digit in digits if digit != "-" and digit != " "]
    i = len(card) - 1

    while i >= 0:
        if len(card) % 2 == 0:
            if i % 2 == 0:
                card[i] *= 2
        else:
            if i % 2 != 0:
                card[i] *= 2
        if card[i] > 9:
            card[i] -= 9
        i -= 1

    print(card)
    print(sum(card))
    if sum(card)%10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


print(verify_card_number('4111-1111 1111-1111'))
