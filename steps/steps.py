from behave import given, when, then
from web3 import Web3
from eth_tester import EthereumTester, PyEVMBackend


# Conectar con un nodo Ethereum
#w3 = Web3(Web3.provider1("http://127.0.0.1:8545"))  # Cambia a tu URL de nodo si es diferente
ethereum_tester = EthereumTester(backend=PyEVMBackend())
w3= Web3(Web3.EthereumTesterProvider(ethereum_tester))
print(w3.is_connected())


@given('I am connected to 1 Ethereum node')
def step_given_connected_node(context):
    assert w3.is_connected(), "Failed to connect to Ethereum node"

@when('I send a simple transaction')
def step_when_send_transaction(context):
    tx = {
        'from': w3.eth.accounts[0],  # Cuenta de origen
        'to': w3.eth.accounts[1],    # Cuenta de destino
        'value': w3.to_wei(0.01, 'ether'),
        'gas': 2000000,
        'gasPrice': w3.to_wei('50', 'gwei')
    }
    tx_hash = w3.eth.send_transaction(tx)
    context.tx_hash = tx_hash
    assert tx_hash is not None, "Transaction failed"

@then('the transaction should be mined successfully')
def step_then_transaction_mined(context):
    tx_receipt = w3.eth.wait_for_transaction_receipt(context.tx_hash)
    assert tx_receipt is not None, "Transaction receipt not received"

@then('the block should be added to the blockchain')
def step_then_block_added(context):
    tx_receipt = w3.eth.wait_for_transaction_receipt(context.tx_hash)
    block = w3.eth.get_block(tx_receipt['blockNumber'])
    assert block is not None, "Block not found"
