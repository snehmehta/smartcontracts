from boa.interop.Neo.Storage import GetContext, Get, Put, Delete


def Main(operation, addr, value):

    ctx = GetContext()

    if operation == 'balance':
        return Get(ctx, addr)

    elif operation == 'add':
        balance = Get(ctx, addr)
        new_balance = balance + value
        Put(ctx, addr, new_balance)
        return new_balance

    elif operation == 'remove':
        balance = Get(ctx, addr)
        Put(ctx, addr, balance - value)
        return balance - value

    else:
        return -1

# sc build_run /root/contracts/balance_sc.py True False False 070502 02 balance AVimbjJccLEAM6cpD5G77aiv4ujmSBQ93N 20
