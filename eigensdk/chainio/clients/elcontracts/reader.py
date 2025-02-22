import logging
from typing import Tuple, List, Any , Dict

from eth_typing import Address
from web3 import Web3
from web3.contract.contract import Contract

from eigensdk._types import Operator
from eigensdk.contracts import ABIs


class ELReader:
    def __init__(
        self,
        allocation_manager: Contract,
        avs_directory: Contract,
        delegation_manager: Contract,
        permissioncontrol: Contract,
        reward_cordinator: Contract,
        strategy_manager: Contract,
        logger: logging.Logger,
        eth_http_client: Web3,
    ):
        self.allocation_manager = allocation_manager
        self.avs_directory = avs_directory
        self.delegation_manager = delegation_manager
        self.permissioncontrol = permissioncontrol
        self.reward_cordinator = reward_cordinator
        self.strategy_manager = strategy_manager
        self.eth_http_client = eth_http_client
        self.logger = logger

    # -------------------------------------------------------
    # AllocationManager
    # -------------------------------------------------------
    def get_allocatable_magnitude(
        self,
        operator_addr: Address,
        strategy_addr: Address
    ) -> int:
        # Check if we have a valid AllocationManager contract instance
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")
        
        # Perform the read-only call to the Solidity function `getAllocatableMagnitude(operator, strategy)`
        allocatable_magnitude: int = self.allocation_manager.functions.getAllocatableMagnitude(
            operator_addr, 
            strategy_addr
        ).call()

        return allocatable_magnitude

    def get_encumbered_magnitude(
        self,
        operator_addr: Address,
        strategy_addr: Address
    ) -> int:
       
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        encumbered_magnitude: int = self.allocation_manager.functions.EncumberedMagnitude(
            operator_addr,
            strategy_addr
        ).call()

        return encumbered_magnitude

    def get_deallocation_delay(self) -> int:
        
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        # Call the Solidity function/variable `DEALLOCATIONDELAY`
        deallocation_delay: int = self.allocation_manager.functions.DEALLOCATIONDELAY().call()
        return deallocation_delay


    def get_allocation_configuration_delay(self) -> int:
        
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        allocation_configuration_delay: int = (
            self.allocation_manager.functions.ALLOCATIONCONFIGURATIONDELAY().call()
        )
        return allocation_configuration_delay

    def get_max_magnitudes(
            self,
            operator_addr: Address,
            strategy_addrs: List[Address]
        ) -> List[int]:
            if self.allocation_manager is None:
                raise ValueError("AllocationManager contract not provided")

            # In the Go version, the Solidity function name is `GetMaxMagnitudes0`. 
            # Adapt it exactly as your contract's ABI specifies:
            max_magnitudes: List[int] = self.allocation_manager.functions.GetMaxMagnitudes0(
                operator_addr, 
                strategy_addrs
            ).call()

            return max_magnitudes

    def get_allocation_info(self, operator_addr: Address, strategy_addr: Address) -> List[Dict[str, Any]]:
        
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        # Call the contract function that returns (opSets, allocationInfo)
        # The function name below must match your contract's ABI exactly.
        # For example: .GetStrategyAllocations(operator_addr, strategy_addr).call()
        # Adjust as needed if the actual name differs.
        op_sets, allocation_info = self.allocation_manager.functions.GetStrategyAllocations(
            operator_addr,
            strategy_addr
        ).call()

        # op_sets and allocation_info should be lists/tuples of the same length
        if len(op_sets) != len(allocation_info):
            raise ValueError("Mismatched lengths of op_sets and allocation_info from contract.")

        results = []
        for i, op_set in enumerate(op_sets):
            # 'op_set' might be a tuple/struct with fields like:
            #    op_set.Id and op_set.Avs in Go
            # In Python, that's typically returned as a tuple (Id, Avs, ...)
            # Similarly, 'allocation_info[i]' might have (CurrentMagnitude, PendingDiff, EffectBlock).
            # Adjust indices accordingly based on your ABI or actual returned data structure.

            # Example assumption:
            #   op_set = (Id, AvsAddress)
            #   allocation_info[i] = (currentMagnitude, pendingDiff, effectBlock)
            op_set_id = op_set[0]
            avs_address = op_set[1]

            current_magnitude = allocation_info[i][0]
            pending_diff      = allocation_info[i][1]
            effect_block      = allocation_info[i][2]

            # Build a dictionary that matches the Go 'AllocationInfo' structure
            allocation_dict = {
                "OperatorSetId":    op_set_id,
                "AvsAddress":       avs_address,
                "CurrentMagnitude": current_magnitude,
                "PendingDiff":      pending_diff,
                "EffectBlock":      effect_block,
            }
            results.append(allocation_dict)

        return results

    def get_operator_shares(
        self,
        operator_addr: Address,
        strategy_addresses: List[Address]
    ) -> List[int]:
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        # The contract function name in Solidity is presumably `GetOperatorShares`. 
        # Adjust if your ABI uses a different name.
        shares_list = self.delegation_manager.functions.GetOperatorShares(
            operator_addr,
            strategy_addresses
        ).call()

        # shares_list is a list of integers in Python.
        return shares_list

    def get_operator_sets_for_operator(self, operator_addr: Address) -> List[Dict[str, Any]]:
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        # Call the contract function. 
        # (Adjust the name `GetAllocatedSets` if your ABI differs.)
        op_sets_raw = self.allocation_manager.functions.GetAllocatedSets(operator_addr).call()

        # op_sets_raw is presumably a list of "OperatorSet" structs.
        # Each item might look like (id, avsAddress, someOtherField, ...)
        # We'll parse each tuple into a dictionary for easier usage in Python.

        operator_sets = []
        for op_set in op_sets_raw:
            # Example assumption of fields: (id, avsAddress, metadata, etc.)
            # Adjust indexes/naming as needed for your ABI:
            parsed_set = {
                "Id": op_set[0],
                "AvsAddress": op_set[1],
                # Uncomment/adjust if there are more fields in the struct:
                # "SomeField": op_set[2],
                # "AnotherField": op_set[3],
            }
            operator_sets.append(parsed_set)

        return operator_sets

    def get_allocation_delay(self, operator_addr: Address) -> int:
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        # Solidity function presumably returns a tuple: (bool isSet, uint32 delay)
        is_set, delay = self.allocation_manager.functions.GetAllocationDelay(
            operator_addr
        ).call()

        if not is_set:
            raise ValueError("allocation delay not set")

        return delay

    def get_registered_sets(self, operator_addr: Address) -> List[Dict[str, Any]]:
    
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")
        
        # Call the contract function to get the registered sets.
        # The return value will depend on your ABI; typically it might be a list of tuples.
        raw_sets = self.allocation_manager.functions.GetRegisteredSets(operator_addr).call()
        
        # Convert each returned tuple to a dictionary. Adjust the field names and indices as needed.
        operator_sets = []
        for op_set in raw_sets:
            # Example: assume each op_set is a tuple (id, avs, ...)
            operator_set_dict = {
                "Id": op_set[0],
                "Avs": op_set[1],
                # Add additional fields as required.
            }
            operator_sets.append(operator_set_dict)
        
        return operator_sets

    # -------------------------------------------------------
    # avsdirectory
    # -------------------------------------------------------
    def calculate_operator_avs_registration_digestHash(
        self,
        operator_addr: Address,
        avs_addr: Address,
        salt: bytes,  # Must be 32 bytes in length
        expiry: int
    ) -> bytes:
        if self.avs_directory is None:
            raise ValueError("AVSDirectory contract not provided")

        # Call the contract function. 
        # Adjust the name if your contract's ABI differs.
        digest_hash = self.avs_directory.functions.CalculateOperatorAVSRegistrationDigestHash(
            operator_addr,
            avs_addr,
            salt,
            expiry
        ).call()

        # Typically returns 32 bytes. Might be `HexBytes` in web3.py, which is fine to treat as bytes.
        # If you prefer to return a hex string, you can do: `return digest_hash.hex()`
        return digest_hash

    # operator_set = {
    #     "Id": some_uint64,
    #     "Avs": some_address
    # }

    def is_operator_registered_with_operator_set(
        self,
        operator_addr: Address,
        operator_set: dict
    ) -> bool:
        
        # operator_set is expected to have keys: "Id" and "Avs"
        set_id = operator_set.get("Id", 0)
        avs_address = operator_set.get("Avs")

        # If Id == 0 => M2 AVS
        if set_id == 0:
            # We need the AVSDirectory contract
            if self.avs_directory is None:
                raise ValueError("AVSDirectory contract not provided")

            # Call avsDirectory.AvsOperatorStatus(avs, operator)
            # The Go code returns 'status', then checks 'status == 1'
            status = self.avs_directory.functions.AvsOperatorStatus(
                avs_address,
                operator_addr
            ).call()
            # In Go, 'status == 1' means True, otherwise False
            return status == 1

        else:
            # We need the AllocationManager contract
            if self.allocation_manager is None:
                raise ValueError("AllocationManager contract not provided")

            # Get all registered sets for this operator
            registered_sets = self.allocation_manager.functions.GetRegisteredSets(
                operator_addr
            ).call()
            
            # Each item in registered_sets is presumably a tuple or struct with (Id, Avs, ...).
            # We check if there's a match with our operator_set.
            for reg_set in registered_sets:
                # Example assumption: reg_set = (regSetId, regSetAvs, ...)
                reg_set_id = reg_set[0]
                reg_set_avs = reg_set[1]

                if reg_set_id == set_id and reg_set_avs == avs_address:
                    return True

            return False


    def get_operators_for_operator_set(
        self,
        operator_set: dict  # e.g. {"Id": ..., "Avs": ...}
    ) -> List[Address]:
        
        # If Id == 0 => legacy AVS not supported
        set_id = operator_set.get("Id", 0)
        if set_id == 0:
            raise ValueError("Legacy AVSs not supported (operatorSet.Id == 0)")

        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        # In the Go code, we do: return r.allocationManager.GetMembers(..., operatorSet)
        # The actual Solidity function signature might be:
        #   function GetMembers(OperatorSet memory opSet) returns (address[] memory)
        #
        # In web3.py, passing a struct can be tricky. You may need to pass it as a tuple
        # if your ABI expects:
        #   GetMembers((uint256,address,...))
        #
        # For example (assuming the struct is just (Id, Avs)):
        # addresses = self.allocation_manager.functions.GetMembers(
        #     (operator_set["Id"], operator_set["Avs"])
        # ).call()

        # If the contract expects separate arguments:
        #   function GetMembers(uint256 id, address avs) returns (address[] memory)
        # then do:
        # addresses = self.allocation_manager.functions.GetMembers(
        #     operator_set["Id"],
        #     operator_set["Avs"]
        # ).call()

        # Below is an example if your struct only has (Id, Avs).
        addresses = self.allocation_manager.functions.GetMembers(
            (operator_set["Id"], operator_set["Avs"])
        ).call()

        return addresses

    def get_num_operators_for_operator_set(self, operator_set: dict) -> int:
        
        set_id = operator_set.get("Id", 0)
        if set_id == 0:
            raise ValueError("Legacy AVSs not supported (operatorSet.Id == 0)")

        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        # In Go: r.allocationManager.GetMemberCount(ctx, operatorSet)
        # In Solidity, that might be a function that takes a struct or individual fields.
        # Example if the struct has (Id, Avs):
        #    self.allocation_manager.functions.GetMemberCount((set_id, operator_set["Avs"])).call()
        # If the contract expects separate args:
        #    self.allocation_manager.functions.GetMemberCount(set_id, operator_set["Avs"]).call()

        member_count = self.allocation_manager.functions.GetMemberCount(
            (operator_set["Id"], operator_set["Avs"])
        ).call()

        # The result is a big integer in Solidity/Go, which Python can handle as an int.
        return member_count


    def get_strategies_for_operator_set(self, operator_set: dict) -> List[Address]:
        
        # Check if this is a "legacy AVS" scenario
        if operator_set.get("Id", 0) == 0:
            raise ValueError("Legacy AVSs not supported (operatorSet.Id == 0)")

        # Check if we have a valid contract instance
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        # In Go: r.allocationManager.GetStrategiesInOperatorSet(ctx, operatorSet)
        # In Solidity, if the function signature is something like:
        #     function GetStrategiesInOperatorSet(OperatorSet memory opSet) view returns (address[] memory)
        # you likely pass the tuple (opSet.Id, opSet.Avs, etc.) if needed.
        strategies = self.allocation_manager.functions.GetStrategiesInOperatorSet(
            (operator_set["Id"], operator_set["Avs"])
        ).call()

        # 'strategies' is a list of addresses, which web3.py typically returns as strings like '0x...'
        return strategies

    def get_slashable_shares_for_operator_sets(
        self,
        operator_sets: List[dict]
    ) -> List[Any]:
        
        # 1. Get the current block number from your web3 client
        current_block = self.eth_http_client.eth.block_number

        # 2. Delegate to a function that calculates slashable shares for the given block number
        return self.GetSlashableSharesForOperatorSetsBefore(
            operator_sets,
            current_block
        )

    # -------------------------------------------------------
    # delegationmanager
    # -------------------------------------------------------
    def is_operator_registered(self, operator_address: str) -> bool:
        
        # Check if the contract instance is available
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        # Convert the address string to whatever format web3.py expects
        # (If it's already a proper '0x'-prefixed string, that's usually sufficient.)
        is_registered = self.delegation_manager.functions.IsOperator(
            operator_address
        ).call()

        return is_registered

    def get_staker_shares(self, staker_address: Address) -> Tuple[List[Address], List[int]]:
        
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        # Call the contract function. 
        # Adjust the name if your ABI differs (e.g. 'getDepositedShares' vs. 'GetDepositedShares').
        strategy_addrs, share_amounts = self.delegation_manager.functions.GetDepositedShares(
            staker_address
        ).call()

        # 'strategy_addrs' will be a list of addresses (e.g. ["0x1234...", "0xABCD..."])
        # 'share_amounts' will be a list of big integers, which Python can handle as int.

        return strategy_addrs, share_amounts

    def get_delegated_operator(
        self,
        staker_address: Address,
        block_number: Optional[int] = None
    ) -> Address:
        
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        # If you want to specify a block number, use call(..., block_identifier=block_number).
        # Otherwise, omit it to use the latest block.
        if block_number is not None:
            delegated_operator = self.delegation_manager.functions.DelegatedTo(
                staker_address
            ).call(block_identifier=block_number)
        else:
            delegated_operator = self.delegation_manager.functions.DelegatedTo(
                staker_address
            ).call()

        return delegated_operator

    def get_operator_details(self, operator: Dict[str, Any]) -> Dict[str, Any]:
        
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        operator_address = operator["Address"]  # e.g., "0x..."

        # 1. Read delegation approver address
        #    In Go, it's: delegationManagerAddress = r.delegationManager.DelegationApprover(..., operator.Address)
        delegation_manager_address = self.delegation_manager.functions.DelegationApprover(
            operator_address
        ).call()
        # Typically returns a hex string like '0x123...', but could be HexBytes.

        # 2. Read the allocation delay: (isSet, delay) from the contract.
        #    In Go: isSet, delay, err := r.allocationManager.GetAllocationDelay(...)
        is_set, delay = self.allocation_manager.functions.GetAllocationDelay(operator_address).call()

        # If it's not set, we default to 0
        allocation_delay = delay if is_set else 0

        # 3. Return a dictionary resembling types.Operator in Go
        return {
            "Address":                   operator_address,
            "DelegationApproverAddress": delegation_manager_address,
            "AllocationDelay":           allocation_delay,
            # Add other fields if your Operator struct has more
        }

    def get_operator_shares_in_strategy(
        self,
        operator_addr: Address,
        strategy_addr: Address
    ) -> int:
        
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        # In Go: r.delegationManager.OperatorShares(&bind.CallOpts{...}, operatorAddr, strategyAddr)
        # In Python/web3.py:
        shares = self.delegation_manager.functions.OperatorShares(
            operator_addr,
            strategy_addr
        ).call()

        # web3.py will return the integer value directly (no overflow issues).
        return shares

    def calculate_delegation_approval_digest_hash(
        self,
        staker: Address,
        operator: Address,
        delegation_approver: Address,
        approver_salt: bytes,    # must be exactly 32 bytes in length
        expiry: int              # Go uses *big.Int, Python int is fine
    ) -> bytes:
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        digest_hash = self.delegation_manager.functions.CalculateDelegationApprovalDigestHash(
            staker,
            operator,
            delegation_approver,
            approver_salt,
            expiry
        ).call()

        return digest_hash

    def get_operator_shares(
        self,
        operator_address: Address,
        strategy_addresses: List[Address]
    ) -> List[int]:
        
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        # In Go: r.delegationManager.GetOperatorShares(&bind.CallOpts{...}, operatorAddress, strategyAddresses)
        # In Python/web3.py:
        shares_list = self.delegation_manager.functions.GetOperatorShares(
            operator_address,
            strategy_addresses
        ).call()

        # shares_list is typically a list of big integers from Solidity (uint256),
        # but Python automatically converts them to int.
        return shares_list

    def get_operators_shares(
        self,
        operator_addresses: List[Address],
        strategy_addresses: List[Address]
    ) -> List[List[int]]:
        
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        # In Go: r.delegationManager.GetOperatorsShares(&bind.CallOpts{Context: ctx}, operatorAddresses, strategyAddresses)
        # In Python/web3.py:
        shares_2d = self.delegation_manager.functions.GetOperatorsShares(
            operator_addresses,
            strategy_addresses
        ).call()

        # shares_2d should be a list of lists (2D array), each element is a "big integer" in Solidity
        # which Python automatically treats as int.
        return shares_2d

    def get_delegation_approver_salt_is_spent(
        self,
        delegation_approver: Address,
        approver_salt: bytes
    ) -> bool:
        
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        # The Go code calls r.delegationManager.DelegationApproverSaltIsSpent(...)
        salt_is_spent = self.delegation_manager.functions.DelegationApproverSaltIsSpent(
            delegation_approver,
            approver_salt
        ).call()

        return salt_is_spent

    def get_pending_withdrawal_status(
        self,
        withdrawal_root: bytes
    ) -> bool:
        
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        # Calls 'PendingWithdrawals(withdrawal_root)' on the DelegationManager contract
        status = self.delegation_manager.functions.PendingWithdrawals(
            withdrawal_root
        ).call()

        return status

    def get_cumulative_withdrawals_queued(
        self,
        staker: Address
    ) -> int:
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        # In Go, this calls: r.delegationManager.CumulativeWithdrawalsQueued(...)
        queued_amount = self.delegation_manager.functions.CumulativeWithdrawalsQueued(
            staker
        ).call()

        # This is typically returned as a big integer by Solidity,
        # but Python automatically converts it to a standard int.
        return queued_amount

    # -------------------------------------------------------
    # ethclient
    # -------------------------------------------------------
    def get_slashable_shares_for_operator_sets(
        self,
        operator_sets: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        
        # Step 1: Retrieve current block number from the Ethereum client
        current_block = self.eth_http_client.eth.block_number

        # Step 2: Delegate to a helper method for slashable shares "before" a certain block
        # We'll assume you define this method similarly to how the Go code calls
        # GetSlashableSharesForOperatorSetsBefore(ctx, operatorSets, blockNumber)
        return self.GetSlashableSharesForOperatorSetsBefore(operator_sets, current_block)



    # -------------------------------------------------------
    # permissioncontrol
    # -------------------------------------------------------
    def can_call(
        self,
        account_address: Address,
        appointee_address: Address,
        target: Address,
        selector: bytes
    ) -> bool:
        if self.permissioncontrol is None:
            raise ValueError("PermissionController contract not provided")

        try:
            can_call = self.permissioncontrol.functions.CanCall(
                account_address,
                appointee_address,
                target,
                selector
            ).call()
        except Exception as e:
            # In Go code, it wraps the error with "utils.WrapError(...)".
            # In Python, we can raise a new exception or re-raise with context.
            raise ValueError(f"call to permission controller failed: {e}") from e

        return can_call

    def list_appointees(
        self,
        account_address: Address,
        target: Address,
        selector: bytes
    ) -> List[Address]:
        if self.permissioncontrol is None:
            raise ValueError("PermissionController contract not provided")

        try:
            appointees = self.permissioncontrol.functions.GetAppointees(
                account_address,
                target,
                selector
            ).call()
        except Exception as e:
            raise ValueError(f"Call to permission controller failed: {e}") from e

        return appointees

    def list_appointee_permissions(
        self,
        account_address: Address,
        appointee_address: Address
    ) -> Tuple[List[Address], List[bytes]]:
        
        if self.permissioncontrol is None:
            raise ValueError("PermissionController contract not provided")

        try:
            # The contract function presumably returns (targets, selectors),
            # where targets is address[], selectors is bytes4[] in Solidity.
            targets, selectors = self.permissioncontrol.functions.GetAppointeePermissions(
                account_address,
                appointee_address
            ).call()
        except Exception as e:
            raise ValueError(f"Call to permission controller failed: {e}") from e

        # 'targets' should be a list of addresses (e.g. ["0x...", "0x..."]).
        # 'selectors' should be a list of 4-byte values, which web3.py typically provides as bytes (e.g., b"\x12\x34\x56\x78").
        return targets, selectors

    def list_pending_admins(
        self,
        account_address: Address
    ) -> List[Address]:
        
        if self.permissioncontrol is None:
            raise ValueError("PermissionController contract not provided")

        try:
            pending_admins = self.permissioncontrol.functions.GetPendingAdmins(
                account_address
            ).call()
        except Exception as e:
            raise ValueError(f"Call to permission controller failed: {e}") from e

        # 'pending_admins' should be a list of addresses, e.g. ["0x...", "0x..."].
        return pending_admins


    def list_admins(
        self,
        account_address: Address
    ) -> List[Address]:
        
        if self.permissioncontrol is None:
            raise ValueError("PermissionController contract not provided")

        try:
            admins = self.permissioncontrol.functions.GetAdmins(account_address).call()
        except Exception as e:
            raise ValueError(f"Call to permission controller failed: {e}") from e

        return admins

    def is_pending_admin(
        self,
        account_address: Address,
        pending_admin_address: Address
    ) -> bool:
        if self.permissioncontrol is None:
            raise ValueError("PermissionController contract not provided")

        try:
            is_pending_admin = self.permissioncontrol.functions.IsPendingAdmin(
                account_address,
                pending_admin_address
            ).call()
        except Exception as e:
            raise ValueError(f"Call to permission controller failed: {e}") from e

        return is_pending_admin

    def is_admin(
        self,
        account_address: Address,
        admin_address: Address
    ) -> bool:
        if self.permissioncontrol is None:
            raise ValueError("PermissionController contract not provided")

        try:
            is_admin = self.permissioncontrol.functions.IsAdmin(
                account_address,
                admin_address
            ).call()
        except Exception as e:
            raise ValueError(f"Call to permission controller failed: {e}") from e

        return is_admin

    # -------------------------------------------------------
    # rewardcordinator
    # -------------------------------------------------------
    def get_distribution_roots_length(self) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        length = self.reward_cordinator.functions.GetDistributionRootsLength().call()
        return length

    def curr_rewards_calculation_end_timestamp(self) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        # In Go: r.rewardsCoordinator.CurrRewardsCalculationEndTimestamp(...)
        # In Python (web3.py):
        end_timestamp = self.reward_cordinator.functions.CurrRewardsCalculationEndTimestamp().call()
        return end_timestamp

    def get_current_claimable_distribution_root(self) -> Dict[str, Any]:
        
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        # Call the contract function. Suppose it returns a struct with fields like (root, startBlock, endBlock, ...).
        # We'll get a tuple in Python, e.g., (root, startBlock, endBlock, totalClaimable, ...)
        raw_data = self.reward_cordinator.functions.GetCurrentClaimableDistributionRoot().call()

        # Example: if your struct is defined in Solidity as something like:
        #
        #   struct DistributionRoot {
        #       bytes32 root;
        #       uint256 startBlock;
        #       uint256 endBlock;
        #       uint256 totalClaimable;
        #       ...
        #   }
        #
        # Then web3.py might return a tuple of:
        #   (root, startBlock, endBlock, totalClaimable, ...)
        #
        # We'll convert this tuple into a dictionary for easier usage:
        distribution_root = {
            "root": raw_data[0],
            "startBlock": raw_data[1],
            "endBlock": raw_data[2],
            "totalClaimable": raw_data[3],
            # Add any additional fields if the struct has more.
        }

        return distribution_root

    def get_root_index_from_hash(
        self,
        root_hash: bytes
    ) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        # Call the contract function
        root_index = self.reward_cordinator.functions.GetRootIndexFromHash(root_hash).call()

        # The Go code returns a uint32; in Python we handle it simply as int.
        return root_index

    def get_cumulative_claimed(
        self,
        earner: Address,
        token: Address
    ) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        claimed_amount = self.reward_cordinator.functions.CumulativeClaimed(
            earner,
            token
        ).call()

        return claimed_amount

    def check_claim(self, claim: Dict[str, Any]) -> bool:
        
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        # Format the claim in a way web3.py expects for a struct.
        # The exact tuple/array order must match the Solidity struct definition.
        # Example if your Solidity struct is:
        #   struct RewardsMerkleClaim {
        #       bytes32 root;
        #       uint256 index;
        #       address account;
        #       uint256 amount;
        #       bytes32[] merkleProof;
        #   }
        # Then you might pass it as a tuple in Python like this:
        claim_tuple = (
            claim["root"],         # bytes32
            claim["index"],        # uint256
            claim["account"],      # address
            claim["amount"],       # uint256
            claim["merkleProof"],  # bytes32[]
        )

        try:
            # In Go: r.rewardsCoordinator.CheckClaim(&bind.CallOpts{Context: ctx}, claim)
            # In Python/web3.py, we call the same function with the struct tuple
            is_valid = self.reward_cordinator.functions.CheckClaim(claim_tuple).call()
        except Exception:
            # If the contract call reverts or fails, treat it as an invalid claim
            return False

        return is_valid

    def get_operator_avs_split(
        self,
        operator: Address,
        avs: Address
    ) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        # Call the contract function (uint16 in Solidity, Python will treat it as int)
        avs_split = self.reward_cordinator.functions.GetOperatorAVSSplit(operator, avs).call()

        return avs_split


    def get_operator_pi_split(self, operator: Address) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        pi_split = self.reward_cordinator.functions.GetOperatorPISplit(operator).call()
        return pi_split


    def get_operator_set_split(self, operator: Address, operator_set: dict) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        # Convert the operator_set dictionary to a tuple that matches the Solidity struct.
        # Adjust the fields and order according to your contract's definition.
        operator_set_tuple = (operator_set["Id"], operator_set["Avs"])
        
        op_set_split = self.reward_cordinator.functions.GetOperatorSetSplit(
            operator,
            operator_set_tuple
        ).call()

        return op_set_split

    def get_calculation_interval_seconds(self) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        interval = self.reward_cordinator.functions.CALCULATIONINTERVALSECONDS().call()
        return interval

    def get_max_rewards_duration(self) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        max_rewards_duration = self.reward_cordinator.functions.MAXREWARDSDURATION().call()
        return max_rewards_duration

    def get_max_retroactive_length(self) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        max_retroactive_length = self.reward_cordinator.functions.MAXRETROACTIVELENGTH().call()
        return max_retroactive_length

    def get_max_future_length(self) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        max_future_length = self.reward_cordinator.functions.MAXFUTURELENGTH().call()
        return max_future_length

    def get_genesis_rewards_timestamp(self) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        genesis_timestamp = self.reward_cordinator.functions.GENESISREWARDSTIMESTAMP().call()
        return genesis_timestamp

    def get_rewards_updater(self) -> Address:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        rewards_updater = self.reward_cordinator.functions.RewardsUpdater().call()
        return rewards_updater

    def GetActivationDelay(self) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        activation_delay = self.reward_cordinator.functions.ActivationDelay().call()
        return activation_delay

    def get_curr_rewards_calculation_end_timestamp(self) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        end_timestamp = self.reward_cordinator.functions.CurrRewardsCalculationEndTimestamp().call()
        return end_timestamp

    def get_default_operator_split_bips(self) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        default_split_bips = self.reward_cordinator.functions.DefaultOperatorSplitBips().call()
        return default_split_bips

    def get_claimer_for(self, earner: Address) -> Address:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        claimer_address = self.reward_cordinator.functions.ClaimerFor(earner).call()
        return claimer_address

    def get_submission_nonce(self, avs: Address) -> int:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        submission_nonce = self.reward_cordinator.functions.SubmissionNonce(avs).call()
        return submission_nonce

    def get_is_avs_rewards_submission_hash(self, avs: Address, hash: bytes) -> bool:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        is_valid = self.reward_cordinator.functions.IsAVSRewardsSubmissionHash(
            avs,
            hash
        ).call()

        return is_valid

    def get_is_rewards_submission_for_all_hash(self, avs: Address, hash: bytes) -> bool:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        is_valid = self.reward_cordinator.functions.IsRewardsSubmissionForAllHash(
            avs,
            hash
        ).call()
        return is_valid

    def get_is_rewards_for_all_submitter(self, submitter: Address) -> bool:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        is_authorized = self.reward_cordinator.functions.IsRewardsForAllSubmitter(submitter).call()
        return is_authorized

    def get_is_rewards_submission_for_all_earners_hash(self, avs: Address, hash: bytes) -> bool:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        is_valid = self.reward_cordinator.functions.IsRewardsSubmissionForAllEarnersHash(
            avs,
            hash
        ).call()
        
        return is_valid


    def get_is_operator_directed_avs_rewards_submission_hash(self, avs: Address, hash: bytes) -> bool:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        is_valid = self.reward_cordinator.functions.IsOperatorDirectedAVSRewardsSubmissionHash(
            avs,
            hash
        ).call()
        
        return is_valid

    def get_is_operator_directed_operator_set_rewards_submission_hash(self, avs: Address, hash: bytes) -> bool:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        is_valid = self.reward_cordinator.functions.IsOperatorDirectedOperatorSetRewardsSubmissionHash(
            avs,
            hash
        ).call()
        
        return is_valid

    # -------------------------------------------------------
    # strategy
    # -------------------------------------------------------
    def get_strategy_and_underlying_erc20_token(self, strategy_addr: Address) -> Tuple[Any, Any, Address]:
        # Create the strategy contract instance
        try:
            contract_strategy = strategy.NewContractIStrategy(strategy_addr, self.eth_http_client)
        except Exception as e:
            raise ValueError(f"Failed to fetch strategy contract: {e}")
        
        # Retrieve the underlying token address from the strategy contract
        try:
            underlying_token_addr = contract_strategy.functions.UnderlyingToken().call()
        except Exception as e:
            raise ValueError(f"Failed to fetch token contract: {e}")
        
        # Create the ERC20 contract instance for the underlying token
        try:
            contract_underlying_token = erc20.NewContractIERC20(underlying_token_addr, self.eth_http_client)
        except Exception as e:
            raise ValueError(f"Failed to fetch token contract: {e}")
        
        return contract_strategy, contract_underlying_token, underlying_token_addr
