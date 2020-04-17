from boa.interop.Neo.Runtime import GetTrigger
from boa.interop.Neo.TriggerType import Verification, Application

from boa.interop.Neo.Action import RegisterAction
from boa.interop.System.ExecutionEngine import GetScriptContainer
from boa.interop.Neo.Storage import Get, GetContext

OnWinner = RegisterAction('onWinner', 'to', 'amount', 'scripthash')


OWNER = b'I\x82]c\xca\xb3s\x84\xe3<\xb5\xda\x9f\xfa$\xd9\xc9`X\xd7'


def Main(op):

    trigger = GetTrigger()
    # print('go trigger')
    # print(trigger)
    # print(Verification)
    if trigger == Verification():
        print('verification')  # will be not be for owner and is read only

    elif trigger == Application():
        print('application')  # this is for owner

        if op == 'addEntry':
            entry = addEntry()
            return True
        
    return False

def addEntry():
    tx = GetScriptContainer()
    ctx = GetContext()

    tx_hash = tx.Hash
    print(tx_hash)
    return False


#  sc build_run /root/smartcontracts/lucky.py True False False 07 02 addEntry
