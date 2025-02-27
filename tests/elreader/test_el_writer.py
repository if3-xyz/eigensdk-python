import pytest
from web3.exceptions import ContractLogicError, TransactionNotFound
from conftest import *


def test_modify_allocations_success(operator_address, operator_sets, el_writer):
    """Test modify_allocations() with valid inputs."""
    try:
        receipt = el_writer.modify_allocations(
            operator_address, operator_sets, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_modify_allocations_contract_error(
    operator_address, operator_sets, el_writer, mock_allocation_manager
):
    """Simulate a ContractLogicError when calling modify_allocations()."""

    # Modify the mock to raise ContractLogicError
    mock_allocation_manager.functions.modifyAllocations.return_value.transact.side_effect = ContractLogicError(
        "Contract execution failed"
    )

    with pytest.raises(ContractLogicError, match="Contract execution failed"):
        el_writer.modify_allocations(
            operator_address, operator_sets, wait_for_receipt=True
        )


def test_modify_allocations_transaction_not_found(
    operator_address, operator_sets, el_writer, mock_eth_http_client
):
    """Simulate a TransactionNotFound error."""

    # Modify the mock to raise TransactionNotFound error
    mock_eth_http_client.eth.wait_for_transaction_receipt.side_effect = (
        TransactionNotFound
    )

    with pytest.raises(TransactionNotFound):
        el_writer.modify_allocations(
            operator_address, operator_sets, wait_for_receipt=True
        )


def test_modify_allocations_value_error(
    operator_address, operator_sets, el_writer, mock_allocation_manager
):
    """Simulate a ValueError when calling modify_allocations()."""

    # Modify the mock to raise ValueError
    mock_allocation_manager.functions.modifyAllocations.return_value.transact.side_effect = ValueError(
        "Invalid allocation data"
    )

    with pytest.raises(ValueError, match="Invalid allocation data"):
        el_writer.modify_allocations(
            operator_address, operator_sets, wait_for_receipt=True
        )


def test_clear_deallocation_queue_success(
    operator_address, strategies, nums_to_clear, el_writer
):
    """Test clear_deallocation_queue() with valid inputs."""
    try:
        receipt = el_writer.clear_deallocation_queue(
            operator_address, strategies, nums_to_clear, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_clear_deallocation_queue_missing_allocation_manager(
    operator_address, strategies, nums_to_clear, el_writer
):
    """Test ValueError when allocation_manager is missing."""

    # Set allocation_manager to None
    el_writer.allocation_manager = None

    with pytest.raises(ValueError, match="AllocationManager contract not provided"):
        el_writer.clear_deallocation_queue(
            operator_address, strategies, nums_to_clear, wait_for_receipt=True
        )


def test_clear_deallocation_queue_tx_opts_failure(
    operator_address, strategies, nums_to_clear, el_writer, mock_tx_mgr
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
        el_writer.clear_deallocation_queue(
            operator_address, strategies, nums_to_clear, wait_for_receipt=True
        )


def test_clear_deallocation_queue_tx_creation_failure(
    operator_address, strategies, nums_to_clear, el_writer, mock_allocation_manager
):
    """Simulate a failure when creating the transaction."""

    # Modify the mock to raise an error
    mock_allocation_manager.functions.clearDeallocationQueue.return_value.transact.side_effect = Exception(
        "Transaction creation failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create ClearDeallocationQueue tx: Transaction creation failed",
    ):
        el_writer.clear_deallocation_queue(
            operator_address, strategies, nums_to_clear, wait_for_receipt=True
        )


def test_clear_deallocation_queue_tx_receipt_failure(
    operator_address, strategies, nums_to_clear, el_writer, mock_eth_http_client
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_eth_http_client.eth.wait_for_transaction_receipt.side_effect = Exception(
        "Failed to get transaction receipt"
    )

    with pytest.raises(
        ValueError,
        match="failed to get transaction receipt: Failed to get transaction receipt",
    ):
        el_writer.clear_deallocation_queue(
            operator_address, strategies, nums_to_clear, wait_for_receipt=True
        )


def test_set_allocation_delay_success(operator_address, delay, el_writer):
    """Test set_allocation_delay() with valid inputs."""
    try:
        receipt = el_writer.set_allocation_delay(
            operator_address, delay, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_set_allocation_delay_missing_allocation_manager(
    operator_address, delay, el_writer
):
    """Test ValueError when allocation_manager is missing."""

    # Set allocation_manager to None
    el_writer.allocation_manager = None

    with pytest.raises(ValueError, match="AllocationManager contract not provided"):
        el_writer.set_allocation_delay(operator_address, delay, wait_for_receipt=True)


def test_set_allocation_delay_tx_opts_failure(
    operator_address, delay, el_writer, mock_tx_mgr
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
        el_writer.set_allocation_delay(operator_address, delay, wait_for_receipt=True)


def test_set_allocation_delay_tx_execution_failure(
    operator_address, delay, el_writer, mock_allocation_manager
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_allocation_manager.functions.setAllocationDelay.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError, match="failed to send tx: Transaction execution failed"
    ):
        el_writer.set_allocation_delay(operator_address, delay, wait_for_receipt=True)


def test_set_allocation_delay_tx_receipt_failure(
    operator_address, delay, el_writer, mock_eth_http_client
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_eth_http_client.eth.wait_for_transaction_receipt.side_effect = Exception(
        "Failed to get transaction receipt"
    )

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to get transaction receipt"
    ):
        el_writer.set_allocation_delay(operator_address, delay, wait_for_receipt=True)


def test_deregister_from_operator_sets_success(
    operator_address, request_data, el_writer
):
    """Test deregister_from_operator_sets() with valid inputs."""
    try:
        receipt = el_writer.deregister_from_operator_sets(
            operator_address, request_data
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_deregister_from_operator_sets_missing_allocation_manager(
    operator_address, request_data, el_writer
):
    """Test ValueError when allocation_manager is missing."""

    # Set allocation_manager to None
    el_writer.allocation_manager = None

    with pytest.raises(ValueError, match="AllocationManager contract not provided"):
        el_writer.deregister_from_operator_sets(operator_address, request_data)


def test_deregister_from_operator_sets_tx_opts_failure(
    operator_address, request_data, el_writer, mock_tx_mgr
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
        el_writer.deregister_from_operator_sets(operator_address, request_data)


def test_deregister_from_operator_sets_tx_execution_failure(
    operator_address, request_data, el_writer, mock_allocation_manager
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_allocation_manager.functions.deregisterFromOperatorSets.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create DeregisterFromOperatorSets tx: Transaction execution failed",
    ):
        el_writer.deregister_from_operator_sets(operator_address, request_data)


def test_deregister_from_operator_sets_tx_receipt_failure(
    operator_address, request_data, el_writer, mock_eth_http_client
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_eth_http_client.eth.wait_for_transaction_receipt.side_effect = Exception(
        "Failed to get transaction receipt"
    )

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to get transaction receipt"
    ):
        el_writer.deregister_from_operator_sets(operator_address, request_data)


def test_deregister_from_operator_sets_invalid_operator_set_ids(
    operator_address, el_writer
):
    """Test ValueError when OperatorSetIds contains non-integer values."""

    invalid_request_data = {
        "AVSAddress": Web3.to_checksum_address(
            "0x09635F643e140090A9A8Dcd712eD6285858ceBef"
        ),
        "OperatorSetIds": ["one", "two", "three"],  # Invalid non-integer values
    }

    with pytest.raises(ValueError, match="invalid literal for int()"):
        el_writer.deregister_from_operator_sets(operator_address, invalid_request_data)


def test_register_for_operator_sets_success(
    registry_coordinator_addr, request_data, el_writer, mock_external_functions
):
    """Test register_for_operator_sets() with valid inputs."""
    try:
        receipt = el_writer.register_for_operator_sets(
            registry_coordinator_addr, request_data
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_register_for_operator_sets_missing_allocation_manager(
    registry_coordinator_addr, request_data, el_writer
):
    """Test ValueError when allocation_manager is missing."""

    # Set allocation_manager to None
    el_writer.allocation_manager = None

    with pytest.raises(ValueError, match="AllocationManager contract not provided"):
        el_writer.register_for_operator_sets(registry_coordinator_addr, request_data)


def test_register_for_operator_sets_tx_opts_failure(
    registry_coordinator_addr, request_data, el_writer, mock_tx_mgr
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
        el_writer.register_for_operator_sets(registry_coordinator_addr, request_data)


def test_register_for_operator_sets_pubkey_params_failure(
    registry_coordinator_addr, request_data, el_writer, mocker
):
    """Simulate a failure when getting public key registration params."""

    # Modify the mock to raise an error
    mocker.patch(
        "base.getPubkeyRegistrationParams",
        side_effect=Exception("Public key params error"),
    )

    with pytest.raises(
        ValueError,
        match="failed to get public key registration params: Public key params error",
    ):
        el_writer.register_for_operator_sets(registry_coordinator_addr, request_data)


def test_register_for_operator_sets_encoding_failure(
    registry_coordinator_addr, request_data, el_writer, mocker
):
    """Simulate a failure when encoding registration params."""

    # Modify the mock to raise an error
    mocker.patch(
        "base.AbiEncodeRegistrationParams", side_effect=Exception("Encoding failed")
    )

    with pytest.raises(
        ValueError, match="failed to encode registration params: Encoding failed"
    ):
        el_writer.register_for_operator_sets(registry_coordinator_addr, request_data)


def test_register_for_operator_sets_tx_execution_failure(
    registry_coordinator_addr, request_data, el_writer, mock_allocation_manager
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_allocation_manager.functions.registerForOperatorSets.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create RegisterForOperatorSets tx: Transaction execution failed",
    ):
        el_writer.register_for_operator_sets(registry_coordinator_addr, request_data)


def test_register_for_operator_sets_tx_receipt_failure(
    registry_coordinator_addr, request_data, el_writer, mock_tx_mgr
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.register_for_operator_sets(registry_coordinator_addr, request_data)


def test_update_operator_details_success(operator_data, el_writer):
    """Test update_operator_details() with valid inputs."""
    try:
        receipt = el_writer.update_operator_details(
            operator_data, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_update_operator_details_missing_delegation_manager(operator_data, el_writer):
    """Test ValueError when delegation_manager is missing."""

    # Set delegation_manager to None
    el_writer.delegation_manager = None

    with pytest.raises(ValueError, match="DelegationManager contract not provided"):
        el_writer.update_operator_details(operator_data, wait_for_receipt=True)


def test_update_operator_details_tx_opts_failure(operator_data, el_writer, mock_tx_mgr):
    """Simulate a failure when retrieving transaction options."""

    # Modify the mock to raise an error
    mock_tx_mgr.get_no_send_tx_opts.side_effect = Exception(
        "Failed to get transaction options"
    )

    with pytest.raises(
        ValueError,
        match="failed to get no send tx opts: Failed to get transaction options",
    ):
        el_writer.update_operator_details(operator_data, wait_for_receipt=True)


def test_update_operator_details_tx_execution_failure(
    operator_data, el_writer, mock_delegation_manager
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_delegation_manager.functions.modifyOperatorDetails.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create ModifyOperatorDetails tx: Transaction execution failed",
    ):
        el_writer.update_operator_details(operator_data, wait_for_receipt=True)


def test_update_operator_details_tx_receipt_failure(
    operator_data, el_writer, mock_tx_mgr
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.update_operator_details(operator_data, wait_for_receipt=True)


def test_update_meta_data_uri_success(operator_address, metadata_uri, el_writer):
    """Test update_meta_data_uri() with valid inputs."""
    try:
        receipt = el_writer.update_meta_data_uri(
            operator_address, metadata_uri, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_update_meta_data_uri_missing_delegation_manager(
    operator_address, metadata_uri, el_writer
):
    """Test ValueError when delegation_manager is missing."""

    # Set delegation_manager to None
    el_writer.delegation_manager = None

    with pytest.raises(ValueError, match="DelegationManager contract not provided"):
        el_writer.update_meta_data_uri(
            operator_address, metadata_uri, wait_for_receipt=True
        )


def test_update_meta_data_uri_tx_opts_failure(
    operator_address, metadata_uri, el_writer, mock_tx_mgr
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
        el_writer.update_meta_data_uri(
            operator_address, metadata_uri, wait_for_receipt=True
        )


def test_update_meta_data_uri_tx_execution_failure(
    operator_address, metadata_uri, el_writer, mock_delegation_manager
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_delegation_manager.functions.updateOperatorMetadataURI.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create UpdateOperatorMetadataURI tx: Transaction execution failed",
    ):
        el_writer.update_meta_data_uri(
            operator_address, metadata_uri, wait_for_receipt=True
        )


def test_update_meta_data_uri_tx_receipt_failure(
    operator_address, metadata_uri, el_writer, mock_tx_mgr
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.update_meta_data_uri(
            operator_address, metadata_uri, wait_for_receipt=True
        )


def test_register_as_operator_success(operator_data, el_writer):
    """Test register_as_operator() with valid inputs."""
    try:
        receipt = el_writer.register_as_operator(operator_data, wait_for_receipt=True)

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_register_as_operator_missing_delegation_manager(operator_data, el_writer):
    """Test ValueError when delegation_manager is missing."""

    # Set delegation_manager to None
    el_writer.delegation_manager = None

    with pytest.raises(ValueError, match="DelegationManager contract not provided"):
        el_writer.register_as_operator(operator_data, wait_for_receipt=True)


def test_register_as_operator_tx_opts_failure(operator_data, el_writer, mock_tx_mgr):
    """Simulate a failure when retrieving transaction options."""

    # Modify the mock to raise an error
    mock_tx_mgr.get_no_send_tx_opts.side_effect = Exception(
        "Failed to get transaction options"
    )

    with pytest.raises(
        ValueError,
        match="failed to get no send tx opts: Failed to get transaction options",
    ):
        el_writer.register_as_operator(operator_data, wait_for_receipt=True)


def test_register_as_operator_tx_execution_failure(
    operator_data, el_writer, mock_delegation_manager
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_delegation_manager.functions.registerAsOperator.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create RegisterAsOperator tx: Transaction execution failed",
    ):
        el_writer.register_as_operator(operator_data, wait_for_receipt=True)


def test_register_as_operator_tx_receipt_failure(operator_data, el_writer, mock_tx_mgr):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.register_as_operator(operator_data, wait_for_receipt=True)


import pytest
from web3.exceptions import TransactionNotFound


def test_remove_permission_success(request_data, el_writer, mock_remove_permission_tx):
    """Test remove_permission() with valid inputs."""
    try:
        receipt = el_writer.remove_permission(request_data)

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_remove_permission_tx_opts_failure(request_data, el_writer, mock_tx_mgr):
    """Simulate a failure when retrieving transaction options."""

    # Modify the mock to raise an error
    mock_tx_mgr.get_no_send_tx_opts.side_effect = Exception(
        "Failed to get transaction options"
    )

    with pytest.raises(
        ValueError,
        match="failed to get no-send tx opts: Failed to get transaction options",
    ):
        el_writer.remove_permission(request_data)


def test_remove_permission_tx_creation_failure(request_data, el_writer, mocker):
    """Simulate a failure when creating the transaction."""

    # Modify the mock to raise an error
    mocker.patch(
        "base.NewRemovePermissionTx",
        side_effect=Exception("Transaction creation failed"),
    )

    with pytest.raises(
        ValueError,
        match="failed to create NewRemovePermissionTx: Transaction creation failed",
    ):
        el_writer.remove_permission(request_data)


def test_remove_permission_tx_receipt_failure(request_data, el_writer, mock_tx_mgr):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.remove_permission(request_data)


import pytest


def test_new_remove_permission_tx_success(tx_opts, request_data, el_writer):
    """Test new_remove_permission_tx() with valid inputs."""
    try:
        tx_hash = el_writer.new_remove_permission_tx(tx_opts, request_data)

        # Assertions
        assert tx_hash is not None, "Expected a valid transaction hash, got None"
        assert isinstance(tx_hash, str), "Expected transaction hash to be a string"
        assert tx_hash.startswith("0x"), "Expected transaction hash to start with '0x'"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_new_remove_permission_tx_missing_permission_control(
    tx_opts, request_data, el_writer
):
    """Test ValueError when permissioncontrol is missing."""

    # Set permissioncontrol to None
    el_writer.permissioncontrol = None

    with pytest.raises(ValueError, match="permission contract not provided"):
        el_writer.new_remove_permission_tx(tx_opts, request_data)


def test_new_remove_permission_tx_execution_failure(
    tx_opts, request_data, el_writer, mock_permission_control
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_permission_control.functions.removeAppointee.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create RemovePermission tx: Transaction execution failed",
    ):
        el_writer.new_remove_permission_tx(tx_opts, request_data)


import pytest


def test_new_set_permission_tx_success(tx_opts, request_data, el_writer):
    """Test new_set_permission_tx() with valid inputs."""
    try:
        tx_hash = el_writer.new_set_permission_tx(tx_opts, request_data)

        # Assertions
        assert tx_hash is not None, "Expected a valid transaction hash, got None"
        assert isinstance(tx_hash, str), "Expected transaction hash to be a string"
        assert tx_hash.startswith("0x"), "Expected transaction hash to start with '0x'"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_new_set_permission_tx_missing_permission_control(
    tx_opts, request_data, el_writer
):
    """Test ValueError when permissioncontrol is missing."""

    # Set permissioncontrol to None
    el_writer.permissioncontrol = None

    with pytest.raises(ValueError, match="permission contract not provided"):
        el_writer.new_set_permission_tx(tx_opts, request_data)


def test_new_set_permission_tx_execution_failure(
    tx_opts, request_data, el_writer, mock_permission_control
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_permission_control.functions.setAppointee.return_value.transact.side_effect = (
        Exception("Transaction execution failed")
    )

    with pytest.raises(
        ValueError,
        match="failed to create SetPermission tx: Transaction execution failed",
    ):
        el_writer.new_set_permission_tx(tx_opts, request_data)


import pytest
from web3.exceptions import TransactionNotFound


def test_set_permission_success(request_data, el_writer, mock_set_permission_tx):
    """Test set_permission() with valid inputs."""
    try:
        receipt = el_writer.set_permission(request_data)

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_set_permission_tx_opts_failure(request_data, el_writer, mock_tx_mgr):
    """Simulate a failure when retrieving transaction options."""

    # Modify the mock to raise an error
    mock_tx_mgr.get_no_send_tx_opts.side_effect = Exception(
        "Failed to get transaction options"
    )

    with pytest.raises(
        ValueError,
        match="failed to get no-send tx opts: Failed to get transaction options",
    ):
        el_writer.set_permission(request_data)


def test_set_permission_tx_creation_failure(request_data, el_writer, mocker):
    """Simulate a failure when creating the transaction."""

    # Modify the mock to raise an error
    mocker.patch(
        "base.NewSetPermissionTx", side_effect=Exception("Transaction creation failed")
    )

    with pytest.raises(
        ValueError,
        match="failed to create NewSetPermissionTx: Transaction creation failed",
    ):
        el_writer.set_permission(request_data)


def test_set_permission_tx_receipt_failure(request_data, el_writer, mock_tx_mgr):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.set_permission(request_data)


import pytest
from web3.exceptions import TransactionNotFound


def test_set_permission_success(request_data, el_writer, mock_set_permission_tx):
    """Test set_permission() with valid inputs."""
    try:
        receipt = el_writer.set_permission(request_data)

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_set_permission_tx_opts_failure(request_data, el_writer, mock_tx_mgr):
    """Simulate a failure when retrieving transaction options."""

    # Modify the mock to raise an error
    mock_tx_mgr.get_no_send_tx_opts.side_effect = Exception(
        "Failed to get transaction options"
    )

    with pytest.raises(
        ValueError,
        match="failed to get no-send tx opts: Failed to get transaction options",
    ):
        el_writer.set_permission(request_data)


def test_set_permission_tx_creation_failure(request_data, el_writer, mocker):
    """Simulate a failure when creating the transaction."""

    # Modify the mock to raise an error
    mocker.patch(
        "base.NewSetPermissionTx", side_effect=Exception("Transaction creation failed")
    )

    with pytest.raises(
        ValueError,
        match="failed to create NewSetPermissionTx: Transaction creation failed",
    ):
        el_writer.set_permission(request_data)


def test_set_permission_tx_receipt_failure(request_data, el_writer, mock_tx_mgr):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.set_permission(request_data)


import pytest
from web3.exceptions import TransactionNotFound


def test_accept_admin_success(request_data, el_writer, mock_accept_admin_tx):
    """Test accept_admin() with valid inputs."""
    try:
        receipt = el_writer.accept_admin(request_data)

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_accept_admin_tx_opts_failure(request_data, el_writer, mock_tx_mgr):
    """Simulate a failure when retrieving transaction options."""

    # Modify the mock to raise an error
    mock_tx_mgr.get_no_send_tx_opts.side_effect = Exception(
        "Failed to get transaction options"
    )

    with pytest.raises(
        ValueError,
        match="failed to get no send tx opts: Failed to get transaction options",
    ):
        el_writer.accept_admin(request_data)


def test_accept_admin_tx_creation_failure(request_data, el_writer, mocker):
    """Simulate a failure when creating the transaction."""

    # Modify the mock to raise an error
    mocker.patch(
        "base.NewAcceptAdminTx", side_effect=Exception("Transaction creation failed")
    )

    with pytest.raises(
        ValueError,
        match="failed to create AcceptAdmin transaction: Transaction creation failed",
    ):
        el_writer.accept_admin(request_data)


def test_accept_admin_tx_receipt_failure(request_data, el_writer, mock_tx_mgr):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.accept_admin(request_data)


import pytest


def test_new_add_pending_admin_tx_success(tx_opts, request_data, el_writer):
    """Test new_add_pending_admin_tx() with valid inputs."""
    try:
        tx_hash = el_writer.new_add_pending_admin_tx(tx_opts, request_data)

        # Assertions
        assert tx_hash is not None, "Expected a valid transaction hash, got None"
        assert isinstance(tx_hash, str), "Expected transaction hash to be a string"
        assert tx_hash.startswith("0x"), "Expected transaction hash to start with '0x'"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_new_add_pending_admin_tx_missing_permission_control(
    tx_opts, request_data, el_writer
):
    """Test ValueError when permissioncontrol is missing."""

    # Set permissioncontrol to None
    el_writer.permissioncontrol = None

    with pytest.raises(ValueError, match="permission contract not provided"):
        el_writer.new_add_pending_admin_tx(tx_opts, request_data)


def test_new_add_pending_admin_tx_execution_failure(
    tx_opts, request_data, el_writer, mock_permission_control
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_permission_control.functions.addPendingAdmin.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create AddPendingAdmin tx: Transaction execution failed",
    ):
        el_writer.new_add_pending_admin_tx(tx_opts, request_data)


import pytest


def test_new_remove_admin_tx_success(tx_opts, request_data, el_writer):
    """Test new_remove_admin_tx() with valid inputs."""
    try:
        tx_hash = el_writer.new_remove_admin_tx(tx_opts, request_data)

        # Assertions
        assert tx_hash is not None, "Expected a valid transaction hash, got None"
        assert isinstance(tx_hash, str), "Expected transaction hash to be a string"
        assert tx_hash.startswith("0x"), "Expected transaction hash to start with '0x'"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_new_remove_admin_tx_missing_permission_control(
    tx_opts, request_data, el_writer
):
    """Test ValueError when permissioncontrol is missing."""

    # Set permissioncontrol to None
    el_writer.permissioncontrol = None

    with pytest.raises(ValueError, match="permission contract not provided"):
        el_writer.new_remove_admin_tx(tx_opts, request_data)


def test_new_remove_admin_tx_execution_failure(
    tx_opts, request_data, el_writer, mock_permission_control
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_permission_control.functions.removeAdmin.return_value.transact.side_effect = (
        Exception("Transaction execution failed")
    )

    with pytest.raises(
        ValueError,
        match="failed to create RemoveAdmin tx: Transaction execution failed",
    ):
        el_writer.new_remove_admin_tx(tx_opts, request_data)


import pytest


def test_new_remove_pending_admin_tx_success(tx_opts, request_data, el_writer):
    """Test new_remove_pending_admin_tx() with valid inputs."""
    try:
        tx_hash = el_writer.new_remove_pending_admin_tx(tx_opts, request_data)

        # Assertions
        assert tx_hash is not None, "Expected a valid transaction hash, got None"
        assert isinstance(tx_hash, str), "Expected transaction hash to be a string"
        assert tx_hash.startswith("0x"), "Expected transaction hash to start with '0x'"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_new_remove_pending_admin_tx_missing_permission_control(
    tx_opts, request_data, el_writer
):
    """Test ValueError when permissioncontrol is missing."""

    # Set permissioncontrol to None
    el_writer.permissioncontrol = None

    with pytest.raises(ValueError, match="permission contract not provided"):
        el_writer.new_remove_pending_admin_tx(tx_opts, request_data)


def test_new_remove_pending_admin_tx_execution_failure(
    tx_opts, request_data, el_writer, mock_permission_control
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_permission_control.functions.RemovePendingAdmin.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create RemovePendingAdmin tx: Transaction execution failed",
    ):
        el_writer.new_remove_pending_admin_tx(tx_opts, request_data)


import pytest
from web3.exceptions import TransactionNotFound


def test_remove_pending_admin_success(
    request_data, el_writer, mock_remove_pending_admin_tx
):
    """Test remove_pending_admin() with valid inputs."""
    try:
        receipt = el_writer.remove_pending_admin(request_data)

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_remove_pending_admin_tx_opts_failure(request_data, el_writer, mock_tx_mgr):
    """Simulate a failure when retrieving transaction options."""

    # Modify the mock to raise an error
    mock_tx_mgr.get_no_send_tx_opts.side_effect = Exception(
        "Failed to get transaction options"
    )

    with pytest.raises(
        ValueError,
        match="failed to get no send tx opts: Failed to get transaction options",
    ):
        el_writer.remove_pending_admin(request_data)


def test_remove_pending_admin_tx_creation_failure(request_data, el_writer, mocker):
    """Simulate a failure when creating the transaction."""

    # Modify the mock to raise an error
    mocker.patch(
        "base.NewRemovePendingAdminTx",
        side_effect=Exception("Transaction creation failed"),
    )

    with pytest.raises(
        ValueError,
        match="failed to create RemovePendingAdmin transaction: Transaction creation failed",
    ):
        el_writer.remove_pending_admin(request_data)


def test_remove_pending_admin_tx_receipt_failure(request_data, el_writer, mock_tx_mgr):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.remove_pending_admin(request_data)


import pytest
from web3.exceptions import TransactionNotFound


def test_set_claimer_for_success(claimer, el_writer, mock_reward_coordinator):
    """Test set_claimer_for() with valid inputs."""
    try:
        receipt = el_writer.set_claimer_for(claimer, wait_for_receipt=True)

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_set_claimer_for_missing_reward_coordinator(claimer, el_writer):
    """Test ValueError when reward_cordinator is missing."""

    # Set reward_cordinator to None
    el_writer.reward_cordinator = None

    with pytest.raises(ValueError, match="RewardsCoordinator contract not provided"):
        el_writer.set_claimer_for(claimer, wait_for_receipt=True)


def test_set_claimer_for_tx_opts_failure(claimer, el_writer, mock_tx_mgr):
    """Simulate a failure when retrieving transaction options."""

    # Modify the mock to raise an error
    mock_tx_mgr.get_no_send_tx_opts.side_effect = Exception(
        "Failed to get transaction options"
    )

    with pytest.raises(
        ValueError,
        match="failed to get no-send tx opts: Failed to get transaction options",
    ):
        el_writer.set_claimer_for(claimer, wait_for_receipt=True)


def test_set_claimer_for_tx_execution_failure(
    claimer, el_writer, mock_reward_coordinator
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_reward_coordinator.functions.setClaimerFor.return_value.build_transaction.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create SetClaimerFor tx: Transaction execution failed",
    ):
        el_writer.set_claimer_for(claimer, wait_for_receipt=True)


def test_set_claimer_for_tx_receipt_failure(claimer, el_writer, mock_tx_mgr):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.set_claimer_for(claimer, wait_for_receipt=True)


import pytest
from web3.exceptions import TransactionNotFound


def test_process_claim_success(
    claim, recipient_address, el_writer, mock_reward_coordinator
):
    """Test process_claim() with valid inputs."""
    try:
        receipt = el_writer.process_claim(
            claim, recipient_address, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_process_claim_missing_reward_coordinator(claim, recipient_address, el_writer):
    """Test ValueError when reward_cordinator is missing."""

    # Set reward_cordinator to None
    el_writer.reward_cordinator = None

    with pytest.raises(ValueError, match="RewardsCoordinator contract not provided"):
        el_writer.process_claim(claim, recipient_address, wait_for_receipt=True)


def test_process_claim_tx_opts_failure(
    claim, recipient_address, el_writer, mock_tx_mgr
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
        el_writer.process_claim(claim, recipient_address, wait_for_receipt=True)


def test_process_claim_tx_execution_failure(
    claim, recipient_address, el_writer, mock_reward_coordinator
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_reward_coordinator.functions.processClaims.return_value.build_transaction.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create ProcessClaim tx: Transaction execution failed",
    ):
        el_writer.process_claim(claim, recipient_address, wait_for_receipt=True)


def test_process_claim_tx_receipt_failure(
    claim, recipient_address, el_writer, mock_tx_mgr
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.process_claim(claim, recipient_address, wait_for_receipt=True)


import pytest
from web3.exceptions import TransactionNotFound


def test_set_operator_avs_split_success(
    operator, avs, split, el_writer, mock_reward_coordinator, mock_eth_http_client
):
    """Test set_operator_avs_split() with valid inputs."""
    try:
        receipt = el_writer.set_operator_avs_split(
            operator, avs, split, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_set_operator_avs_split_missing_reward_coordinator(
    operator, avs, split, el_writer
):
    """Test ValueError when reward_cordinator is missing."""

    # Set reward_cordinator to None
    el_writer.reward_cordinator = None

    with pytest.raises(ValueError, match="RewardsCoordinator contract not provided"):
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


def test_set_operator_avs_split_tx_opts_failure(
    operator, avs, split, el_writer, mock_tx_mgr
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
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


def test_set_operator_avs_split_tx_execution_failure(
    operator, avs, split, el_writer, mock_reward_coordinator
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_reward_coordinator.functions.setOperatorAVSSplit.return_value.build_transaction.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create SetOperatorAVSSplit tx: Transaction execution failed",
    ):
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


def test_set_operator_avs_split_tx_signing_failure(
    operator, avs, split, el_writer, mock_eth_http_client
):
    """Simulate a failure in signing the transaction."""

    # Modify the mock to raise an error
    mock_eth_http_client.eth.account.sign_transaction.side_effect = Exception(
        "Failed to sign transaction"
    )

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to sign transaction"
    ):
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


def test_set_operator_avs_split_tx_sending_failure(
    operator, avs, split, el_writer, mock_eth_http_client
):
    """Simulate a failure in sending transaction."""

    # Modify the mock to raise an error
    mock_eth_http_client.eth.send_raw_transaction.side_effect = Exception(
        "Failed to send raw transaction"
    )

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send raw transaction"
    ):
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


def test_set_operator_avs_split_tx_receipt_failure(
    operator, avs, split, el_writer, mock_eth_http_client
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_eth_http_client.eth.wait_for_transaction_receipt.side_effect = Exception(
        "Failed to get transaction receipt"
    )

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to get transaction receipt"
    ):
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


import pytest
from web3.exceptions import TransactionNotFound


def test_set_operator_avs_split_success(
    operator, avs, split, el_writer, mock_reward_coordinator, mock_eth_http_client
):
    """Test set_operator_avs_split() with valid inputs."""
    try:
        receipt = el_writer.set_operator_avs_split(
            operator, avs, split, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_set_operator_avs_split_missing_reward_coordinator(
    operator, avs, split, el_writer
):
    """Test ValueError when reward_cordinator is missing."""

    # Set reward_cordinator to None
    el_writer.reward_cordinator = None

    with pytest.raises(ValueError, match="RewardsCoordinator contract not provided"):
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


def test_set_operator_avs_split_tx_opts_failure(
    operator, avs, split, el_writer, mock_tx_mgr
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
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


def test_set_operator_avs_split_tx_execution_failure(
    operator, avs, split, el_writer, mock_reward_coordinator
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_reward_coordinator.functions.setOperatorAVSSplit.return_value.build_transaction.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create SetOperatorAVSSplit tx: Transaction execution failed",
    ):
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


def test_set_operator_avs_split_tx_signing_failure(
    operator, avs, split, el_writer, mock_eth_http_client
):
    """Simulate a failure in signing the transaction."""

    # Modify the mock to raise an error
    mock_eth_http_client.eth.account.sign_transaction.side_effect = Exception(
        "Failed to sign transaction"
    )

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to sign transaction"
    ):
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


def test_set_operator_avs_split_tx_sending_failure(
    operator, avs, split, el_writer, mock_eth_http_client
):
    """Simulate a failure in sending transaction."""

    # Modify the mock to raise an error
    mock_eth_http_client.eth.send_raw_transaction.side_effect = Exception(
        "Failed to send raw transaction"
    )

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send raw transaction"
    ):
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


def test_set_operator_avs_split_tx_receipt_failure(
    operator, avs, split, el_writer, mock_eth_http_client
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_eth_http_client.eth.wait_for_transaction_receipt.side_effect = Exception(
        "Failed to get transaction receipt"
    )

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to get transaction receipt"
    ):
        el_writer.set_operator_avs_split(operator, avs, split, wait_for_receipt=True)


import pytest
from web3.exceptions import TransactionNotFound


def test_set_operator_pi_split_success(
    operator, split, el_writer, mock_reward_coordinator
):
    """Test set_operator_pi_split() with valid inputs."""
    try:
        receipt = el_writer.set_operator_pi_split(
            operator, split, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_set_operator_pi_split_missing_reward_coordinator(operator, split, el_writer):
    """Test ValueError when reward_cordinator is missing."""

    # Set reward_cordinator to None
    el_writer.reward_cordinator = None

    with pytest.raises(ValueError, match="RewardsCoordinator contract not provided"):
        el_writer.set_operator_pi_split(operator, split, wait_for_receipt=True)


def test_set_operator_pi_split_tx_opts_failure(operator, split, el_writer, mock_tx_mgr):
    """Simulate a failure when retrieving transaction options."""

    # Modify the mock to raise an error
    mock_tx_mgr.get_no_send_tx_opts.side_effect = Exception(
        "Failed to get transaction options"
    )

    with pytest.raises(
        ValueError,
        match="failed to get no send tx opts: Failed to get transaction options",
    ):
        el_writer.set_operator_pi_split(operator, split, wait_for_receipt=True)


def test_set_operator_pi_split_tx_execution_failure(
    operator, split, el_writer, mock_reward_coordinator
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_reward_coordinator.functions.setOperatorPISplit.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create SetOperatorPISplit tx: Transaction execution failed",
    ):
        el_writer.set_operator_pi_split(operator, split, wait_for_receipt=True)


def test_set_operator_pi_split_tx_receipt_failure(
    operator, split, el_writer, mock_tx_mgr
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.set_operator_pi_split(operator, split, wait_for_receipt=True)


import pytest
from web3.exceptions import TransactionNotFound


def test_set_operator_set_split_success(
    operator, operator_set, split, el_writer, mock_reward_coordinator
):
    """Test set_operator_set_split() with valid inputs."""
    try:
        receipt = el_writer.set_operator_set_split(
            operator, operator_set, split, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_set_operator_set_split_missing_reward_coordinator(
    operator, operator_set, split, el_writer
):
    """Test ValueError when reward_cordinator is missing."""

    # Set reward_cordinator to None
    el_writer.reward_cordinator = None

    with pytest.raises(ValueError, match="RewardsCoordinator contract not provided"):
        el_writer.set_operator_set_split(
            operator, operator_set, split, wait_for_receipt=True
        )


def test_set_operator_set_split_tx_opts_failure(
    operator, operator_set, split, el_writer, mock_tx_mgr
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
        el_writer.set_operator_set_split(
            operator, operator_set, split, wait_for_receipt=True
        )


def test_set_operator_set_split_tx_execution_failure(
    operator, operator_set, split, el_writer, mock_reward_coordinator
):
    """Simulate a failure when executing the transaction."""

    # Modify the mock to raise an error
    mock_reward_coordinator.functions.setOperatorSetSplit.return_value.transact.side_effect = Exception(
        "Transaction execution failed"
    )

    with pytest.raises(
        ValueError,
        match="failed to create SetOperatorSetSplit tx: Transaction execution failed",
    ):
        el_writer.set_operator_set_split(
            operator, operator_set, split, wait_for_receipt=True
        )


def test_set_operator_set_split_tx_receipt_failure(
    operator, operator_set, split, el_writer, mock_tx_mgr
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send transaction")

    with pytest.raises(
        ValueError, match="failed to send tx: Failed to send transaction"
    ):
        el_writer.set_operator_set_split(
            operator, operator_set, split, wait_for_receipt=True
        )


import pytest
from web3.exceptions import TransactionNotFound


def test_deposit_erc20_into_strategy_success(
    strategy_addr,
    amount,
    el_writer,
    mock_strategy_manager,
    mock_el_chain_reader,
    mock_underlying_token_contract,
):
    """Test deposit_erc20_into_strategy() with valid inputs."""
    try:
        receipt = el_writer.deposit_erc20_into_strategy(
            strategy_addr, amount, wait_for_receipt=True
        )

        # Assertions
        assert receipt is not None, "Expected a valid transaction receipt, got None"
        assert isinstance(receipt, dict), "Expected receipt to be a dictionary"
        assert "transactionHash" in receipt, "Expected 'transactionHash' in receipt"

    except Exception as e:
        pytest.fail(f"❌ Unexpected Error: {e}")


def test_deposit_erc20_into_strategy_missing_strategy_manager(
    strategy_addr, amount, el_writer
):
    """Test ValueError when strategy_manager is missing."""

    # Set strategy_manager to None
    el_writer.strategy_manager = None

    with pytest.raises(ValueError, match="StrategyManager contract not provided"):
        el_writer.deposit_erc20_into_strategy(
            strategy_addr, amount, wait_for_receipt=True
        )


def test_deposit_erc20_into_strategy_tx_opts_failure(
    strategy_addr, amount, el_writer, mock_tx_mgr
):
    """Simulate a failure when retrieving transaction options."""

    # Modify the mock to raise an error
    mock_tx_mgr.get_no_send_tx_opts.side_effect = Exception(
        "Failed to get transaction options"
    )

    with pytest.raises(
        ValueError,
        match="failed to get no-send tx opts: Failed to get transaction options",
    ):
        el_writer.deposit_erc20_into_strategy(
            strategy_addr, amount, wait_for_receipt=True
        )


def test_deposit_erc20_into_strategy_get_strategy_failure(
    strategy_addr, amount, el_writer, mock_el_chain_reader
):
    """Simulate a failure when fetching strategy and underlying ERC20 token."""

    # Modify the mock to raise an error
    mock_el_chain_reader.GetStrategyAndUnderlyingERC20Token.side_effect = Exception(
        "Failed to fetch strategy data"
    )

    with pytest.raises(
        ValueError,
        match="failed to get strategy and underlying ERC20 token: Failed to fetch strategy data",
    ):
        el_writer.deposit_erc20_into_strategy(
            strategy_addr, amount, wait_for_receipt=True
        )


def test_deposit_erc20_into_strategy_approve_failure(
    strategy_addr, amount, el_writer, mock_underlying_token_contract
):
    """Simulate a failure when approving token transfer."""

    # Modify the mock to raise an error
    mock_underlying_token_contract.functions.Approve.return_value.transact.side_effect = Exception(
        "Approval failed"
    )

    with pytest.raises(
        ValueError, match="failed to create approve token transfer tx: Approval failed"
    ):
        el_writer.deposit_erc20_into_strategy(
            strategy_addr, amount, wait_for_receipt=True
        )


def test_deposit_erc20_into_strategy_approve_tx_failure(
    strategy_addr, amount, el_writer, mock_tx_mgr
):
    """Simulate a failure in sending the approval transaction."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send approval transaction")

    with pytest.raises(
        ValueError,
        match="failed to send approval tx: Failed to send approval transaction",
    ):
        el_writer.deposit_erc20_into_strategy(
            strategy_addr, amount, wait_for_receipt=True
        )


def test_deposit_erc20_into_strategy_deposit_failure(
    strategy_addr, amount, el_writer, mock_strategy_manager
):
    """Simulate a failure when executing the deposit transaction."""

    # Modify the mock to raise an error
    mock_strategy_manager.functions.depositIntoStrategyWithSignature.return_value.transact.side_effect = Exception(
        "Deposit failed"
    )

    with pytest.raises(
        ValueError, match="failed to create DepositIntoStrategy tx: Deposit failed"
    ):
        el_writer.deposit_erc20_into_strategy(
            strategy_addr, amount, wait_for_receipt=True
        )


def test_deposit_erc20_into_strategy_tx_receipt_failure(
    strategy_addr, amount, el_writer, mock_tx_mgr
):
    """Simulate a failure in getting transaction receipt."""

    # Modify the mock to raise an error
    mock_tx_mgr.send.side_effect = Exception("Failed to send deposit transaction")

    with pytest.raises(
        ValueError,
        match="failed to send deposit tx: Failed to send deposit transaction",
    ):
        el_writer.deposit_erc20_into_strategy(
            strategy_addr, amount, wait_for_receipt=True
        )
