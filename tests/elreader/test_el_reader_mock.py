# from unittest.mock import MagicMock
# import pytest
# from base import *
# from web3 import Web3
# from conftestreader import *

# def test_get_allocatable_magnitude_valid(mocker, operator_address, strategy_address):
#     """Test get_allocatable_magnitude() returns the correct magnitude."""

#     # Mock the function response
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getAllocatableMagnitude.return_value.call.return_value = 1000000000000000000

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_allocatable_magnitude(operator_address, strategy_address)

#     # Assertions
#     assert result == 1000000000000000000, f"Expected 1000000000000000000, but got {result}"


# def test_get_allocatable_magnitude_zero(mocker, operator_address, strategy_address):
#     """Test get_allocatable_magnitude() returns zero when no magnitude is available."""

#     # Mock the function response to return 0
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getAllocatableMagnitude.return_value.call.return_value = 0

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_allocatable_magnitude(operator_address, strategy_address)

#     # Assertions
#     assert result == 0, f"Expected 0, but got {result}"


# def test_get_allocatable_magnitude_exception(mocker, operator_address, strategy_address):
#     """Test get_allocatable_magnitude() handles contract call failure."""

#     # Mock the function to raise an exception
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getAllocatableMagnitude.return_value.call.side_effect = Exception("Contract call failed")

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_allocatable_magnitude(operator_address, strategy_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# from unittest.mock import MagicMock

# def test_get_encumbered_magnitude_valid(mocker, encumbered_operator_address, encumbered_strategy_address):
#     """Test get_encumbered_magnitude() returns the expected encumbered magnitude."""

#     # Mock the function response
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getEncumberedMagnitude.return_value.call.return_value = 500000000000000000

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_encumbered_magnitude(encumbered_operator_address, encumbered_strategy_address)

#     # Assertions
#     assert result == 500000000000000000, f"Expected 500000000000000000, but got {result}"


# def test_get_encumbered_magnitude_zero(mocker, encumbered_operator_address, encumbered_strategy_address):
#     """Test get_encumbered_magnitude() returns zero when no encumbered magnitude exists."""

#     # Mock the function response to return 0
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getEncumberedMagnitude.return_value.call.return_value = 0

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_encumbered_magnitude(encumbered_operator_address, encumbered_strategy_address)

#     # Assertions
#     assert result == 0, f"Expected 0, but got {result}"


# def test_get_encumbered_magnitude_exception(mocker, encumbered_operator_address, encumbered_strategy_address):
#     """Test get_encumbered_magnitude() handles contract call failure properly."""

#     # Mock the function to raise an exception
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getEncumberedMagnitude.return_value.call.side_effect = Exception("Contract call failed")

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_encumbered_magnitude(encumbered_operator_address, encumbered_strategy_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# from unittest.mock import MagicMock

# def test_get_max_magnitudes_valid(mocker, max_magnitudes_operator_address, max_magnitudes_strategy_addresses):
#     """Test get_max_magnitudes() returns the expected magnitudes."""

#     # Mock the function response
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getMaxMagnitudes.return_value.call.return_value = [
#         1000000000000000000, 2000000000000000000
#     ]

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_max_magnitudes(max_magnitudes_operator_address, max_magnitudes_strategy_addresses)

#     # Assertions
#     assert result == [1000000000000000000, 2000000000000000000], f"Expected [1000000000000000000, 2000000000000000000], but got {result}"


# def test_get_max_magnitudes_zero(mocker, max_magnitudes_operator_address, max_magnitudes_strategy_addresses):
#     """Test get_max_magnitudes() returns zero values when max magnitudes are not set."""

#     # Mock the function response to return 0 values
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getMaxMagnitudes.return_value.call.return_value = [0, 0]

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_max_magnitudes(max_magnitudes_operator_address, max_magnitudes_strategy_addresses)

#     # Assertions
#     assert result == [0, 0], f"Expected [0, 0], but got {result}"


# def test_get_max_magnitudes_exception(mocker, max_magnitudes_operator_address, max_magnitudes_strategy_addresses):
#     """Test get_max_magnitudes() handles contract call failure properly."""

#     # Mock the function to raise an exception
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getMaxMagnitudes.return_value.call.side_effect = Exception("Contract call failed")

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_max_magnitudes(max_magnitudes_operator_address, max_magnitudes_strategy_addresses)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# from unittest.mock import MagicMock

# def test_get_allocation_info_valid(mocker, allocation_operator_address, allocation_strategy_address):
#     """Test get_allocation_info() returns allocation data correctly."""

#     # Mock contract response
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getAllocationInfo.return_value.call.return_value = [
#         {"amount": 500, "timestamp": 1700000000}
#     ]

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_allocation_info(allocation_operator_address, allocation_strategy_address)

#     # Assertions
#     assert isinstance(result, list), f"Expected list, but got {type(result)}"
#     assert len(result) == 1, f"Expected 1 allocation entry, but got {len(result)}"
#     assert result[0]["amount"] == 500, f"Expected amount 500, but got {result[0]['amount']}"
#     assert result[0]["timestamp"] == 1700000000, f"Expected timestamp 1700000000, but got {result[0]['timestamp']}"


# def test_get_allocation_info_empty(mocker, allocation_operator_address, allocation_strategy_address):
#     """Test get_allocation_info() returns an empty list when no allocations exist."""

#     # Mock contract response to return an empty list
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getAllocationInfo.return_value.call.return_value = []

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_allocation_info(allocation_operator_address, allocation_strategy_address)

#     # Assertions
#     assert result == [], f"Expected an empty list, but got {result}"


# def test_get_allocation_info_exception(mocker, allocation_operator_address, allocation_strategy_address):
#     """Test get_allocation_info() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getAllocationInfo.return_value.call.side_effect = Exception("Contract call failed")

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_allocation_info(allocation_operator_address, allocation_strategy_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# from unittest.mock import MagicMock

# def test_get_operator_shares_valid(mocker, operator_shares_operator_address, operator_shares_strategy_addresses):
#     """Test get_operator_shares() returns valid operator shares."""

#     # Mock contract response
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getOperatorShares.return_value.call.return_value = [1000, 2000]

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_operator_shares(operator_shares_operator_address, operator_shares_strategy_addresses)

#     # Assertions
#     assert isinstance(result, list), f"Expected list, but got {type(result)}"
#     assert len(result) == 2, f"Expected 2 shares, but got {len(result)}"
#     assert result[0] == 1000, f"Expected 1000 shares, but got {result[0]}"
#     assert result[1] == 2000, f"Expected 2000 shares, but got {result[1]}"


# def test_get_operator_shares_zero(mocker, operator_shares_operator_address, operator_shares_strategy_addresses):
#     """Test get_operator_shares() returns zero when operator has no shares."""

#     # Mock contract response to return zero shares
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getOperatorShares.return_value.call.return_value = [0, 0]

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_operator_shares(operator_shares_operator_address, operator_shares_strategy_addresses)

#     # Assertions
#     assert result == [0, 0], f"Expected [0, 0] but got {result}"


# def test_get_operator_shares_exception(mocker, operator_shares_operator_address, operator_shares_strategy_addresses):
#     """Test get_operator_shares() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getOperatorShares.return_value.call.side_effect = Exception("Contract call failed")

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_operator_shares(operator_shares_operator_address, operator_shares_strategy_addresses)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# from unittest.mock import MagicMock

# def test_get_operator_sets_for_operator_valid(mocker, operator_sets_operator_address):
#     """Test get_operator_sets_for_operator() returns valid operator sets."""

#     # Mock contract response
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getOperatorSetsForOperator.return_value.call.return_value = [
#         {"Id": 1, "Avs": "0x2222222222222222222222222222222222222222"},
#         {"Id": 2, "Avs": "0x3333333333333333333333333333333333333333"},
#     ]

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_operator_sets_for_operator(operator_sets_operator_address)

#     # Assertions
#     assert isinstance(result, list), f"Expected list, but got {type(result)}"
#     assert len(result) == 2, f"Expected 2 operator sets, but got {len(result)}"
#     assert result[0]["Id"] == 1, f"Expected first operator set ID 1, but got {result[0]['Id']}"
#     assert result[1]["Id"] == 2, f"Expected second operator set ID 2, but got {result[1]['Id']}"
#     assert result[0]["Avs"] == "0x2222222222222222222222222222222222222222", "Incorrect Avs for first operator set"
#     assert result[1]["Avs"] == "0x3333333333333333333333333333333333333333", "Incorrect Avs for second operator set"


# def test_get_operator_sets_for_operator_empty(mocker, operator_sets_operator_address):
#     """Test get_operator_sets_for_operator() returns an empty list when no operator sets exist."""

#     # Mock contract response to return an empty list
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getOperatorSetsForOperator.return_value.call.return_value = []

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function
#     result = el_reader.get_operator_sets_for_operator(operator_sets_operator_address)

#     # Assertions
#     assert result == [], f"Expected an empty list but got {result}"


# def test_get_operator_sets_for_operator_exception(mocker, operator_sets_operator_address):
#     """Test get_operator_sets_for_operator() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getOperatorSetsForOperator.return_value.call.side_effect = Exception("Contract call failed")

#     # Inject the mock into the ELReader instance
#     el_reader.allocation_manager = mock_allocation_manager

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_operator_sets_for_operator(operator_sets_operator_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_allocation_delay_valid(mocker, allocation_delay_operator_address, mock_allocation_manager):
#     """Test get_allocation_delay() returns a valid allocation delay."""

#     # Mock contract response to return a valid delay
#     mock_allocation_manager.functions.getAllocationDelay.return_value.call.return_value = (True, 10)

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.get_allocation_delay(allocation_delay_operator_address)

#     # Assertions
#     assert isinstance(result, int), f"Expected integer, but got {type(result)}"
#     assert result == 10, f"Expected allocation delay 10, but got {result}"


# def test_get_allocation_delay_zero(mocker, allocation_delay_operator_address, mock_allocation_manager):
#     """Test get_allocation_delay() returns 0 when no delay is set."""

#     # Mock contract response to return zero delay
#     mock_allocation_manager.functions.getAllocationDelay.return_value.call.return_value = (True, 0)

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.get_allocation_delay(allocation_delay_operator_address)

#     # Assertions
#     assert result == 0, f"Expected allocation delay 0, but got {result}"


# def test_get_allocation_delay_exception(mocker, allocation_delay_operator_address, mock_allocation_manager):
#     """Test get_allocation_delay() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager.functions.getAllocationDelay.return_value.call.side_effect = Exception("Contract call failed")

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_allocation_delay(allocation_delay_operator_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_registered_sets_valid(mocker, registered_sets_operator_address, mock_allocation_manager):
#     """Test get_registered_sets() returns a valid list of sets."""

#     # Mock contract response to return some registered sets
#     mock_allocation_manager.functions.getRegisteredSets.return_value.call.return_value = [1, 2, 3]

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.get_registered_sets(registered_sets_operator_address)

#     # Assertions
#     assert isinstance(result, list), f"Expected list, but got {type(result)}"
#     assert result == [1, 2, 3], f"Expected registered sets [1, 2, 3], but got {result}"


# def test_get_registered_sets_empty(mocker, registered_sets_operator_address, mock_allocation_manager):
#     """Test get_registered_sets() returns an empty list when no sets are registered."""

#     # Mock contract response to return an empty list
#     mock_allocation_manager.functions.getRegisteredSets.return_value.call.return_value = []

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.get_registered_sets(registered_sets_operator_address)

#     # Assertions
#     assert result == [], f"Expected empty list, but got {result}"


# def test_get_registered_sets_exception(mocker, registered_sets_operator_address, mock_allocation_manager):
#     """Test get_registered_sets() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager.functions.getRegisteredSets.return_value.call.side_effect = Exception("Contract call failed")

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_registered_sets(registered_sets_operator_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_calculate_operator_avs_registration_digestHash_valid(mocker, operator_address, avs_address, salt, expiry, mock_allocation_manager):
#     """Test calculate_operator_avs_registration_digestHash() returns a valid hash."""

#     # Expected hash result (mocked)
#     expected_hash = b'!K\x9e\xbeT\xd4U\xf7\x80\xed&\x03z\x9ev-6\xbf\xc1\x9d\xa2\x88DiY\xb3Q\x7f\xca\xe3\xb4\x85'

#     # Mock contract response
#     mock_allocation_manager.functions.CalculateOperatorAVSRegistrationDigestHash.return_value.call.return_value = expected_hash

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.calculate_operator_avs_registration_digestHash(operator_address, avs_address, salt, expiry)

#     # Assertions
#     assert isinstance(result, bytes), f"Expected bytes, but got {type(result)}"
#     assert result == expected_hash, f"Expected hash {expected_hash}, but got {result}"


# def test_calculate_operator_avs_registration_digestHash_invalid_input(mocker, operator_address, avs_address, salt, expiry, mock_allocation_manager):
#     """Test calculate_operator_avs_registration_digestHash() with invalid input (None values)."""

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call function with None values
#     try:
#         result = el_reader.calculate_operator_avs_registration_digestHash(None, avs_address, salt, expiry)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert isinstance(e, TypeError), f"Unexpected exception type: {type(e)}"


# def test_calculate_operator_avs_registration_digestHash_exception(mocker, operator_address, avs_address, salt, expiry, mock_allocation_manager):
#     """Test calculate_operator_avs_registration_digestHash() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager.functions.CalculateOperatorAVSRegistrationDigestHash.return_value.call.side_effect = Exception("Contract call failed")

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function and handle exception
#     try:
#         result = el_reader.calculate_operator_avs_registration_digestHash(operator_address, avs_address, salt, expiry)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_get_operators_for_operator_set_valid(mocker, operator_set, mock_allocation_manager):
#     """Test get_operators_for_operator_set() with a valid operator set."""

#     # Mock contract response with example operator addresses
#     expected_operators = [
#         "0x1234567890abcdef1234567890abcdef12345678",
#         "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd"
#     ]
#     mock_allocation_manager.functions.getMembers.return_value.call.return_value = expected_operators

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.get_operators_for_operator_set(operator_set)

#     # Assertions
#     assert isinstance(result, list), f"Expected list, but got {type(result)}"
#     assert result == expected_operators, f"Expected operators {expected_operators}, but got {result}"


# def test_get_operators_for_operator_set_invalid_input(mocker, mock_allocation_manager):
#     """Test get_operators_for_operator_set() with invalid input (missing fields)."""

#     invalid_operator_set = {"Id": None}  # Missing "Avs" key

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call function with invalid input and check for ValueError
#     try:
#         result = el_reader.get_operators_for_operator_set(invalid_operator_set)
#         assert False, f"Expected an exception but got result: {result}"
#     except ValueError as e:
#         assert "operator_set must contain 'Id' and 'Avs' keys." in str(e), f"Unexpected error message: {e}"


# def test_get_operators_for_operator_set_exception(mocker, operator_set, mock_allocation_manager):
#     """Test get_operators_for_operator_set() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager.functions.getMembers.return_value.call.side_effect = Exception("Contract call failed")

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_operators_for_operator_set(operator_set)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_num_operators_for_operator_set_valid(mocker, operator_set, mock_allocation_manager):
#     """Test get_num_operators_for_operator_set() with a valid operator set."""

#     # Mock contract response with a list of operator addresses
#     expected_operators = [
#         "0x1234567890abcdef1234567890abcdef12345678",
#         "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd"
#     ]
#     mock_allocation_manager.functions.getMembers.return_value.call.return_value = expected_operators

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.get_num_operators_for_operator_set(operator_set)

#     # Assertions
#     assert isinstance(result, int), f"Expected int, but got {type(result)}"
#     assert result == len(expected_operators), f"Expected {len(expected_operators)} operators, but got {result}"


# def test_get_num_operators_for_operator_set_invalid_input(mocker, mock_allocation_manager):
#     """Test get_num_operators_for_operator_set() with invalid input (missing fields)."""

#     invalid_operator_set = {"Id": None}  # Missing "Avs" key

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call function with invalid input and check for ValueError
#     try:
#         result = el_reader.get_num_operators_for_operator_set(invalid_operator_set)
#         assert False, f"Expected an exception but got result: {result}"
#     except ValueError as e:
#         assert "operator_set must contain 'Id' and 'Avs' keys." in str(e), f"Unexpected error message: {e}"


# def test_get_num_operators_for_operator_set_exception(mocker, operator_set, mock_allocation_manager):
#     """Test get_num_operators_for_operator_set() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager.functions.getMembers.return_value.call.side_effect = Exception("Contract call failed")

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_num_operators_for_operator_set(operator_set)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_get_strategies_for_operator_set_valid(mocker, operator_set, mock_allocation_manager):
#     """Test get_strategies_for_operator_set() with a valid operator set."""

#     # Mock contract response with a list of strategies
#     expected_strategies = [
#         "0x4444444444444444444444444444444444444444",
#         "0x5555555555555555555555555555555555555555"
#     ]
#     mock_allocation_manager.functions.getStrategiesInOperatorSet.return_value.call.return_value = expected_strategies

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.get_strategies_for_operator_set(operator_set)

#     # Assertions
#     assert isinstance(result, list), f"Expected list, but got {type(result)}"
#     assert result == expected_strategies, f"Expected {expected_strategies}, but got {result}"


# def test_get_strategies_for_operator_set_invalid_input(mocker, mock_allocation_manager):
#     """Test get_strategies_for_operator_set() with invalid input (missing fields)."""

#     invalid_operator_set = {"Id": None}  # Missing "Avs" key

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call function with invalid input and check for ValueError
#     try:
#         result = el_reader.get_strategies_for_operator_set(invalid_operator_set)
#         assert False, f"Expected an exception but got result: {result}"
#     except ValueError as e:
#         assert "operator_set must contain 'Id' and 'Avs' keys." in str(e), f"Unexpected error message: {e}"


# def test_get_strategies_for_operator_set_exception(mocker, operator_set, mock_allocation_manager):
#     """Test get_strategies_for_operator_set() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager.functions.getStrategiesInOperatorSet.return_value.call.side_effect = Exception("Contract call failed")

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_strategies_for_operator_set(operator_set)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_is_operator_registered_valid(mocker, operator_address, mock_allocation_manager):
#     """Test is_operator_registered() with a registered operator."""

#     # Mock contract response to return True
#     mock_allocation_manager.functions.isOperatorRegistered.return_value.call.return_value = True

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.is_operator_registered(operator_address)

#     # Assertions
#     assert isinstance(result, bool), f"Expected bool, but got {type(result)}"
#     assert result is True, f"Expected True, but got {result}"


# def test_is_operator_registered_unregistered(mocker, operator_address, mock_allocation_manager):
#     """Test is_operator_registered() with an unregistered operator."""

#     # Mock contract response to return False
#     mock_allocation_manager.functions.isOperatorRegistered.return_value.call.return_value = False

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.is_operator_registered(operator_address)

#     # Assertions
#     assert isinstance(result, bool), f"Expected bool, but got {type(result)}"
#     assert result is False, f"Expected False, but got {result}"


# def test_is_operator_registered_exception(mocker, operator_address, mock_allocation_manager):
#     """Test is_operator_registered() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager.functions.isOperatorRegistered.return_value.call.side_effect = Exception("Contract call failed")

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function and handle exception
#     try:
#         result = el_reader.is_operator_registered(operator_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_staker_shares_valid(mocker, staker_address, mock_allocation_manager):
#     """Test get_staker_shares() with a staker having shares."""

#     # Mock contract response
#     mock_allocation_manager.functions.getStakerShares.return_value.call.return_value = (
#         ["0xStrategy1", "0xStrategy2"], [1000, 500]
#     )

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     strategies, shares = el_reader.get_staker_shares(staker_address)

#     # Assertions
#     assert isinstance(strategies, list), "Expected strategies to be a list"
#     assert isinstance(shares, list), "Expected shares to be a list"
#     assert strategies == ["0xStrategy1", "0xStrategy2"], f"Unexpected strategies: {strategies}"
#     assert shares == [1000, 500], f"Unexpected shares: {shares}"


# def test_get_staker_shares_empty(mocker, staker_address, mock_allocation_manager):
#     """Test get_staker_shares() with a staker having no shares."""

#     # Mock contract response to return empty lists
#     mock_allocation_manager.functions.getStakerShares.return_value.call.return_value = ([], [])

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     strategies, shares = el_reader.get_staker_shares(staker_address)

#     # Assertions
#     assert strategies == [], "Expected an empty list for strategies"
#     assert shares == [], "Expected an empty list for shares"


# def test_get_staker_shares_exception(mocker, staker_address, mock_allocation_manager):
#     """Test get_staker_shares() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager.functions.getStakerShares.return_value.call.side_effect = Exception("Contract call failed")

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function and handle exception
#     try:
#         strategies, shares = el_reader.get_staker_shares(staker_address)
#         assert False, f"Expected an exception but got result: {strategies}, {shares}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_get_delegated_operator_valid(mocker, staker_address, block_number, mock_allocation_manager):
#     """Test get_delegated_operator() with a staker that has a delegated operator."""

#     # Mock contract response to return a valid operator address
#     mock_allocation_manager.functions.getDelegatedOperator.return_value.call.return_value = "0x1234567890abcdef1234567890abcdef12345678"

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.get_delegated_operator(staker_address, block_number)

#     # Assertions
#     assert isinstance(result, str), "Expected result to be a string"
#     assert result == "0x1234567890abcdef1234567890abcdef12345678", f"Unexpected result: {result}"


# def test_get_delegated_operator_empty(mocker, staker_address, block_number, mock_allocation_manager):
#     """Test get_delegated_operator() with a staker that has no delegated operator."""

#     # Mock contract response to return zero address
#     mock_allocation_manager.functions.getDelegatedOperator.return_value.call.return_value = "0x0000000000000000000000000000000000000000"

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.get_delegated_operator(staker_address, block_number)

#     # Assertions
#     assert result == "0x0000000000000000000000000000000000000000", f"Unexpected result: {result}"


# def test_get_delegated_operator_exception(mocker, staker_address, block_number, mock_allocation_manager):
#     """Test get_delegated_operator() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager.functions.getDelegatedOperator.return_value.call.side_effect = Exception("Contract call failed")

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_delegated_operator(staker_address, block_number)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_operator_details_valid(mocker, mock_allocation_manager):
#     """Test get_operator_details() for a valid operator with expected details."""

#     # Mock contract response to return expected details
#     mock_allocation_manager.functions.getOperatorDetails.return_value.call.return_value = (
#         "0x1111111111111111111111111111111111111111",  # Address
#         "0x2222222222222222222222222222222222222222",  # DelegationApproverAddress
#         100  # AllocationDelay
#     )

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Operator dictionary format
#     operator = {"Address": "0x1111111111111111111111111111111111111111"}

#     # Call the function
#     result = el_reader.get_operator_details(operator)

#     # Assertions
#     assert isinstance(result, dict), "Expected result to be a dictionary"
#     assert result["Address"] == "0x1111111111111111111111111111111111111111"
#     assert result["DelegationApproverAddress"] == "0x2222222222222222222222222222222222222222"
#     assert result["AllocationDelay"] == 100


# def test_get_operator_details_empty(mocker, mock_allocation_manager):
#     """Test get_operator_details() for an operator that does not exist (returns default values)."""

#     # Mock contract response to return empty or default values
#     mock_allocation_manager.functions.getOperatorDetails.return_value.call.return_value = (
#         "0x0000000000000000000000000000000000000000",  # Address
#         False,  # DelegationApproverAddress (not set)
#         0  # AllocationDelay
#     )

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Operator dictionary format
#     operator = {"Address": "0x0000000000000000000000000000000000000000"}

#     # Call the function
#     result = el_reader.get_operator_details(operator)

#     # Assertions
#     assert result["Address"] == "0x0000000000000000000000000000000000000000"
#     assert result["DelegationApproverAddress"] is False  # Expecting False when not set
#     assert result["AllocationDelay"] == 0


# def test_get_operator_details_exception(mocker, mock_allocation_manager):
#     """Test get_operator_details() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager.functions.getOperatorDetails.return_value.call.side_effect = Exception("Contract call failed")

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Operator dictionary format
#     operator = {"Address": "0x1111111111111111111111111111111111111111"}

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_operator_details(operator)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_get_operator_shares_in_strategy_valid(mocker, mock_allocation_manager, operator_address, strategy_address):
#     """Test get_operator_shares_in_strategy() for an operator with shares in a strategy."""

#     # Mock contract response to return a valid share value
#     mock_allocation_manager.functions.getOperatorSharesInStrategy.return_value.call.return_value = 500000000000000000

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.get_operator_shares_in_strategy(operator_address, strategy_address)

#     # Assertions
#     assert isinstance(result, int), "Expected result to be an integer"
#     assert result == 500000000000000000, f"Unexpected share value: {result}"


# def test_get_operator_shares_in_strategy_zero_shares(mocker, mock_allocation_manager, operator_address, strategy_address):
#     """Test get_operator_shares_in_strategy() when the operator has zero shares in the strategy."""

#     # Mock contract response to return zero shares
#     mock_allocation_manager.functions.getOperatorSharesInStrategy.return_value.call.return_value = 0

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function
#     result = el_reader.get_operator_shares_in_strategy(operator_address, strategy_address)

#     # Assertions
#     assert result == 0, f"Expected zero shares but got: {result}"


# def test_get_operator_shares_in_strategy_exception(mocker, mock_allocation_manager, operator_address, strategy_address):
#     """Test get_operator_shares_in_strategy() handles contract call failure properly."""

#     # Mock contract response to raise an exception
#     mock_allocation_manager.functions.getOperatorSharesInStrategy.return_value.call.side_effect = Exception("Contract call failed")

#     # Patch ELReader instance
#     mocker.patch.object(el_reader, 'allocation_manager', mock_allocation_manager)

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_operator_shares_in_strategy(operator_address, strategy_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_calculate_delegation_approval_digest_hash_valid(
#     mocker, staker, operator, delegation_approver, approver_salt, expiry
# ):
#     """Test calculate_delegation_approval_digest_hash() with valid inputs."""

#     expected_hash = b'\x8a\x9ca\x98\xc1G\xea\xef\xe2c:[\x94\xea\x9b\xd5\xbf\x179\x13\xf8C\xd6\xc6Z;\x06\x18\xef\x01\xden'

#     # Mock contract response
#     mock_digest_hash_function = mocker.patch.object(
#         el_reader,
#         "calculate_delegation_approval_digest_hash",
#         return_value=expected_hash
#     )

#     # Call the function
#     result = el_reader.calculate_delegation_approval_digest_hash(
#         staker, operator, delegation_approver, approver_salt, expiry
#     )

#     # Assertions
#     mock_digest_hash_function.assert_called_once_with(staker, operator, delegation_approver, approver_salt, expiry)
#     assert isinstance(result, bytes), "Expected result to be bytes"
#     assert result == expected_hash, f"Unexpected hash value: {result}"


# def test_calculate_delegation_approval_digest_hash_invalid_input(
#     mocker, staker, delegation_approver, approver_salt, expiry
# ):
#     """Test calculate_delegation_approval_digest_hash() with invalid inputs."""

#     invalid_operator = 12345  # Invalid operator type (int instead of address)

#     # Mock function to simulate failure
#     mock_digest_hash_function = mocker.patch.object(
#         el_reader,
#         "calculate_delegation_approval_digest_hash",
#         side_effect=ValueError("Invalid operator address format")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.calculate_delegation_approval_digest_hash(
#             staker, invalid_operator, delegation_approver, approver_salt, expiry
#         )
#         assert False, f"Expected ValueError but got result: {result}"
#     except ValueError as e:
#         assert str(e) == "Invalid operator address format", f"Unexpected error message: {e}"


# def test_calculate_delegation_approval_digest_hash_exception(
#     mocker, staker, operator, delegation_approver, approver_salt, expiry
# ):
#     """Test calculate_delegation_approval_digest_hash() handles contract call failure."""

#     # Mock function to simulate an exception
#     mock_digest_hash_function = mocker.patch.object(
#         el_reader,
#         "calculate_delegation_approval_digest_hash",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.calculate_delegation_approval_digest_hash(
#             staker, operator, delegation_approver, approver_salt, expiry
#         )
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_operator_shares_valid(mocker, operator_address, strategy_addresses):
#     """Test get_operator_shares() with valid inputs."""

#     expected_shares = [0, 0]  # Expected shares for given strategies

#     # Mock contract response
#     mock_shares_function = mocker.patch.object(
#         el_reader,
#         "get_operator_shares",
#         return_value=expected_shares
#     )

#     # Call the function
#     result = el_reader.get_operator_shares(operator_address, strategy_addresses)

#     # Assertions
#     mock_shares_function.assert_called_once_with(operator_address, strategy_addresses)
#     assert isinstance(result, list), "Expected result to be a list"
#     assert all(isinstance(share, int) for share in result), "Expected list items to be integers"
#     assert result == expected_shares, f"Unexpected shares: {result}"


# def test_get_operator_shares_no_strategies(mocker, operator_address):
#     """Test get_operator_shares() with an empty strategy list."""

#     empty_strategies = []  # No strategies provided
#     expected_shares = []  # Should return an empty list

#     # Mock function to return empty list
#     mock_shares_function = mocker.patch.object(
#         el_reader,
#         "get_operator_shares",
#         return_value=expected_shares
#     )

#     # Call the function
#     result = el_reader.get_operator_shares(operator_address, empty_strategies)

#     # Assertions
#     mock_shares_function.assert_called_once_with(operator_address, empty_strategies)
#     assert isinstance(result, list), "Expected result to be a list"
#     assert result == expected_shares, f"Expected empty list, got: {result}"


# def test_get_operator_shares_exception(mocker, operator_address, strategy_addresses):
#     """Test get_operator_shares() when contract call fails."""

#     # Mock function to simulate an exception
#     mock_shares_function = mocker.patch.object(
#         el_reader,
#         "get_operator_shares",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_operator_shares(operator_address, strategy_addresses)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_operators_shares_valid(mocker, operator_addresses, strategy_addresses):
#     """Test get_operators_shares() with valid inputs."""

#     expected_shares = [[0, 0], [0, 0]]  # Expected shares for given operators and strategies

#     # Mock contract response
#     mock_shares_function = mocker.patch.object(
#         el_reader,
#         "get_operators_shares",
#         return_value=expected_shares
#     )

#     # Call the function
#     result = el_reader.get_operators_shares(operator_addresses, strategy_addresses)

#     # Assertions
#     mock_shares_function.assert_called_once_with(operator_addresses, strategy_addresses)
#     assert isinstance(result, list), "Expected result to be a list"
#     assert all(isinstance(item, list) for item in result), "Expected each item in result to be a list"
#     assert all(all(isinstance(share, int) for share in shares) for shares in result), "Expected all shares to be integers"
#     assert result == expected_shares, f"Unexpected shares: {result}"


# def test_get_operators_shares_empty_inputs(mocker):
#     """Test get_operators_shares() with empty operators and strategies lists."""

#     empty_operators = []  # No operators
#     empty_strategies = []  # No strategies
#     expected_shares = []  # Should return an empty list

#     # Mock function to return empty list
#     mock_shares_function = mocker.patch.object(
#         el_reader,
#         "get_operators_shares",
#         return_value=expected_shares
#     )

#     # Call the function
#     result = el_reader.get_operators_shares(empty_operators, empty_strategies)

#     # Assertions
#     mock_shares_function.assert_called_once_with(empty_operators, empty_strategies)
#     assert isinstance(result, list), "Expected result to be a list"
#     assert result == expected_shares, f"Expected empty list, got: {result}"


# def test_get_operators_shares_exception(mocker, operator_addresses, strategy_addresses):
#     """Test get_operators_shares() when contract call fails."""

#     # Mock function to simulate an exception
#     mock_shares_function = mocker.patch.object(
#         el_reader,
#         "get_operators_shares",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_operators_shares(operator_addresses, strategy_addresses)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_delegation_approver_salt_is_spent_valid(mocker, delegation_approver, approver_salt):
#     """Test get_delegation_approver_salt_is_spent() with a valid, unspent salt."""

#     expected_result = False  # Salt is not spent

#     # Mock function response
#     mock_salt_check = mocker.patch.object(
#         el_reader,
#         "get_delegation_approver_salt_is_spent",
#         return_value=expected_result
#     )

#     # Call the function
#     result = el_reader.get_delegation_approver_salt_is_spent(delegation_approver, approver_salt)

#     # Assertions
#     mock_salt_check.assert_called_once_with(delegation_approver, approver_salt)
#     assert isinstance(result, bool), "Expected result to be a boolean"
#     assert result is False, f"Expected False (salt not spent), got: {result}"


# def test_get_delegation_approver_salt_is_spent_spent(mocker, delegation_approver, approver_salt):
#     """Test get_delegation_approver_salt_is_spent() with an already spent salt."""

#     expected_result = True  # Salt is spent

#     # Mock function response
#     mock_salt_check = mocker.patch.object(
#         el_reader,
#         "get_delegation_approver_salt_is_spent",
#         return_value=expected_result
#     )

#     # Call the function
#     result = el_reader.get_delegation_approver_salt_is_spent(delegation_approver, approver_salt)

#     # Assertions
#     mock_salt_check.assert_called_once_with(delegation_approver, approver_salt)
#     assert isinstance(result, bool), "Expected result to be a boolean"
#     assert result is True, f"Expected True (salt spent), got: {result}"


# def test_get_delegation_approver_salt_is_spent_exception(mocker, delegation_approver, approver_salt):
#     """Test get_delegation_approver_salt_is_spent() when contract call fails."""

#     # Mock function to simulate an exception
#     mock_salt_check = mocker.patch.object(
#         el_reader,
#         "get_delegation_approver_salt_is_spent",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_delegation_approver_salt_is_spent(delegation_approver, approver_salt)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_pending_withdrawal_status_not_pending(mocker, withdrawal_root):
#     """Test get_pending_withdrawal_status() when the withdrawal is not pending."""

#     expected_result = False  # Withdrawal is not pending

#     # Mock function response
#     mock_withdrawal_status = mocker.patch.object(
#         el_reader,
#         "get_pending_withdrawal_status",
#         return_value=expected_result
#     )

#     # Call the function
#     result = el_reader.get_pending_withdrawal_status(withdrawal_root)

#     # Assertions
#     mock_withdrawal_status.assert_called_once_with(withdrawal_root)
#     assert isinstance(result, bool), "Expected result to be a boolean"
#     assert result is False, f"Expected False (withdrawal not pending), got: {result}"


# def test_get_pending_withdrawal_status_pending(mocker, withdrawal_root):
#     """Test get_pending_withdrawal_status() when the withdrawal is pending."""

#     expected_result = True  # Withdrawal is pending

#     # Mock function response
#     mock_withdrawal_status = mocker.patch.object(
#         el_reader,
#         "get_pending_withdrawal_status",
#         return_value=expected_result
#     )

#     # Call the function
#     result = el_reader.get_pending_withdrawal_status(withdrawal_root)

#     # Assertions
#     mock_withdrawal_status.assert_called_once_with(withdrawal_root)
#     assert isinstance(result, bool), "Expected result to be a boolean"
#     assert result is True, f"Expected True (withdrawal pending), got: {result}"


# def test_get_pending_withdrawal_status_exception(mocker, withdrawal_root):
#     """Test get_pending_withdrawal_status() when contract call fails."""

#     # Mock function to simulate an exception
#     mock_withdrawal_status = mocker.patch.object(
#         el_reader,
#         "get_pending_withdrawal_status",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_pending_withdrawal_status(withdrawal_root)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_cumulative_withdrawals_queued_no_withdrawals(mocker, staker):
#     """Test get_cumulative_withdrawals_queued() when no withdrawals are queued."""

#     expected_result = 0  # No withdrawals queued

#     # Mock function response
#     mock_withdrawals_queued = mocker.patch.object(
#         el_reader,
#         "get_cumulative_withdrawals_queued",
#         return_value=expected_result
#     )

#     # Call the function
#     result = el_reader.get_cumulative_withdrawals_queued(staker)

#     # Assertions
#     mock_withdrawals_queued.assert_called_once_with(staker)
#     assert isinstance(result, int), "Expected result to be an integer"
#     assert result == 0, f"Expected 0 (no withdrawals queued), got: {result}"


# def test_get_cumulative_withdrawals_queued_withdrawals(mocker, staker):
#     """Test get_cumulative_withdrawals_queued() when withdrawals are queued."""

#     expected_result = 500000000000000000  # Example queued amount

#     # Mock function response
#     mock_withdrawals_queued = mocker.patch.object(
#         el_reader,
#         "get_cumulative_withdrawals_queued",
#         return_value=expected_result
#     )

#     # Call the function
#     result = el_reader.get_cumulative_withdrawals_queued(staker)

#     # Assertions
#     mock_withdrawals_queued.assert_called_once_with(staker)
#     assert isinstance(result, int), "Expected result to be an integer"
#     assert result == expected_result, f"Expected {expected_result}, got: {result}"


# def test_get_cumulative_withdrawals_queued_exception(mocker, staker):
#     """Test get_cumulative_withdrawals_queued() when contract call fails."""

#     # Mock function to simulate an exception
#     mock_withdrawals_queued = mocker.patch.object(
#         el_reader,
#         "get_cumulative_withdrawals_queued",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_cumulative_withdrawals_queued(staker)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_can_call_not_allowed(mocker, account_address, appointee_address, target, selector):
#     """Test can_call() when the call is NOT allowed."""

#     expected_result = False  # Call is not allowed

#     # Mock function response
#     mock_can_call = mocker.patch.object(
#         el_reader,
#         "can_call",
#         return_value=expected_result
#     )

#     # Call the function
#     result = el_reader.can_call(account_address, appointee_address, target, selector)

#     # Assertions
#     mock_can_call.assert_called_once_with(account_address, appointee_address, target, selector)
#     assert isinstance(result, bool), "Expected result to be a boolean"
#     assert not result, f"Expected False (call not allowed), got: {result}"


# def test_can_call_allowed(mocker, account_address, appointee_address, target, selector):
#     """Test can_call() when the call is allowed."""

#     expected_result = True  # Call is allowed

#     # Mock function response
#     mock_can_call = mocker.patch.object(
#         el_reader,
#         "can_call",
#         return_value=expected_result
#     )

#     # Call the function
#     result = el_reader.can_call(account_address, appointee_address, target, selector)

#     # Assertions
#     mock_can_call.assert_called_once_with(account_address, appointee_address, target, selector)
#     assert isinstance(result, bool), "Expected result to be a boolean"
#     assert result, f"Expected True (call allowed), got: {result}"


# def test_can_call_exception(mocker, account_address, appointee_address, target, selector):
#     """Test can_call() when contract call fails."""

#     # Mock function to simulate an exception
#     mock_can_call = mocker.patch.object(
#         el_reader,
#         "can_call",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.can_call(account_address, appointee_address, target, selector)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_list_appointees_with_results(mocker, account_address, target, selector):
#     """Test list_appointees() when appointees exist."""

#     expected_result = [
#         "0x1111111111111111111111111111111111111111",
#         "0x2222222222222222222222222222222222222222"
#     ]  # Sample appointees list

#     # Mock function response
#     mock_list_appointees = mocker.patch.object(
#         el_reader,
#         "list_appointees",
#         return_value=expected_result
#     )

#     # Call the function
#     result = el_reader.list_appointees(account_address, target, selector)

#     # Assertions
#     mock_list_appointees.assert_called_once_with(account_address, target, selector)
#     assert isinstance(result, list), "Expected result to be a list"
#     assert result == expected_result, f"Expected {expected_result}, got {result}"


# def test_list_appointees_empty(mocker, account_address, target, selector):
#     """Test list_appointees() when no appointees exist."""

#     expected_result = []  # No appointees

#     # Mock function response
#     mock_list_appointees = mocker.patch.object(
#         el_reader,
#         "list_appointees",
#         return_value=expected_result
#     )

#     # Call the function
#     result = el_reader.list_appointees(account_address, target, selector)

#     # Assertions
#     mock_list_appointees.assert_called_once_with(account_address, target, selector)
#     assert isinstance(result, list), "Expected result to be a list"
#     assert result == [], f"Expected empty list, got: {result}"


# def test_list_appointees_exception(mocker, account_address, target, selector):
#     """Test list_appointees() when contract call fails."""

#     # Mock function to simulate an exception
#     mock_list_appointees = mocker.patch.object(
#         el_reader,
#         "list_appointees",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.list_appointees(account_address, target, selector)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_list_appointee_permissions_with_results(mocker, account_address, appointee_address):
#     """Test list_appointee_permissions() when permissions exist."""

#     expected_targets = [
#         "0x1111111111111111111111111111111111111111",
#         "0x2222222222222222222222222222222222222222"
#     ]
#     expected_selectors = [
#         bytes.fromhex("a3d1e5f4"),  # Example function selectors
#         bytes.fromhex("b4c2d3e6")
#     ]

#     # Mock function response
#     mock_list_permissions = mocker.patch.object(
#         el_reader,
#         "list_appointee_permissions",
#         return_value=(expected_targets, expected_selectors)
#     )

#     # Call the function
#     targets, selectors = el_reader.list_appointee_permissions(account_address, appointee_address)

#     # Assertions
#     mock_list_permissions.assert_called_once_with(account_address, appointee_address)
#     assert isinstance(targets, list), "Expected targets to be a list"
#     assert isinstance(selectors, list), "Expected selectors to be a list"
#     assert targets == expected_targets, f"Expected {expected_targets}, got {targets}"
#     assert selectors == expected_selectors, f"Expected {expected_selectors}, got {selectors}"


# def test_list_appointee_permissions_empty(mocker, account_address, appointee_address):
#     """Test list_appointee_permissions() when no permissions exist."""

#     expected_targets = []  # No targets
#     expected_selectors = []  # No selectors

#     # Mock function response
#     mock_list_permissions = mocker.patch.object(
#         el_reader,
#         "list_appointee_permissions",
#         return_value=(expected_targets, expected_selectors)
#     )

#     # Call the function
#     targets, selectors = el_reader.list_appointee_permissions(account_address, appointee_address)

#     # Assertions
#     mock_list_permissions.assert_called_once_with(account_address, appointee_address)
#     assert isinstance(targets, list), "Expected targets to be a list"
#     assert isinstance(selectors, list), "Expected selectors to be a list"
#     assert targets == [], f"Expected empty list, got: {targets}"
#     assert selectors == [], f"Expected empty list, got: {selectors}"


# def test_list_appointee_permissions_exception(mocker, account_address, appointee_address):
#     """Test list_appointee_permissions() when contract call fails."""

#     # Mock function to simulate an exception
#     mock_list_permissions = mocker.patch.object(
#         el_reader,
#         "list_appointee_permissions",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         targets, selectors = el_reader.list_appointee_permissions(account_address, appointee_address)
#         assert False, f"Expected an exception but got result: {targets}, {selectors}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_list_pending_admins_with_results(mocker, account_address):
#     """Test list_pending_admins() when pending admins exist."""

#     expected_admins = [
#         "0x1111111111111111111111111111111111111111",
#         "0x2222222222222222222222222222222222222222"
#     ]

#     # Mock function response
#     mock_list_pending_admins = mocker.patch.object(
#         el_reader,
#         "list_pending_admins",
#         return_value=expected_admins
#     )

#     # Call the function
#     result = el_reader.list_pending_admins(account_address)

#     # Assertions
#     mock_list_pending_admins.assert_called_once_with(account_address)
#     assert isinstance(result, list), "Expected result to be a list"
#     assert result == expected_admins, f"Expected {expected_admins}, got {result}"


# def test_list_pending_admins_empty(mocker, account_address):
#     """Test list_pending_admins() when no pending admins exist."""

#     expected_admins = []  # No pending admins

#     # Mock function response
#     mock_list_pending_admins = mocker.patch.object(
#         el_reader,
#         "list_pending_admins",
#         return_value=expected_admins
#     )

#     # Call the function
#     result = el_reader.list_pending_admins(account_address)

#     # Assertions
#     mock_list_pending_admins.assert_called_once_with(account_address)
#     assert isinstance(result, list), "Expected result to be a list"
#     assert result == [], f"Expected empty list, got: {result}"


# def test_list_pending_admins_exception(mocker, account_address):
#     """Test list_pending_admins() when contract call fails."""

#     # Mock function to simulate an exception
#     mock_list_pending_admins = mocker.patch.object(
#         el_reader,
#         "list_pending_admins",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.list_pending_admins(account_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_list_admins_with_results(mocker, account_address):
#     """Test list_admins() when admins exist."""

#     expected_admins = [
#         "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
#         "0x2222222222222222222222222222222222222222"
#     ]

#     # Mock function response
#     mock_list_admins = mocker.patch.object(
#         el_reader,
#         "list_admins",
#         return_value=expected_admins
#     )

#     # Call the function
#     result = el_reader.list_admins(account_address)

#     # Assertions
#     mock_list_admins.assert_called_once_with(account_address)
#     assert isinstance(result, list), "Expected result to be a list"
#     assert result == expected_admins, f"Expected {expected_admins}, got {result}"


# def test_list_admins_empty(mocker, account_address):
#     """Test list_admins() when no admins exist."""

#     expected_admins = []  # No admins

#     # Mock function response
#     mock_list_admins = mocker.patch.object(
#         el_reader,
#         "list_admins",
#         return_value=expected_admins
#     )

#     # Call the function
#     result = el_reader.list_admins(account_address)

#     # Assertions
#     mock_list_admins.assert_called_once_with(account_address)
#     assert isinstance(result, list), "Expected result to be a list"
#     assert result == [], f"Expected empty list, got: {result}"


# def test_list_admins_exception(mocker, account_address):
#     """Test list_admins() when contract call fails."""

#     # Mock function to simulate an exception
#     mock_list_admins = mocker.patch.object(
#         el_reader,
#         "list_admins",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.list_admins(account_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_is_pending_admin_true(mocker, account_address, pending_admin_address):
#     """Test is_pending_admin() when the pending admin exists (should return True)."""

#     # Mock function response
#     mock_is_pending_admin = mocker.patch.object(
#         el_reader,
#         "is_pending_admin",
#         return_value=True
#     )

#     # Call the function
#     result = el_reader.is_pending_admin(account_address, pending_admin_address)

#     # Assertions
#     mock_is_pending_admin.assert_called_once_with(account_address, pending_admin_address)
#     assert isinstance(result, bool), "Expected result to be a boolean"
#     assert result is True, f"Expected True, got {result}"


# def test_is_pending_admin_false(mocker, account_address, pending_admin_address):
#     """Test is_pending_admin() when no pending admin exists (should return False)."""

#     # Mock function response
#     mock_is_pending_admin = mocker.patch.object(
#         el_reader,
#         "is_pending_admin",
#         return_value=False
#     )

#     # Call the function
#     result = el_reader.is_pending_admin(account_address, pending_admin_address)

#     # Assertions
#     mock_is_pending_admin.assert_called_once_with(account_address, pending_admin_address)
#     assert isinstance(result, bool), "Expected result to be a boolean"
#     assert result is False, f"Expected False, got {result}"


# def test_is_pending_admin_exception(mocker, account_address, pending_admin_address):
#     """Test is_pending_admin() when contract call fails."""

#     # Mock function to simulate an exception
#     mock_is_pending_admin = mocker.patch.object(
#         el_reader,
#         "is_pending_admin",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.is_pending_admin(account_address, pending_admin_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_is_admin_true(mocker, account_address, admin_address):
#     """Test is_admin() when the admin exists (should return True)."""

#     # Mock function response
#     mock_is_admin = mocker.patch.object(
#         el_reader,
#         "is_admin",
#         return_value=True
#     )

#     # Call the function
#     result = el_reader.is_admin(account_address, admin_address)

#     # Assertions
#     mock_is_admin.assert_called_once_with(account_address, admin_address)
#     assert isinstance(result, bool), "Expected result to be a boolean"
#     assert result is True, f"Expected True, got {result}"


# def test_is_admin_false(mocker, account_address, admin_address):
#     """Test is_admin() when the account is NOT an admin (should return False)."""

#     # Mock function response
#     mock_is_admin = mocker.patch.object(
#         el_reader,
#         "is_admin",
#         return_value=False
#     )

#     # Call the function
#     result = el_reader.is_admin(account_address, admin_address)

#     # Assertions
#     mock_is_admin.assert_called_once_with(account_address, admin_address)
#     assert isinstance(result, bool), "Expected result to be a boolean"
#     assert result is False, f"Expected False, got {result}"


# def test_is_admin_exception(mocker, account_address, admin_address):
#     """Test is_admin() when contract call fails (should raise an exception)."""

#     # Mock function to simulate an exception
#     mock_is_admin = mocker.patch.object(
#         el_reader,
#         "is_admin",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.is_admin(account_address, admin_address)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_get_distribution_roots_length_zero(mocker):
#     """Test get_distribution_roots_length() when there are no distribution roots (should return 0)."""

#     # Mock function response
#     mock_get_length = mocker.patch.object(
#         el_reader,
#         "get_distribution_roots_length",
#         return_value=0
#     )

#     # Call the function
#     result = el_reader.get_distribution_roots_length()

#     # Assertions
#     mock_get_length.assert_called_once()
#     assert isinstance(result, int), "Expected result to be an integer"
#     assert result == 0, f"Expected 0, got {result}"


# def test_get_distribution_roots_length_nonzero(mocker):
#     """Test get_distribution_roots_length() when there are multiple distribution roots."""

#     # Mock function response
#     mock_get_length = mocker.patch.object(
#         el_reader,
#         "get_distribution_roots_length",
#         return_value=5
#     )

#     # Call the function
#     result = el_reader.get_distribution_roots_length()

#     # Assertions
#     mock_get_length.assert_called_once()
#     assert isinstance(result, int), "Expected result to be an integer"
#     assert result == 5, f"Expected 5, got {result}"


# def test_get_distribution_roots_length_exception(mocker):
#     """Test get_distribution_roots_length() when contract call fails (should raise an exception)."""

#     # Mock function to simulate an exception
#     mock_get_length = mocker.patch.object(
#         el_reader,
#         "get_distribution_roots_length",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_distribution_roots_length()
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_curr_rewards_calculation_end_timestamp_zero(mocker):
#     """Test curr_rewards_calculation_end_timestamp() when there is no rewards calculation timestamp (should return 0)."""

#     # Mock function response
#     mock_get_timestamp = mocker.patch.object(
#         el_reader,
#         "curr_rewards_calculation_end_timestamp",
#         return_value=0
#     )

#     # Call the function
#     result = el_reader.curr_rewards_calculation_end_timestamp()

#     # Assertions
#     mock_get_timestamp.assert_called_once()
#     assert isinstance(result, int), "Expected result to be an integer"
#     assert result == 0, f"Expected 0, got {result}"


# def test_curr_rewards_calculation_end_timestamp_future(mocker):
#     """Test curr_rewards_calculation_end_timestamp() when a valid future timestamp is set."""

#     future_timestamp = 1710000000  # Example future timestamp (Unix time)

#     # Mock function response
#     mock_get_timestamp = mocker.patch.object(
#         el_reader,
#         "curr_rewards_calculation_end_timestamp",
#         return_value=future_timestamp
#     )

#     # Call the function
#     result = el_reader.curr_rewards_calculation_end_timestamp()

#     # Assertions
#     mock_get_timestamp.assert_called_once()
#     assert isinstance(result, int), "Expected result to be an integer"
#     assert result == future_timestamp, f"Expected {future_timestamp}, got {result}"


# def test_curr_rewards_calculation_end_timestamp_exception(mocker):
#     """Test curr_rewards_calculation_end_timestamp() when contract call fails (should raise an exception)."""

#     # Mock function to simulate an exception
#     mock_get_timestamp = mocker.patch.object(
#         el_reader,
#         "curr_rewards_calculation_end_timestamp",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.curr_rewards_calculation_end_timestamp()
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_current_claimable_distribution_root_default(mocker):
#     """Test get_current_claimable_distribution_root() when no claimable distribution root exists (should return default values)."""

#     # Default empty distribution root
#     default_root = {
#         'root': b'\x00' * 32,
#         'startBlock': 0,
#         'endBlock': 0,
#         'totalClaimable': False
#     }

#     # Mock function response
#     mock_get_root = mocker.patch.object(
#         el_reader,
#         "get_current_claimable_distribution_root",
#         return_value=default_root
#     )

#     # Call the function
#     result = el_reader.get_current_claimable_distribution_root()

#     # Assertions
#     mock_get_root.assert_called_once()
#     assert isinstance(result, dict), "Expected result to be a dictionary"
#     assert result == default_root, f"Expected {default_root}, got {result}"


# def test_get_current_claimable_distribution_root_populated(mocker):
#     """Test get_current_claimable_distribution_root() when a valid claimable distribution root exists."""

#     populated_root = {
#         'root': b'\x12\x34\x56\x78' + b'\x00' * 28,  # Example non-zero root hash
#         'startBlock': 1500000,
#         'endBlock': 1510000,
#         'totalClaimable': True
#     }

#     # Mock function response
#     mock_get_root = mocker.patch.object(
#         el_reader,
#         "get_current_claimable_distribution_root",
#         return_value=populated_root
#     )

#     # Call the function
#     result = el_reader.get_current_claimable_distribution_root()

#     # Assertions
#     mock_get_root.assert_called_once()
#     assert isinstance(result, dict), "Expected result to be a dictionary"
#     assert result == populated_root, f"Expected {populated_root}, got {result}"


# def test_get_current_claimable_distribution_root_exception(mocker):
#     """Test get_current_claimable_distribution_root() when contract call fails (should raise an exception)."""

#     # Mock function to simulate an exception
#     mock_get_root = mocker.patch.object(
#         el_reader,
#         "get_current_claimable_distribution_root",
#         side_effect=Exception("Contract call failed")
#     )

#     # Call the function and handle exception
#     try:
#         result = el_reader.get_current_claimable_distribution_root()
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_root_index_from_hash_found(mocker):
#     """Test get_root_index_from_hash() when the root hash exists (should return a valid index)."""

#     root_hash = "0xa3d1e5f47b6c9f8e2d3c4b5a6e7f8d9c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d"

#     # Mock the contract method to return index 5
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getRootIndexFromHash.return_value.call.return_value = 5
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_root_index_from_hash(root_hash)

#     # Assertions
#     assert result == 5, f"Expected index 5, but got {result}"


# def test_get_root_index_from_hash_not_found(mocker):
#     """Test get_root_index_from_hash() when the root hash does not exist (should return 0 or handle gracefully)."""

#     root_hash = "0xb3d1e5f47b6c9f8e2d3c4b5a6e7f8d9c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d"

#     # Mock the contract method to return 0 (not found)
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getRootIndexFromHash.return_value.call.return_value = 0
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_root_index_from_hash(root_hash)

#     # Assertions
#     assert result == 0, f"Expected index 0 (not found), but got {result}"


# def test_get_root_index_from_hash_exception(mocker):
#     """Test get_root_index_from_hash() when contract call fails (should raise an exception)."""

#     root_hash = "0xc3d1e5f47b6c9f8e2d3c4b5a6e7f8d9c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d"

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getRootIndexFromHash.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_root_index_from_hash(root_hash)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_get_root_index_from_hash_found(mocker):
#     """Test get_root_index_from_hash() when the root hash exists (should return a valid index)."""

#     root_hash = "0xa3d1e5f47b6c9f8e2d3c4b5a6e7f8d9c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d"

#     # Mock the contract method to return index 5
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getRootIndexFromHash.return_value.call.return_value = 5
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_root_index_from_hash(root_hash)

#     # Assertions
#     assert result == 5, f"Expected index 5, but got {result}"


# def test_get_root_index_from_hash_not_found(mocker):
#     """Test get_root_index_from_hash() when the root hash does not exist (should return 0 or handle gracefully)."""

#     root_hash = "0xb3d1e5f47b6c9f8e2d3c4b5a6e7f8d9c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d"

#     # Mock the contract method to return 0 (not found)
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getRootIndexFromHash.return_value.call.return_value = 0
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_root_index_from_hash(root_hash)

#     # Assertions
#     assert result == 0, f"Expected index 0 (not found), but got {result}"


# def test_get_root_index_from_hash_exception(mocker):
#     """Test get_root_index_from_hash() when contract call fails (should raise an exception)."""

#     root_hash = "0xc3d1e5f47b6c9f8e2d3c4b5a6e7f8d9c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d"

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getRootIndexFromHash.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_root_index_from_hash(root_hash)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_cumulative_claimed_zero(mocker, earner, token):
#     """Test get_cumulative_claimed() when no claims have been made (should return 0)."""

#     # Mock contract method to return 0
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getCumulativeClaimed.return_value.call.return_value = 0
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_cumulative_claimed(earner, token)

#     # Assertions
#     assert result == 0, f"Expected cumulative claimed to be 0, but got {result}"


# def test_get_cumulative_claimed_non_zero(mocker, earner, token):
#     """Test get_cumulative_claimed() when claims have been made (should return a valid amount)."""

#     claimed_amount = 1000  # Simulated claimed amount

#     # Mock contract method to return claimed_amount
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getCumulativeClaimed.return_value.call.return_value = claimed_amount
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_cumulative_claimed(earner, token)

#     # Assertions
#     assert result == claimed_amount, f"Expected cumulative claimed to be {claimed_amount}, but got {result}"


# def test_get_cumulative_claimed_exception(mocker, earner, token):
#     """Test get_cumulative_claimed() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getCumulativeClaimed.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_cumulative_claimed(earner, token)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_check_claim_invalid(mocker, claim):
#     """Test check_claim() when the claim is invalid (should return False)."""

#     # Mock contract method to return False (claim is invalid)
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.checkClaim.return_value.call.return_value = False
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.check_claim(claim)

#     # Assertions
#     assert result is False, f"Expected check_claim to return False, but got {result}"


# def test_check_claim_valid(mocker, claim):
#     """Test check_claim() when the claim is valid (should return True)."""

#     # Mock contract method to return True (claim is valid)
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.checkClaim.return_value.call.return_value = True
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.check_claim(claim)

#     # Assertions
#     assert result is True, f"Expected check_claim to return True, but got {result}"


# def test_check_claim_exception(mocker, claim):
#     """Test check_claim() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.checkClaim.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.check_claim(claim)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_check_claim_invalid(mocker, claim):
#     """Test check_claim() when the claim is invalid (should return False)."""

#     # Mock contract method to return False (invalid claim)
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.checkClaim.return_value.call.return_value = False
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.check_claim(claim)

#     # Assertions
#     assert result is False, f"Expected check_claim to return False, but got {result}"


# def test_check_claim_valid(mocker, claim):
#     """Test check_claim() when the claim is valid (should return True)."""

#     # Mock contract method to return True (valid claim)
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.checkClaim.return_value.call.return_value = True
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.check_claim(claim)

#     # Assertions
#     assert result is True, f"Expected check_claim to return True, but got {result}"


# def test_check_claim_exception(mocker, claim):
#     """Test check_claim() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.checkClaim.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.check_claim(claim)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_get_operator_avs_split_valid(mocker, operator, avs):
#     """Test get_operator_avs_split() when a valid operator and AVS are provided (should return 1000)."""

#     # Mock contract method to return 1000 (valid operator/AVS split)
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.getOperatorAVSSplit.return_value.call.return_value = 1000
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call function
#     result = el_reader.get_operator_avs_split(operator, avs)

#     # Assertions
#     assert result == 1000, f"Expected get_operator_avs_split to return 1000, but got {result}"


# def test_get_operator_avs_split_invalid(mocker, operator, avs):
#     """Test get_operator_avs_split() when an invalid operator or AVS is provided (should return 0)."""

#     # Mock contract method to return 0 (invalid operator/AVS)
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.getOperatorAVSSplit.return_value.call.return_value = 0
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call function
#     result = el_reader.get_operator_avs_split(operator, avs)

#     # Assertions
#     assert result == 0, f"Expected get_operator_avs_split to return 0, but got {result}"


# def test_get_operator_avs_split_exception(mocker, operator, avs):
#     """Test get_operator_avs_split() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.getOperatorAVSSplit.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_operator_avs_split(operator, avs)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_get_operator_pi_split_valid(mocker, operator):
#     """Test get_operator_pi_split() when a valid operator is provided (should return 1000)."""

#     # Mock contract method to return 1000 (valid operator)
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.getOperatorPISplit.return_value.call.return_value = 1000
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call function
#     result = el_reader.get_operator_pi_split(operator)

#     # Assertions
#     assert result == 1000, f"Expected get_operator_pi_split to return 1000, but got {result}"


# def test_get_operator_pi_split_invalid(mocker, operator):
#     """Test get_operator_pi_split() when an invalid operator is provided (should return 0)."""

#     # Mock contract method to return 0 (invalid operator)
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.getOperatorPISplit.return_value.call.return_value = 0
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call function
#     result = el_reader.get_operator_pi_split(operator)

#     # Assertions
#     assert result == 0, f"Expected get_operator_pi_split to return 0, but got {result}"


# def test_get_operator_pi_split_exception(mocker, operator):
#     """Test get_operator_pi_split() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.getOperatorPISplit.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_operator_pi_split(operator)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_get_operator_set_split_valid(mocker):
#     """Test get_operator_set_split() when valid operator and operator set are provided (should return 1000)."""

#     operator = "0x1111111111111111111111111111111111111111"
#     operator_set = {"avs": "0x2222222222222222222222222222222222222222", "id": 1}

#     # Mock contract method to return 1000 (valid case)
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.getOperatorSetSplit.return_value.call.return_value = 1000
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call function
#     result = el_reader.get_operator_set_split(operator, operator_set)

#     # Assertions
#     assert result == 1000, f"Expected get_operator_set_split to return 1000, but got {result}"


# def test_get_operator_set_split_invalid(mocker):
#     """Test get_operator_set_split() when an invalid operator and operator set are provided (should return 0)."""

#     operator = "0x0000000000000000000000000000000000000000"
#     operator_set = {"avs": "0x0000000000000000000000000000000000000000", "id": 0}

#     # Mock contract method to return 0 (invalid case)
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.getOperatorSetSplit.return_value.call.return_value = 0
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call function
#     result = el_reader.get_operator_set_split(operator, operator_set)

#     # Assertions
#     assert result == 0, f"Expected get_operator_set_split to return 0, but got {result}"


# def test_get_operator_set_split_exception(mocker):
#     """Test get_operator_set_split() when contract call fails (should raise an exception)."""

#     operator = "0x1111111111111111111111111111111111111111"
#     operator_set = {"avs": "0x2222222222222222222222222222222222222222", "id": 1}

#     # Mock contract method to raise an exception
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.getOperatorSetSplit.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_operator_set_split(operator, operator_set)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_get_rewards_updater_valid(mocker):
#     """Test get_rewards_updater() when a valid rewards updater is set (should return correct address)."""

#     expected_address = "0x18a0f92Ad9645385E8A8f3db7d0f6CF7aBBb0aD4"

#     # Mock contract method to return expected address
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.rewardsUpdater.return_value.call.return_value = expected_address
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_rewards_updater()

#     # Assertions
#     assert str(result) == expected_address, f"Expected {expected_address}, but got {result}"


# def test_get_rewards_updater_no_updater(mocker):
#     """Test get_rewards_updater() when no rewards updater is set (should return zero address)."""

#     expected_address = "0x0000000000000000000000000000000000000000"

#     # Mock contract method to return zero address
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.rewardsUpdater.return_value.call.return_value = expected_address
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_rewards_updater()

#     # Assertions
#     assert str(result) == expected_address, f"Expected {expected_address}, but got {result}"


# def test_get_rewards_updater_exception(mocker):
#     """Test get_rewards_updater() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.rewardsUpdater.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_rewards_updater()
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_activation_delay_valid(mocker):
#     """Test GetActivationDelay() when a valid activation delay is set (should return correct value)."""

#     expected_delay = 10

#     # Mock contract method to return expected delay
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.activationDelay.return_value.call.return_value = expected_delay
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.GetActivationDelay()

#     # Assertions
#     assert result == expected_delay, f"Expected {expected_delay}, but got {result}"


# def test_get_activation_delay_zero(mocker):
#     """Test GetActivationDelay() when the activation delay is set to zero (should return 0)."""

#     expected_delay = 0

#     # Mock contract method to return zero delay
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.activationDelay.return_value.call.return_value = expected_delay
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.GetActivationDelay()

#     # Assertions
#     assert result == expected_delay, f"Expected {expected_delay}, but got {result}"


# def test_get_activation_delay_exception(mocker):
#     """Test GetActivationDelay() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.activationDelay.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.GetActivationDelay()
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_curr_rewards_calculation_end_timestamp_valid(mocker):
#     """Test get_curr_rewards_calculation_end_timestamp() when a valid timestamp is set (should return correct value)."""

#     expected_timestamp = 1700000000  # Example Unix timestamp

#     # Mock contract method to return expected timestamp
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.currRewardsCalculationEndTimestamp.return_value.call.return_value = expected_timestamp
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_curr_rewards_calculation_end_timestamp()

#     # Assertions
#     assert result == expected_timestamp, f"Expected {expected_timestamp}, but got {result}"


# def test_get_curr_rewards_calculation_end_timestamp_zero(mocker):
#     """Test get_curr_rewards_calculation_end_timestamp() when the timestamp is zero (should return 0)."""

#     expected_timestamp = 0  # No rewards calculation has ended

#     # Mock contract method to return zero timestamp
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.currRewardsCalculationEndTimestamp.return_value.call.return_value = expected_timestamp
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_curr_rewards_calculation_end_timestamp()

#     # Assertions
#     assert result == expected_timestamp, f"Expected {expected_timestamp}, but got {result}"


# def test_get_curr_rewards_calculation_end_timestamp_exception(mocker):
#     """Test get_curr_rewards_calculation_end_timestamp() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.currRewardsCalculationEndTimestamp.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_curr_rewards_calculation_end_timestamp()
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_default_operator_split_bips_valid(mocker):
#     """Test get_default_operator_split_bips() when a valid split value is set (should return correct value)."""

#     expected_bips = 1000  # Example default split BIPS

#     # Mock contract method to return expected BIPS value
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.defaultOperatorSplitBips.return_value.call.return_value = expected_bips
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_default_operator_split_bips()

#     # Assertions
#     assert result == expected_bips, f"Expected {expected_bips}, but got {result}"


# def test_get_default_operator_split_bips_zero(mocker):
#     """Test get_default_operator_split_bips() when the split is zero (should return 0)."""

#     expected_bips = 0  # Example case where split BIPS is 0

#     # Mock contract method to return zero
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.defaultOperatorSplitBips.return_value.call.return_value = expected_bips
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_default_operator_split_bips()

#     # Assertions
#     assert result == expected_bips, f"Expected {expected_bips}, but got {result}"


# def test_get_default_operator_split_bips_exception(mocker):
#     """Test get_default_operator_split_bips() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.defaultOperatorSplitBips.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_default_operator_split_bips()
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_claimer_for_valid(mocker, earner):
#     """Test get_claimer_for() when a valid claimer is set (should return correct address)."""

#     expected_claimer = "0x1234567890abcdef1234567890abcdef12345678"  # Example valid claimer address

#     # Mock contract method to return expected claimer address
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.claimerFor.return_value.call.return_value = expected_claimer
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_claimer_for(earner)

#     # Assertions
#     assert str(result) == expected_claimer, f"Expected {expected_claimer}, but got {result}"


# def test_get_claimer_for_zero(mocker, earner):
#     """Test get_claimer_for() when no claimer is set (should return zero address)."""

#     expected_claimer = "0x0000000000000000000000000000000000000000"  # Default empty claimer

#     # Mock contract method to return zero address
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.claimerFor.return_value.call.return_value = expected_claimer
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_claimer_for(earner)

#     # Assertions
#     assert str(result) == expected_claimer, f"Expected {expected_claimer}, but got {result}"


# def test_get_claimer_for_exception(mocker, earner):
#     """Test get_claimer_for() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.claimerFor.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_claimer_for(earner)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_submission_nonce_valid(mocker, avs):
#     """Test get_submission_nonce() when a valid nonce is returned (should return correct integer)."""

#     expected_nonce = 42  # Example valid nonce

#     # Mock contract method to return expected nonce
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.submissionNonces.return_value.call.return_value = expected_nonce
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_submission_nonce(avs)

#     # Assertions
#     assert result == expected_nonce, f"Expected {expected_nonce}, but got {result}"


# def test_get_submission_nonce_zero(mocker, avs):
#     """Test get_submission_nonce() when no submissions have been made (should return zero)."""

#     expected_nonce = 0  # Default empty nonce

#     # Mock contract method to return zero
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.submissionNonces.return_value.call.return_value = expected_nonce
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_submission_nonce(avs)

#     # Assertions
#     assert result == expected_nonce, f"Expected {expected_nonce}, but got {result}"


# def test_get_submission_nonce_exception(mocker, avs):
#     """Test get_submission_nonce() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.submissionNonces.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_submission_nonce(avs)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"

# def test_get_is_avs_rewards_submission_hash_valid(mocker, avs, submission_hash):
#     """Test get_is_avs_rewards_submission_hash() when a valid submission hash exists (should return True)."""

#     expected_result = True  # Example: Submission hash exists

#     # Mock contract method to return expected result
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsAVSRewardsSubmissionHash.return_value.call.return_value = expected_result
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_is_avs_rewards_submission_hash(avs, submission_hash)

#     # Assertions
#     assert result == expected_result, f"Expected {expected_result}, but got {result}"


# def test_get_is_avs_rewards_submission_hash_invalid(mocker, avs, submission_hash):
#     """Test get_is_avs_rewards_submission_hash() when submission hash is invalid (should return False)."""

#     expected_result = False  # Example: Submission hash does not exist

#     # Mock contract method to return expected result
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsAVSRewardsSubmissionHash.return_value.call.return_value = expected_result
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function
#     result = el_reader.get_is_avs_rewards_submission_hash(avs, submission_hash)

#     # Assertions
#     assert result == expected_result, f"Expected {expected_result}, but got {result}"


# def test_get_is_avs_rewards_submission_hash_exception(mocker, avs, submission_hash):
#     """Test get_is_avs_rewards_submission_hash() when contract call fails (should raise an exception)."""

#     # Mock contract method to raise an exception
#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsAVSRewardsSubmissionHash.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     # Call function and check for exception handling
#     try:
#         result = el_reader.get_is_avs_rewards_submission_hash(avs, submission_hash)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed", f"Unexpected exception message: {e}"


# def test_get_is_rewards_submission_for_all_hash_valid(mocker, avs, submission_hash):
#     """Test get_is_rewards_submission_for_all_hash() when submission hash is valid (should return True)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsRewardsSubmissionForAllHash.return_value.call.return_value = True
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     result = el_reader.get_is_rewards_submission_for_all_hash(avs, submission_hash)
#     assert result is True


# def test_get_is_rewards_submission_for_all_hash_invalid(mocker, avs, submission_hash):
#     """Test get_is_rewards_submission_for_all_hash() when submission hash is invalid (should return False)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsRewardsSubmissionForAllHash.return_value.call.return_value = False
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     result = el_reader.get_is_rewards_submission_for_all_hash(avs, submission_hash)
#     assert result is False


# def test_get_is_rewards_submission_for_all_hash_exception(mocker, avs, submission_hash):
#     """Test get_is_rewards_submission_for_all_hash() when contract call fails (should raise an exception)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsRewardsSubmissionForAllHash.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     try:
#         result = el_reader.get_is_rewards_submission_for_all_hash(avs, submission_hash)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed"


# def test_get_is_rewards_for_all_submitter_valid(mocker, submitter):
#     """Test get_is_rewards_for_all_submitter() when submitter is valid (should return True)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsRewardsForAllSubmitter.return_value.call.return_value = True
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     result = el_reader.get_is_rewards_for_all_submitter(submitter)
#     assert result is True


# def test_get_is_rewards_for_all_submitter_invalid(mocker, submitter):
#     """Test get_is_rewards_for_all_submitter() when submitter is not registered (should return False)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsRewardsForAllSubmitter.return_value.call.return_value = False
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     result = el_reader.get_is_rewards_for_all_submitter(submitter)
#     assert result is False


# def test_get_is_rewards_for_all_submitter_exception(mocker, submitter):
#     """Test get_is_rewards_for_all_submitter() when contract call fails (should raise an exception)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsRewardsForAllSubmitter.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     try:
#         result = el_reader.get_is_rewards_for_all_submitter(submitter)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed"


# def test_get_is_rewards_submission_for_all_earners_hash_valid(mocker, avs, submission_hash):
#     """Test get_is_rewards_submission_for_all_earners_hash() when submission hash exists (should return True)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsRewardsSubmissionForAllEarnersHash.return_value.call.return_value = True
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     result = el_reader.get_is_rewards_submission_for_all_earners_hash(avs, submission_hash)
#     assert result is True


# def test_get_is_rewards_submission_for_all_earners_hash_invalid(mocker, avs, submission_hash):
#     """Test get_is_rewards_submission_for_all_earners_hash() when submission hash is invalid (should return False)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsRewardsSubmissionForAllEarnersHash.return_value.call.return_value = False
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     result = el_reader.get_is_rewards_submission_for_all_earners_hash(avs, submission_hash)
#     assert result is False


# def test_get_is_rewards_submission_for_all_earners_hash_exception(mocker, avs, submission_hash):
#     """Test get_is_rewards_submission_for_all_earners_hash() when contract call fails (should raise an exception)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsRewardsSubmissionForAllEarnersHash.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     try:
#         result = el_reader.get_is_rewards_submission_for_all_earners_hash(avs, submission_hash)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed"

# def test_get_is_operator_directed_avs_rewards_submission_hash_valid(mocker, avs, submission_hash):
#     """Test get_is_operator_directed_avs_rewards_submission_hash() when submission hash exists (should return True)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsOperatorDirectedAVSRewardsSubmissionHash.return_value.call.return_value = True
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     result = el_reader.get_is_operator_directed_avs_rewards_submission_hash(avs, submission_hash)
#     assert result is True


# def test_get_is_operator_directed_avs_rewards_submission_hash_invalid(mocker, avs, submission_hash):
#     """Test get_is_operator_directed_avs_rewards_submission_hash() when submission hash is invalid (should return False)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsOperatorDirectedAVSRewardsSubmissionHash.return_value.call.return_value = False
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     result = el_reader.get_is_operator_directed_avs_rewards_submission_hash(avs, submission_hash)
#     assert result is False


# def test_get_is_operator_directed_avs_rewards_submission_hash_exception(mocker, avs, submission_hash):
#     """Test get_is_operator_directed_avs_rewards_submission_hash() when contract call fails (should raise an exception)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsOperatorDirectedAVSRewardsSubmissionHash.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     try:
#         result = el_reader.get_is_operator_directed_avs_rewards_submission_hash(avs, submission_hash)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed"

# def test_get_is_operator_directed_operator_set_rewards_submission_hash_valid(mocker, avs, submission_hash):
#     """Test get_is_operator_directed_operator_set_rewards_submission_hash() when submission hash exists (should return True)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsOperatorDirectedOperatorSetRewardsSubmissionHash.return_value.call.return_value = True
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     result = el_reader.get_is_operator_directed_operator_set_rewards_submission_hash(avs, submission_hash)
#     assert result is True


# def test_get_is_operator_directed_operator_set_rewards_submission_hash_invalid(mocker, avs, submission_hash):
#     """Test get_is_operator_directed_operator_set_rewards_submission_hash() when submission hash is invalid (should return False)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsOperatorDirectedOperatorSetRewardsSubmissionHash.return_value.call.return_value = False
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     result = el_reader.get_is_operator_directed_operator_set_rewards_submission_hash(avs, submission_hash)
#     assert result is False


# def test_get_is_operator_directed_operator_set_rewards_submission_hash_exception(mocker, avs, submission_hash):
#     """Test get_is_operator_directed_operator_set_rewards_submission_hash() when contract call fails (should raise an exception)."""

#     mock_reward_coordinator = mocker.MagicMock()
#     mock_reward_coordinator.functions.getIsOperatorDirectedOperatorSetRewardsSubmissionHash.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_reward_coordinator)

#     try:
#         result = el_reader.get_is_operator_directed_operator_set_rewards_submission_hash(avs, submission_hash)
#         assert False, f"Expected an exception but got result: {result}"
#     except Exception as e:
#         assert str(e) == "Contract call failed"

# def test_calculate_operator_avs_registration_digest_hash_valid(mocker, operator, avs, salt, expiry):
#     """Test calculate_operator_avs_registration_digest_hash() with valid input."""

#     # Expected digest hash
#     expected_hash = b'u\xf4\xe3\x91^\x9c\x01\xe6\xe9\xeb\xbdH\xa1\x9b\xd7\xfd\xbf\xde\xf7\x1c\xe2;\xa8\xd9\xccc\x8f\xda=xw\x80'

#     # Mock the contract function to return the expected hash
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.CalculateOperatorAVSRegistrationDigestHash.return_value.call.return_value = expected_hash
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call the function
#     result, error = el_reader.calculate_operator_avs_registration_digest_hash(operator, avs, salt, expiry)

#     # Assertions
#     assert error is None, f"Unexpected error: {error}"
#     assert result == expected_hash


# def test_calculate_operator_avs_registration_digest_hash_invalid(mocker, operator, avs, salt, expiry):
#     """Test calculate_operator_avs_registration_digest_hash() when invalid data is used (should return error)."""

#     # Mock the contract function to return None (invalid case)
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.CalculateOperatorAVSRegistrationDigestHash.return_value.call.return_value = None
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call the function
#     result, error = el_reader.calculate_operator_avs_registration_digest_hash(operator, avs, salt, expiry)

#     # Assertions
#     assert result is None
#     assert isinstance(error, ValueError)


# def test_calculate_operator_avs_registration_digest_hash_exception(mocker, operator, avs, salt, expiry):
#     """Test calculate_operator_avs_registration_digest_hash() when contract call fails."""

#     # Mock the contract function to raise an exception
#     mock_avs_directory = mocker.MagicMock()
#     mock_avs_directory.functions.CalculateOperatorAVSRegistrationDigestHash.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "avs_directory", mock_avs_directory)

#     # Call the function
#     result, error = el_reader.calculate_operator_avs_registration_digest_hash(operator, avs, salt, expiry)

#     # Assertions
#     assert result is None
#     assert str(error) == "Contract call failed"

# def test_get_calculation_interval_seconds_valid(mocker):
#     """Test get_calculation_interval_seconds() with a valid contract response."""

#     # Mock the contract function to return expected value
#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.CALCULATION_INTERVAL_SECONDS.return_value.call.return_value = 604800
#     mocker.patch.object(el_reader, "rewards_coordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_calculation_interval_seconds()

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 604800


# def test_get_calculation_interval_seconds_none(mocker):
#     """Test get_calculation_interval_seconds() when contract returns None (invalid case)."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.CALCULATION_INTERVAL_SECONDS.return_value.call.return_value = None
#     mocker.patch.object(el_reader, "rewards_coordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_calculation_interval_seconds()

#     assert result is None
#     assert isinstance(error, ValueError)


# def test_get_calculation_interval_seconds_exception(mocker):
#     """Test get_calculation_interval_seconds() when contract call fails."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.CALCULATION_INTERVAL_SECONDS.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "rewards_coordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_calculation_interval_seconds()

#     assert result is None
#     assert str(error) == "Contract call failed"

#     def test_get_max_rewards_duration_valid(mocker):
#     """Test get_max_rewards_duration() with a valid contract response."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_REWARDS_DURATION.return_value.call.return_value = 604800
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_rewards_duration()

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 604800


# def test_get_max_rewards_duration_none(mocker):
#     """Test get_max_rewards_duration() when contract returns None (invalid case)."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_REWARDS_DURATION.return_value.call.return_value = None
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_rewards_duration()

#     assert result is None
#     assert isinstance(error, ValueError)


# def test_get_max_rewards_duration_exception(mocker):
#     """Test get_max_rewards_duration() when contract call fails."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_REWARDS_DURATION.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_rewards_duration()

#     assert result is None
#     assert str(error) == "Contract call failed"

# def test_get_max_retroactive_length_valid(mocker):
#     """Test get_max_retroactive_length() with a valid contract response."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_RETROACTIVE_LENGTH.return_value.call.return_value = 7776000
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_retroactive_length()

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 7776000


# def test_get_max_retroactive_length_none(mocker):
#     """Test get_max_retroactive_length() when contract returns None (invalid case)."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_RETROACTIVE_LENGTH.return_value.call.return_value = None
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_retroactive_length()

#     assert result is None
#     assert isinstance(error, ValueError)


# def test_get_max_retroactive_length_exception(mocker):
#     """Test get_max_retroactive_length() when contract call fails."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_RETROACTIVE_LENGTH.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_retroactive_length()

#     assert result is None
#     assert str(error) == "Contract call failed"


# def test_get_max_future_length_valid(mocker):
#     """Test get_max_future_length() with a valid contract response."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_FUTURE_LENGTH.return_value.call.return_value = 2592000
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_future_length()

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 2592000


# def test_get_max_future_length_none(mocker):
#     """Test get_max_future_length() when contract returns None (invalid case)."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_FUTURE_LENGTH.return_value.call.return_value = None
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_future_length()

#     assert result is None
#     assert isinstance(error, ValueError)


# def test_get_max_future_length_exception(mocker):
#     """Test get_max_future_length() when contract call fails."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_FUTURE_LENGTH.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_future_length()

#     assert result is None
#     assert str(error) == "Contract call failed"

# def test_get_activation_delay_valid(mocker):
#     """Test get_activation_delay() with a valid contract response."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.activationDelay.return_value.call.return_value = 7200
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_activation_delay()

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 7200


# def test_get_activation_delay_none(mocker):
#     """Test get_activation_delay() when contract returns None (invalid case)."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.activationDelay.return_value.call.return_value = None
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_activation_delay()

#     assert result is None
#     assert isinstance(error, ValueError)


# def test_get_activation_delay_exception(mocker):
#     """Test get_activation_delay() when contract call fails."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.activationDelay.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_activation_delay()

#     assert result is None
#     assert str(error) == "Contract call failed"

# def test_get_deallocation_delay_valid(mocker):
#     """Test get_deallocation_delay() with a valid contract response."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.DEALLOCATION_DELAY.return_value.call.return_value = 900
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_deallocation_delay()

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 900


# def test_get_deallocation_delay_none(mocker):
#     """Test get_deallocation_delay() when contract returns None (invalid case)."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.DEALLOCATION_DELAY.return_value.call.return_value = None
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_deallocation_delay()

#     assert result is None
#     assert isinstance(error, ValueError)


# def test_get_deallocation_delay_exception(mocker):
#     """Test get_deallocation_delay() when contract call fails."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.DEALLOCATION_DELAY.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_deallocation_delay()

#     assert result is None
#     assert str(error) == "Contract call failed"


# def test_get_max_future_length_valid(mocker):
#     """Test get_max_future_length() with a valid contract response."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_FUTURE_LENGTH.return_value.call.return_value = 2592000
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_future_length()

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 2592000


# def test_get_max_future_length_none(mocker):
#     """Test get_max_future_length() when contract returns None (invalid case)."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_FUTURE_LENGTH.return_value.call.return_value = None
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_future_length()

#     assert result is None
#     assert isinstance(error, ValueError)


# def test_get_max_future_length_exception(mocker):
#     """Test get_max_future_length() when contract call fails."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.MAX_FUTURE_LENGTH.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_max_future_length()

#     assert result is None
#     assert str(error) == "Contract call failed"


# def test_get_activation_delay_valid(mocker):
#     """Test get_activation_delay() with a valid contract response."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.activationDelay.return_value.call.return_value = 7200
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_activation_delay()

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 7200


# def test_get_activation_delay_none(mocker):
#     """Test get_activation_delay() when contract returns None (invalid case)."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.activationDelay.return_value.call.return_value = None
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_activation_delay()

#     assert result is None
#     assert isinstance(error, ValueError)


# def test_get_activation_delay_exception(mocker):
#     """Test get_activation_delay() when contract call fails."""

#     mock_rewards_coordinator = mocker.MagicMock()
#     mock_rewards_coordinator.functions.activationDelay.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "reward_cordinator", mock_rewards_coordinator)

#     result, error = el_reader.get_activation_delay()

#     assert result is None
#     assert str(error) == "Contract call failed"

# def test_get_deallocation_delay_valid(mocker):
#     """Test get_deallocation_delay() with a valid contract response."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.DEALLOCATION_DELAY.return_value.call.return_value = 900
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_deallocation_delay()

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 900


# def test_get_deallocation_delay_none(mocker):
#     """Test get_deallocation_delay() when contract returns None (invalid case)."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.DEALLOCATION_DELAY.return_value.call.return_value = None
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_deallocation_delay()

#     assert result is None
#     assert isinstance(error, ValueError)


# def test_get_deallocation_delay_exception(mocker):
#     """Test get_deallocation_delay() when contract call fails."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.DEALLOCATION_DELAY.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_deallocation_delay()

#     assert result is None
#     assert str(error) == "Contract call failed"

# def test_get_allocation_configuration_delay_valid(mocker):
#     """Test get_allocation_configuration_delay() with a valid contract response."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.ALLOCATION_CONFIGURATION_DELAY.return_value.call.return_value = 1200
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_allocation_configuration_delay()

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 1200


# def test_get_allocation_configuration_delay_none(mocker):
#     """Test get_allocation_configuration_delay() when contract returns None (invalid case)."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.ALLOCATION_CONFIGURATION_DELAY.return_value.call.return_value = None
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_allocation_configuration_delay()

#     assert result is None
#     assert isinstance(error, ValueError)


# def test_get_allocation_configuration_delay_exception(mocker):
#     """Test get_allocation_configuration_delay() when contract call fails."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.ALLOCATION_CONFIGURATION_DELAY.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_allocation_configuration_delay()

#     assert result is None
#     assert str(error) == "Contract call failed"

# def test_get_num_operator_sets_for_operator_empty(mocker, operator_address):
#     """Test when the operator is not part of any operator set (returns 0)."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getAllocatedSets.return_value.call.return_value = []
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_num_operator_sets_for_operator(operator_address)

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 0


# def test_get_num_operator_sets_for_operator_multiple_sets(mocker, operator_address):
#     """Test when the operator is part of multiple operator sets (returns count)."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getAllocatedSets.return_value.call.return_value = [1, 2, 3]
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_num_operator_sets_for_operator(operator_address)

#     assert error is None, f"Unexpected error: {error}"
#     assert result == 3


# def test_get_num_operator_sets_for_operator_contract_error(mocker, operator_address):
#     """Test when the contract call fails (should return error)."""

#     mock_allocation_manager = mocker.MagicMock()
#     mock_allocation_manager.functions.getAllocatedSets.return_value.call.side_effect = Exception("Contract call failed")
#     mocker.patch.object(el_reader, "allocation_manager", mock_allocation_manager)

#     result, error = el_reader.get_num_operator_sets_for_operator(operator_address)

#     assert result is None
#     assert str(error) == "Contract call failed"
