import pytest
from unittest.mock import MagicMock
from web3 import Web3


@pytest.fixture
def operator_address():
    return Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266")


@pytest.fixture
def avs_address():
    return Web3.to_checksum_address("0x3333333333333333333333333333333333333333")


@pytest.fixture
def strategies():
    return [
        Web3.to_checksum_address("0x4444444444444444444444444444444444444444"),
        Web3.to_checksum_address("0x5555555555555555555555555555555555555555"),
    ]


@pytest.fixture
def magnitudes():
    return [100, 200]


@pytest.fixture
def operator_sets(avs_address, strategies, magnitudes):
    return [(avs_address, 1, strategies, magnitudes)]


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_allocation_manager():
    """Mock the allocation manager contract."""
    mock_contract = MagicMock()
    mock_contract.functions.modifyAllocations.return_value.transact.return_value = (
        "0xabcdef"
    )
    mock_contract.functions.clearDeallocationQueue.return_value.transact.return_value = (
        "0xabcdef"
    )
    mock_contract.functions.setAllocationDelay.return_value.transact.return_value = (
        "0xabcdef"
    )
    mock_contract.functions.deregisterFromOperatorSets.return_value.transact.return_value = (
        "0xabcdef"
    )
    return mock_contract


@pytest.fixture
def mock_eth_http_client():
    """Mock the Ethereum HTTP client."""
    mock_client = MagicMock()
    mock_client.eth.wait_for_transaction_receipt.return_value = {
        "transactionHash": "0xabcdef",
        "status": 1,
    }
    return mock_client


@pytest.fixture
def el_writer(mock_tx_mgr, mock_allocation_manager, mock_eth_http_client):
    """Inject mocks into el_writer."""
    from base import el_writer

    el_writer.tx_mgr = mock_tx_mgr
    el_writer.allocation_manager = mock_allocation_manager
    el_writer.eth_http_client = mock_eth_http_client
    return el_writer


@pytest.fixture
def nums_to_clear():
    """Fixture for nums_to_clear input"""
    return [1, 2]


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    return mock_tx_mgr


@pytest.fixture
def mock_allocation_manager():
    """Mock the allocation manager contract."""
    mock_contract = MagicMock()

    # Mock clearDeallocationQueue transaction
    mock_contract.functions.clearDeallocationQueue.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def delay():
    """Fixture for delay input"""
    return 120  # Example delay in seconds


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    return mock_tx_mgr


@pytest.fixture
def mock_allocation_manager():
    """Mock the allocation manager contract."""
    mock_contract = MagicMock()

    # Mock setAllocationDelay transaction
    mock_contract.functions.setAllocationDelay.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def request_data():
    """Fixture for request data including AVS address and operator set IDs."""
    return {
        "AVSAddress": Web3.to_checksum_address(
            "0x09635F643e140090A9A8Dcd712eD6285858ceBef"
        ),
        "OperatorSetIds": [1, 2, 3],  # Example operator set IDs
    }


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    return mock_tx_mgr


@pytest.fixture
def mock_allocation_manager():
    """Mock the allocation manager contract."""
    mock_contract = MagicMock()

    # Mock deregisterFromOperatorSets transaction
    mock_contract.functions.deregisterFromOperatorSets.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def request_data():
    """Fixture for request data including AVS address, operator address, and other parameters."""
    return {
        "AVSAddress": Web3.to_checksum_address(
            "0x09635F643e140090A9A8Dcd712eD6285858ceBef"
        ),
        "OperatorAddress": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "BlsKeyPair": bytes.fromhex(
            "a3d1e5f47b6c9f8e2d3c4b5a6e7f8d9c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d"
        ),
        "Socket": "test_socket",
        "OperatorSetIds": [1, 2, 3],
        "WaitForReceipt": True,
    }


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_allocation_manager():
    """Mock the allocation manager contract."""
    mock_contract = MagicMock()

    # Mock registerForOperatorSets transaction
    mock_contract.functions.registerForOperatorSets.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def mock_external_functions(mocker):
    """Mock external functions used in register_for_operator_sets."""
    mocker.patch(
        "base.getPubkeyRegistrationParams", return_value=b"mocked_pubkey_params"
    )
    mocker.patch(
        "base.AbiEncodeRegistrationParams", return_value=b"mocked_encoded_params"
    )


@pytest.fixture
def operator_data():
    """Fixture for operator details including address and delegation approver address."""
    return {
        "Address": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "DelegationApproverAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
    }


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_delegation_manager():
    """Mock the delegation manager contract."""
    mock_contract = MagicMock()

    # Mock modifyOperatorDetails transaction
    mock_contract.functions.modifyOperatorDetails.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def operator_data():
    """Fixture for operator details including address and delegation approver address."""
    return {
        "Address": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "DelegationApproverAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
    }


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_delegation_manager():
    """Mock the delegation manager contract."""
    mock_contract = MagicMock()

    # Mock modifyOperatorDetails transaction
    mock_contract.functions.modifyOperatorDetails.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def metadata_uri():
    """Fixture for operator metadata URI."""
    return "https://example.com/operator_metadata.json"


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_delegation_manager():
    """Mock the delegation manager contract."""
    mock_contract = MagicMock()

    # Mock updateOperatorMetadataURI transaction
    mock_contract.functions.updateOperatorMetadataURI.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def operator_data():
    """Fixture for operator details including address, delegation approver address, allocation delay, and metadata URL."""
    return {
        "Address": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "DelegationApproverAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
        "AllocationDelay": 100,
        "MetadataUrl": "https://example.com/operator_metadata.json",
    }


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_delegation_manager():
    """Mock the delegation manager contract."""
    mock_contract = MagicMock()

    # Mock registerAsOperator transaction
    mock_contract.functions.registerAsOperator.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def request_data():
    """Fixture for remove permission request."""
    return {
        "Address": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "PermissionId": 1,
        "WaitForReceipt": True,
    }


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_remove_permission_tx(mocker):
    """Mock NewRemovePermissionTx function."""
    return mocker.patch("base.NewRemovePermissionTx", return_value="0xabcdef")


@pytest.fixture
def tx_opts():
    """Fixture for transaction options."""
    return {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }


@pytest.fixture
def request_data():
    """Fixture for remove permission request."""
    return {
        "AccountAddress": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "AppointeeAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
        "Target": Web3.to_checksum_address(
            "0x3333333333333333333333333333333333333333"
        ),
        "Selector": "0xabcdef",
    }


@pytest.fixture
def mock_permission_control():
    """Mock the permission control contract."""
    mock_contract = MagicMock()

    # Mock removeAppointee transaction
    mock_contract.functions.removeAppointee.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def tx_opts():
    """Fixture for transaction options."""
    return {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }


@pytest.fixture
def request_data():
    """Fixture for set permission request."""
    return {
        "AccountAddress": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "AppointeeAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
        "Target": Web3.to_checksum_address(
            "0x3333333333333333333333333333333333333333"
        ),
        "Selector": "0xabcdef",
    }


@pytest.fixture
def mock_permission_control():
    """Mock the permission control contract."""
    mock_contract = MagicMock()

    # Mock setAppointee transaction
    mock_contract.functions.setAppointee.return_value.transact.return_value = "0xabcdef"

    return mock_contract


@pytest.fixture
def request_data():
    """Fixture for set permission request."""
    return {
        "AccountAddress": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "AppointeeAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
        "Target": Web3.to_checksum_address(
            "0x3333333333333333333333333333333333333333"
        ),
        "Selector": "0xabcdef",
        "WaitForReceipt": True,
    }


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_set_permission_tx(mocker):
    """Mock NewSetPermissionTx function."""
    return mocker.patch("base.NewSetPermissionTx", return_value="0xabcdef")


@pytest.fixture
def request_data():
    """Fixture for set permission request."""
    return {
        "AccountAddress": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "AppointeeAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
        "Target": Web3.to_checksum_address(
            "0x3333333333333333333333333333333333333333"
        ),
        "Selector": "0xabcdef",
        "WaitForReceipt": True,
    }


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_set_permission_tx(mocker):
    """Mock NewSetPermissionTx function."""
    return mocker.patch("base.NewSetPermissionTx", return_value="0xabcdef")


@pytest.fixture
def request_data():
    """Fixture for accept admin request."""
    return {
        "AdminAddress": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "WaitForReceipt": True,
    }


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_accept_admin_tx(mocker):
    """Mock NewAcceptAdminTx function."""
    return mocker.patch("base.NewAcceptAdminTx", return_value="0xabcdef")


@pytest.fixture
def tx_opts():
    """Fixture for transaction options."""
    return {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }


@pytest.fixture
def request_data():
    """Fixture for add pending admin request."""
    return {
        "AccountAddress": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "AdminAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
    }


@pytest.fixture
def mock_permission_control():
    """Mock the permission control contract."""
    mock_contract = MagicMock()

    # Mock addPendingAdmin transaction
    mock_contract.functions.addPendingAdmin.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def tx_opts():
    """Fixture for transaction options."""
    return {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }


@pytest.fixture
def request_data():
    """Fixture for remove admin request."""
    return {
        "AccountAddress": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "AdminAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
    }


@pytest.fixture
def mock_permission_control():
    """Mock the permission control contract."""
    mock_contract = MagicMock()

    # Mock removeAdmin transaction
    mock_contract.functions.removeAdmin.return_value.transact.return_value = "0xabcdef"

    return mock_contract


@pytest.fixture
def tx_opts():
    """Fixture for transaction options."""
    return {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }


@pytest.fixture
def request_data():
    """Fixture for remove pending admin request."""
    return {
        "AccountAddress": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "AdminAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
    }


@pytest.fixture
def mock_permission_control():
    """Mock the permission control contract."""
    mock_contract = MagicMock()

    # Mock RemovePendingAdmin transaction
    mock_contract.functions.RemovePendingAdmin.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def request_data():
    """Fixture for remove pending admin request."""
    return {
        "AccountAddress": Web3.to_checksum_address(
            "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
        ),
        "AdminAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
        "WaitForReceipt": True,
    }


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_remove_pending_admin_tx(mocker):
    """Mock NewRemovePendingAdminTx function."""
    return mocker.patch("base.NewRemovePendingAdminTx", return_value="0xabcdef")


@pytest.fixture
def claimer():
    """Fixture for claimer address."""
    return Web3.to_checksum_address("0x1111111111111111111111111111111111111111")


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_reward_coordinator():
    """Mock the RewardsCoordinator contract."""
    mock_contract = MagicMock()

    # Mock setClaimerFor transaction
    mock_contract.functions.setClaimerFor.return_value.build_transaction.return_value = {
        "to": "0x2222222222222222222222222222222222222222",
        "from": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
        "gas": 21000,
        "nonce": 1,
        "data": "0xabcdef",
    }

    return mock_contract


@pytest.fixture
def claim():
    """Fixture for claim data."""
    return {"amount": 100, "nonce": 1, "signature": "0xabcdef"}


@pytest.fixture
def recipient_address():
    """Fixture for recipient address."""
    return Web3.to_checksum_address("0x3333333333333333333333333333333333333333")


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 21000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_reward_coordinator():
    """Mock the RewardsCoordinator contract."""
    mock_contract = MagicMock()

    # Mock processClaims transaction
    mock_contract.functions.processClaims.return_value.build_transaction.return_value = {
        "to": "0x2222222222222222222222222222222222222222",
        "from": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
        "gas": 21000,
        "nonce": 1,
        "data": "0xabcdef",
    }

    return mock_contract


@pytest.fixture
def operator():
    """Fixture for operator address."""
    return Web3.to_checksum_address("0x1111111111111111111111111111111111111111")


@pytest.fixture
def avs():
    """Fixture for AVS address."""
    return Web3.to_checksum_address("0x2222222222222222222222222222222222222222")


@pytest.fixture
def split():
    """Fixture for split value."""
    return 50  # Example split value


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and signing."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 210000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.private_key = (
        "0xabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef"
    )
    return mock_tx_mgr


@pytest.fixture
def mock_eth_http_client():
    """Mock Web3 Ethereum client."""
    mock_client = MagicMock()

    # Mock eth functions
    mock_client.eth.default_account = Web3.to_checksum_address(
        "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
    )
    mock_client.eth.get_transaction_count.return_value = 10
    mock_client.eth.gas_price = Web3.to_wei(20, "gwei")
    mock_client.eth.send_raw_transaction.return_value = b"\x12\x34"
    mock_client.eth.wait_for_transaction_receipt.return_value = {
        "transactionHash": "0xabcdef"
    }

    return mock_client


@pytest.fixture
def mock_reward_coordinator():
    """Mock the RewardsCoordinator contract."""
    mock_contract = MagicMock()

    # Mock setOperatorAVSSplit transaction
    mock_contract.functions.setOperatorAVSSplit.return_value.build_transaction.return_value = {
        "to": "0x2222222222222222222222222222222222222222",
        "from": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
        "gas": 210000,
        "nonce": 10,
        "data": "0xabcdef",
    }

    return mock_contract


@pytest.fixture
def operator():
    """Fixture for operator address."""
    return Web3.to_checksum_address("0x1111111111111111111111111111111111111111")


@pytest.fixture
def avs():
    """Fixture for AVS address."""
    return Web3.to_checksum_address("0x2222222222222222222222222222222222222222")


@pytest.fixture
def split():
    """Fixture for split value."""
    return 50  # Example split value


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and signing."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 210000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.private_key = (
        "0xabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef"
    )
    return mock_tx_mgr


@pytest.fixture
def mock_eth_http_client():
    """Mock Web3 Ethereum client."""
    mock_client = MagicMock()

    # Mock eth functions
    mock_client.eth.default_account = Web3.to_checksum_address(
        "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
    )
    mock_client.eth.get_transaction_count.return_value = 10
    mock_client.eth.gas_price = Web3.to_wei(20, "gwei")
    mock_client.eth.send_raw_transaction.return_value = b"\x12\x34"
    mock_client.eth.wait_for_transaction_receipt.return_value = {
        "transactionHash": "0xabcdef"
    }

    return mock_client


@pytest.fixture
def mock_reward_coordinator():
    """Mock the RewardsCoordinator contract."""
    mock_contract = MagicMock()

    # Mock setOperatorAVSSplit transaction
    mock_contract.functions.setOperatorAVSSplit.return_value.build_transaction.return_value = {
        "to": "0x2222222222222222222222222222222222222222",
        "from": "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
        "gas": 210000,
        "nonce": 10,
        "data": "0xabcdef",
    }

    return mock_contract


@pytest.fixture
def operator():
    """Fixture for operator address."""
    return Web3.to_checksum_address("0x1111111111111111111111111111111111111111")


@pytest.fixture
def split():
    """Fixture for split value."""
    return 50  # Example split value


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 210000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_reward_coordinator():
    """Mock the RewardsCoordinator contract."""
    mock_contract = MagicMock()

    # Mock setOperatorPISplit transaction
    mock_contract.functions.setOperatorPISplit.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def operator():
    """Fixture for operator address."""
    return Web3.to_checksum_address("0x1111111111111111111111111111111111111111")


@pytest.fixture
def operator_set():
    """Fixture for operator set data."""
    return {
        "AVSAddress": Web3.to_checksum_address(
            "0x2222222222222222222222222222222222222222"
        ),
        "OperatorSetIds": [1, 2, 3],  # Example operator set IDs
    }


@pytest.fixture
def split():
    """Fixture for split value."""
    return 50  # Example split value


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 210000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_reward_coordinator():
    """Mock the RewardsCoordinator contract."""
    mock_contract = MagicMock()

    # Mock setOperatorSetSplit transaction
    mock_contract.functions.setOperatorSetSplit.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


@pytest.fixture
def claims():
    """Fixture for multiple claim data."""
    return [
        {"amount": 100, "nonce": 1, "signature": "0xabcdef"},
        {"amount": 200, "nonce": 2, "signature": "0x123456"},
    ]


@pytest.fixture
def recipient_address():
    """Fixture for recipient address."""
    return Web3.to_checksum_address("0x3333333333333333333333333333333333333333")


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 210000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_reward_coordinator():
    """Mock the RewardsCoordinator contract."""
    mock_contract = MagicMock()

    # Mock processClaims transaction
    mock_contract.functions.processClaims.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract


import pytest
from web3.exceptions import TransactionNotFound


def test_process_claims_success(
    claims, recipient_address, el_writer, mock_reward_coordinator
):
    """Test process_claims() with valid inputs."""
    try:
        receipt = el_writer.process_claims(
            claims, recipient_address, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_process_claims_missing_reward_coordinator(
    claims, recipient_address, el_writer
):
    """Test ValueError when reward_cordinator is missing."""

    # Set reward_cordinator to None
    el_writer.reward_cordinator = None

    with pytest.raises(ValueError, match="RewardsCoordinator contract not provided"):
        el_writer.process_claims(claims, recipient_address, wait_for_receipt=True)


def test_process_claims_empty_claims_list(recipient_address, el_writer):
    """Test ValueError when claims list is empty."""

    with pytest.raises(
        ValueError, match="claims is empty, at least one claim must be provided"
    ):
        el_writer.process_claims([], recipient_address, wait_for_receipt=True)


def test_process_claims_tx_opts_failure(
    claims, recipient_address, el_writer, mock_tx_mgr
):
    """Simulate a failure when retrieving transaction options."""

    # Modify the mock to raise an error
    mock_tx_mgr.get_no_send_tx_opts.side_effect = Exception(
        "Failed to get transaction options"
    )

    with pytest.raises(
        ValueError,
        match="failed to get no send tx opts: Failed to get transaction options",
    ):
        el_writer.process_claims(claims, recipient_address, wait_for_receipt=True)


def test_process_claims_tx_execution_failure(
    claims, recipient_address, el_writer, mock_reward_coordinator
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_reward_coordinator.functions.processClaims.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create ProcessClaims tx: Transaction execution failed",
    ):
        el_writer.process_claims(claims, recipient_address, wait_for_receipt=True)


def test_process_claims_tx_receipt_failure(
    claims, recipient_address, el_writer, mock_tx_mgr
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.process_claims(claims, recipient_address, wait_for_receipt=True)


@pytest.fixture
def strategy_addr():
    """Fixture for strategy address."""
    return Web3.to_checksum_address("0x1111111111111111111111111111111111111111")


@pytest.fixture
def underlying_token_addr():
    """Fixture for underlying ERC20 token address."""
    return Web3.to_checksum_address("0x2222222222222222222222222222222222222222")


@pytest.fixture
def amount():
    """Fixture for token amount."""
    return 1000  # Example deposit amount


@pytest.fixture
def mock_tx_mgr():
    """Mock the TxManager for transaction options and sending."""
    mock_tx_mgr = MagicMock()
    mock_tx_mgr.get_no_send_tx_opts.return_value = {
        "from": Web3.to_checksum_address("0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"),
        "nonce": 1,
        "gas": 210000,
        "maxFeePerGas": Web3.to_wei(5, "gwei"),
        "maxPriorityFeePerGas": Web3.to_wei(2, "gwei"),
    }
    mock_tx_mgr.send.return_value = {"transactionHash": "0xabcdef"}
    return mock_tx_mgr


@pytest.fixture
def mock_el_chain_reader():
    """Mock the ELChainReader for fetching strategy and ERC20 token details."""
    mock_reader = MagicMock()

    # Mock GetStrategyAndUnderlyingERC20Token response
    mock_reader.GetStrategyAndUnderlyingERC20Token.return_value = (
        MagicMock(),  # Strategy contract mock
        MagicMock(),  # Underlying token contract mock
        Web3.to_checksum_address("0x2222222222222222222222222222222222222222"),
    )

    return mock_reader


@pytest.fixture
def mock_underlying_token_contract():
    """Mock the ERC20 token contract."""
    mock_contract = MagicMock()

    # Mock Approve transaction
    mock_contract.functions.Approve.return_value.transact.return_value = "0xabcdef"

    return mock_contract


@pytest.fixture
def mock_strategy_manager():
    """Mock the StrategyManager contract."""
    mock_contract = MagicMock()

    # Mock depositIntoStrategyWithSignature transaction
    mock_contract.functions.depositIntoStrategyWithSignature.return_value.transact.return_value = (
        "0xabcdef"
    )

    return mock_contract
