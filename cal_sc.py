def Main(op, n1, n2):

    if op == 'add':
        return n1 + n2
    elif op == 'sub':
        return n1 - n2
    elif op == 'div':
        return n1/n2
    elif op == 'mul':
        return n1 * n2 

    else:
        return - 1


# sc build_run /root/contracts/cal_sc.py False False False 070202 02 add 10 20
