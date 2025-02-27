import logging
from typing import Tuple, List, Any, Dict

from eth_typing import Address
from web3 import Web3
from web3.contract.contract import Contract

from eigensdk._types import Operator
from eigensdk.contracts import ABIs
from txmanager import TxManager
from eth_abi import encode


class ELWriter:
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
        tx_mgr: TxManager,
        # strategy_abi: List[Dict[str, Any]],
        # erc20_abi: List[Dict[str, Any]],
    ):
        self.allocation_manager: Contract = allocation_manager
        self.avs_directory: Contract = avs_directory
        self.delegation_manager: Contract = delegation_manager
        self.permissioncontrol: Contract = permissioncontrol
        self.reward_cordinator: Contract = reward_cordinator
        self.strategy_manager: Contract = strategy_manager
        self.eth_http_client: Web3 = eth_http_client
        self.logger: logging.Logger = logger
        self.tx_mgr: TxManager = tx_mgr
        # self.strategy_abi = strategy_abi
        # self.erc20_abi = erc20_abi

    # AllocationManager

    def modify_allocations(
        self,
        operator_address: Address,
        operator_sets: List[Tuple[Address, int, List[Address], List[int]]],
        wait_for_receipt: bool,
    ) -> Any:

        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        try:
            # ✅ Ensure all addresses are properly formatted
            if not operator_address or not Web3.is_address(operator_address):
                raise ValueError(f"Invalid operator address: {operator_address}")

            operator_address = Web3.to_checksum_address(operator_address)

            formatted_operator_sets = []
            for avs, op_id, strategies, magnitudes in operator_sets:
                if not avs or not Web3.is_address(avs):
                    raise ValueError(f"Invalid AVS address: {avs}")

                formatted_operator_sets.append(
                    (
                        (Web3.to_checksum_address(avs), int(op_id)),
                        [
                            Web3.to_checksum_address(strategy)
                            for strategy in strategies
                            if Web3.is_address(strategy)
                        ],
                        [int(mag) for mag in magnitudes],
                    )
                )

            print(f"✅ Formatted Operator Address: {operator_address}")
            print(f"✅ Formatted Operator Sets: {formatted_operator_sets}")

            # ✅ Fetch transaction options from TxManager
            no_send_tx_opts = self.tx_mgr.get_no_send_tx_opts()

        except Exception as e:
            raise ValueError(
                f"Failed to prepare inputs for ModifyAllocations: {e}"
            ) from e

        try:
            # ✅ Call contract function correctly
            tx_hash = self.allocation_manager.functions.modifyAllocations(
                operator_address, formatted_operator_sets
            ).transact(no_send_tx_opts)

            # ✅ Retrieve the transaction receipt
            tx_receipt = self.eth_http_client.eth.wait_for_transaction_receipt(tx_hash)

        except Exception as e:
            raise ValueError(f"Failed to create ModifyAllocations tx: {e}") from e

        try:
            # ✅ Send the transaction
            receipt = self.tx_mgr.send(tx_receipt, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"Failed to send tx: {e}") from e

        return receipt

    def clear_deallocation_queue(
        self,
        operator_address: Address,
        strategies: List[Address],
        nums_to_clear: List[int],
        wait_for_receipt: bool,
    ) -> Any:

        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        try:
            # Retrieve transaction options without sending the transaction.
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Create the transaction to clear the deallocation queue.
            tx_hash = self.allocation_manager.functions.clearDeallocationQueue(
                operator_address, strategies, nums_to_clear
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create ClearDeallocationQueue tx: {e}") from e

        try:
            # ✅ FIX: Ensure the correct transaction format is passed to `Send`
            tx_receipt = (
                self.eth_http_client.eth.wait_for_transaction_receipt(tx_hash)
                if wait_for_receipt
                else tx_hash
            )
        except Exception as e:
            raise ValueError(f"failed to get transaction receipt: {e}") from e

        return tx_receipt

    def set_allocation_delay(
        self, operator_address: Address, delay: int, wait_for_receipt: bool
    ) -> Any:

        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Create the transaction and get the tx hash
            tx_hash = self.allocation_manager.functions.setAllocationDelay(
                operator_address, delay
            ).transact(no_send_tx_opts)

            # Wait for receipt if requested
            if wait_for_receipt:
                receipt = self.eth_http_client.eth.wait_for_transaction_receipt(tx_hash)
            else:
                receipt = {"transactionHash": tx_hash}

        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def deregister_from_operator_sets(
        self, operator: Address, request: Dict[str, Any]
    ) -> Any:

        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Ensure operatorSetIds are converted to a list of uint32 integers
            operator_set_ids = [int(x) for x in request["OperatorSetIds"]]

            # Prepare struct-like tuple as per Solidity ABI
            deregistration_params = (request["AVSAddress"], operator_set_ids)

            # Call the contract function with correctly formatted parameters
            tx_hash = self.allocation_manager.functions.deregisterFromOperatorSets(
                deregistration_params  # 👈 Pass as a tuple
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(
                f"failed to create DeregisterFromOperatorSets tx: {e}"
            ) from e

        try:
            # Wait for transaction receipt instead of passing hash directly
            receipt = self.eth_http_client.eth.wait_for_transaction_receipt(tx_hash)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def getPubkeyRegistrationParams(
        eth_client, registry_coordinator_addr, operator_address, bls_key_pair
    ):
        """Fetch public key registration parameters from the blockchain."""

        registry_contract = eth_client.eth.contract(
            address=registry_coordinator_addr,
            abi=[  # Define the ABI for the function call
                {
                    "constant": True,
                    "inputs": [
                        {"name": "operator", "type": "address"},
                        {"name": "blsKeyPair", "type": "bytes32"},
                    ],
                    "name": "getPubkeyRegistrationParams",
                    "outputs": [{"name": "params", "type": "bytes"}],
                    "stateMutability": "view",
                    "type": "function",
                }
            ],
        )

        try:
            params = registry_contract.functions.getPubkeyRegistrationParams(
                operator_address, bls_key_pair
            ).call()
            return params
        except Exception as e:
            raise ValueError(f"Failed to fetch public key registration params: {e}")

    def AbiEncodeRegistrationParams(registration_type, socket, pubkey_reg_params):
        """ABI encode registration parameters."""

        encoded_params = encode(
            ["uint256", "string", "bytes"],
            [registration_type, socket, pubkey_reg_params],
        )

        return encoded_params

    def register_for_operator_sets(
        self, registry_coordinator_addr: Address, request: Dict[str, any]
    ) -> Any:

        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            pubkey_reg_params = getPubkeyRegistrationParams(
                self.eth_client,
                registry_coordinator_addr,
                request["OperatorAddress"],
                request["BlsKeyPair"],
            )
        except Exception as e:
            raise ValueError(
                f"failed to get public key registration params: {e}"
            ) from e

        try:
            data = AbiEncodeRegistrationParams(
                RegistrationTypeNormal, request["Socket"], pubkey_reg_params
            )
        except Exception as e:
            raise ValueError(f"failed to encode registration params: {e}") from e

        try:
            register_params = {
                "Avs": request["AVSAddress"],
                "OperatorSetIds": request["OperatorSetIds"],
                "Data": data,
            }
            tx = self.allocation_manager.functions.registerForOperatorSets(
                request["OperatorAddress"], register_params
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create RegisterForOperatorSets tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(tx, request["WaitForReceipt"])
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    # delegationmanager

    def update_operator_details(
        self, operator: Dict[str, Any], wait_for_receipt: bool
    ) -> Any:

        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        # Log that we're updating operator details
        self.logger.info(
            f"updating operator details of operator {operator['Address']} to EigenLayer"
        )

        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Create the transaction by calling ModifyOperatorDetails on the contract.
            # Here, we assume that the contract function accepts the operator address and the delegation approver address.
            tx = self.delegation_manager.functions.modifyOperatorDetails(
                operator["Address"], operator["DelegationApproverAddress"]
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create ModifyOperatorDetails tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        self.logger.info(
            f"successfully updated operator details, txHash: {receipt.txHash}, operator: {operator['Address']}"
        )

        return receipt

    def update_meta_data_uri(
        self, operator_address: Address, uri: str, wait_for_receipt: bool
    ) -> Any:

        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Create the transaction by calling the contract function.
            tx = self.delegation_manager.functions.updateOperatorMetadataURI(
                operator_address, uri
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(
                f"failed to create UpdateOperatorMetadataURI tx: {e}"
            ) from e

        try:
            receipt = self.tx_mgr.Send(tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        self.logger.info(
            f"successfully updated operator metadata uri, txHash: {receipt.txHash}"
        )

        return receipt

    def register_as_operator(
        self, operator: Dict[str, any], wait_for_receipt: bool
    ) -> Any:

        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        self.logger.info(f"registering operator {operator['Address']} to EigenLayer")

        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            tx = self.delegation_manager.functions.registerAsOperator(
                operator["DelegationApproverAddress"],
                operator["AllocationDelay"],
                operator["MetadataUrl"],
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create RegisterAsOperator tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        self.logger.info(f"tx successfully included, txHash: {receipt.txHash}")
        return receipt

    # permisssioncontrol

    def remove_permission(self, request: Dict[str, any]) -> Any:

        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no-send tx opts: {e}") from e

        try:
            tx = self.NewRemovePermissionTx(tx_opts, request)
        except Exception as e:
            raise ValueError(f"failed to create NewRemovePermissionTx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(tx, request["WaitForReceipt"])
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def new_remove_permission_tx(
        self, tx_opts: Dict[str, any], request: Dict[str, any]
    ) -> Any:
        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")

        try:
            tx = self.permissioncontrol.functions.removeAppointee(
                request["AccountAddress"],
                request["AppointeeAddress"],
                request["Target"],
                request["Selector"],
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create RemovePermission tx: {e}") from e

        return tx

    def new_set_permission_tx(
        self, tx_opts: Dict[str, any], request: Dict[str, any]
    ) -> Any:

        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")

        try:
            tx = self.permissioncontrol.functions.setAppointee(
                request["AccountAddress"],
                request["AppointeeAddress"],
                request["Target"],
                request["Selector"],
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create SetPermission tx: {e}") from e

        return tx

    def set_permission(self, request: Dict[str, any]) -> Any:
        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no-send tx opts: {e}") from e

        try:
            tx = self.NewSetPermissionTx(tx_opts, request)
        except Exception as e:
            raise ValueError(f"failed to create NewSetPermissionTx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(tx, request["WaitForReceipt"])
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def new_accept_admin_tx(
        self, tx_opts: Dict[str, any], request: Dict[str, any]
    ) -> Any:
        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")

        try:
            tx = self.permissioncontrol.functions.acceptAdmin(
                request["AccountAddress"]
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create AcceptAdmin tx: {e}") from e

        return tx

    def accept_admin(self, request: Dict[str, any]) -> Any:
        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            tx = self.NewAcceptAdminTx(tx_opts, request)
        except Exception as e:
            raise ValueError(f"failed to create AcceptAdmin transaction: {e}") from e

        try:
            receipt = self.tx_mgr.Send(tx, request["WaitForReceipt"])
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def new_add_pending_admin_tx(
        self, tx_opts: Dict[str, any], request: Dict[str, any]
    ) -> Any:
        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")

        try:
            tx = self.permissioncontrol.functions.addPendingAdmin(
                request["AccountAddress"], request["AdminAddress"]
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create AddPendingAdmin tx: {e}") from e

        return tx

    def new_remove_admin_tx(
        self, tx_opts: Dict[str, any], request: Dict[str, any]
    ) -> Any:
        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")

        try:
            tx = self.permissioncontrol.functions.removeAdmin(
                request["AccountAddress"], request["AdminAddress"]
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create RemoveAdmin tx: {e}") from e

        return tx

    def new_remove_pending_admin_tx(
        self, tx_opts: Dict[str, any], request: Dict[str, any]
    ) -> Any:
        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")

        try:
            tx = self.permissioncontrol.functions.RemovePendingAdmin(
                request["AccountAddress"], request["AdminAddress"]
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create RemovePendingAdmin tx: {e}") from e

        return tx

    def remove_pending_admin(self, request: Dict[str, any]) -> Any:
        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            tx = self.NewRemovePendingAdminTx(tx_opts, request)
        except Exception as e:
            raise ValueError(
                f"failed to create RemovePendingAdmin transaction: {e}"
            ) from e

        try:
            receipt = self.tx_mgr.Send(tx, request["WaitForReceipt"])
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    # rewardcordinator

    def set_claimer_for(self, claimer: Address, wait_for_receipt: bool) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no-send tx opts: {e}") from e

        try:
            # Create transaction but do not send yet
            tx = self.reward_cordinator.functions.setClaimerFor(
                claimer
            ).build_transaction(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create SetClaimerFor tx: {e}") from e

        try:
            # Send transaction with a correctly formatted transaction dictionary
            receipt = self.tx_mgr.Send(tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def process_claim(
        self, claim: Any, recipient_address: Address, wait_for_receipt: bool
    ) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Pass claim as a list because the contract expects an array
            tx = self.reward_cordinator.functions.processClaims(
                [claim], recipient_address
            ).build_transaction(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create ProcessClaim tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def set_operator_avs_split(
        self, operator: Address, avs: Address, split: int, wait_for_receipt: bool
    ) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
            tx_opts.update(
                {
                    "from": self.eth_http_client.eth.default_account,
                    "nonce": self.eth_http_client.eth.get_transaction_count(
                        self.eth_http_client.eth.default_account
                    ),
                    "gas": 200000,  # Ensure you set a reasonable gas limit
                    "gasPrice": self.eth_http_client.eth.gas_price,
                }
            )
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            tx = self.reward_cordinator.functions.setOperatorAVSSplit(
                operator, avs, split
            ).build_transaction(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create SetOperatorAVSSplit tx: {e}") from e

        try:
            signed_tx = self.eth_http_client.eth.account.sign_transaction(
                tx, self.tx_mgr.private_key
            )  # Ensure private key is available
            tx_hash = self.eth_http_client.eth.send_raw_transaction(
                signed_tx.rawTransaction
            )

            if wait_for_receipt:
                receipt = self.eth_http_client.eth.wait_for_transaction_receipt(tx_hash)
            else:
                receipt = tx_hash.hex()
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def set_operator_pi_split(
        self, operator: Address, split: int, wait_for_receipt: bool
    ) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Call the contract function SetOperatorPISplit.
            tx = self.reward_cordinator.functions.setOperatorPISplit(
                operator, split
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create SetOperatorPISplit tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def set_operator_set_split(
        self,
        operator: Address,
        operator_set: Dict[str, any],
        split: int,
        wait_for_receipt: bool,
    ) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # The operator_set parameter is expected to match the structure required by your contract's ABI.
            tx = self.reward_cordinator.functions.setOperatorSetSplit(
                operator, operator_set, split
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create SetOperatorSetSplit tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def process_claims(
        self, claims: List[Any], recipient_address: Address, wait_for_receipt: bool
    ) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        if not claims:
            raise ValueError("claims is empty, at least one claim must be provided")

        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            tx = self.reward_cordinator.functions.processClaims(
                claims, recipient_address
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create ProcessClaims tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    # strategy

    def deposit_erc20_into_strategy(
        self, strategy_addr: Address, amount: int, wait_for_receipt: bool
    ) -> Any:
        # Check if the strategy manager contract is available.
        if self.strategy_manager is None:
            raise ValueError("StrategyManager contract not provided")

        self.logger.info(f"depositing {amount} tokens into strategy {strategy_addr}")

        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no-send tx opts: {e}") from e

        try:
            # Retrieve underlying token contract and address from the chain reader.
            # We assume GetStrategyAndUnderlyingERC20Token returns a tuple like:
            # (strategy_contract, underlying_token_contract, underlying_token_addr)
            _, underlying_token_contract, underlying_token_addr = (
                self.elChainReader.GetStrategyAndUnderlyingERC20Token(strategy_addr)
            )
        except Exception as e:
            raise ValueError(
                f"failed to get strategy and underlying ERC20 token: {e}"
            ) from e

        # Approve the strategy manager to spend the tokens.
        try:
            tx = underlying_token_contract.functions.Approve(
                self.strategy_manager_addr, amount
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create approve token transfer tx: {e}") from e

        try:
            # Send the approval transaction.
            _ = self.tx_mgr.Send(tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send approval tx: {e}") from e

        # Deposit tokens into the strategy.
        try:
            tx = self.strategy_manager.functions.depositIntoStrategyWithSignature(
                strategy_addr, underlying_token_addr, amount
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create DepositIntoStrategy tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send deposit tx: {e}") from e

        self.logger.info(f"deposited {amount} into strategy {strategy_addr}")
        return receipt
