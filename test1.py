

def run_test():
    print('test 1 - dictionary')

    me = {
        'first': 'Ard',
        'last': 'Mora',
        'age': 33,
        'hobbies': [],
        'address': {'street': '123 apple street', 'city': 'san diego', 'state': 'CA', 'zip': '91229'}
    }

# add fist and last
    print(me)
    print(me['first'])
    print(me['first'] + ' ' + me['last'])

# add values
    me['age'] = me['age'] + 1
    me['age'] = 995

    # sdd new keys
    me['preferred_color'] = 'turquoise'
    print(me)

    # read if existing
    if 'middle_name' in me:  # check for existence
        print(me['middle_name'])

    # print full address
    address = me['address']
    print('-----------address------------')
    print(address)
    print(type(address))

    #   f = format
    print(
        f'{address["street"]} {address["city"]}, {address["state"]}, {address["zip"]}')


run_test()
