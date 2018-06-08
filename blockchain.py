genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Nikhil'
participants = {'Nikhil'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_last_blockchain_value():
    """ Returns the last value of the Blockchain """

    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    tx_recipient = input('Enter the sender of the transaction: ')
    tx_amount = float(input('Enter you transaction amount: '))

    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input('Enter you choice: ')

    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    # is_valid = True

    # for block_index in range(len(blockchain)):
    #     if block_index == 0:
    #         block_index += 1

    #         continue
    #     elif blockchain[block_index][0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False

    #         break

    # return is_valid
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print('What would you like to do?')
    print(' 1: Enter a new transaction value')
    print(' 2: Mine a new block')
    print(' 3: Output the blockchain blocks')
    print(' 4: Output participants')
    print(' h: Manipulate the chain')
    print(' q: Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Zephyr', 'recipient': 'Pickle', 'amount': 100}]
            }
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Invalid Input!')

    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain')

        break
else:
    print('User left!')


print('Bye!')
