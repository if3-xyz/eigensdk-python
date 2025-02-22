import logging
from typing import Tuple, List, Any , Dict

from eth_typing import Address
from web3 import Web3
from web3.contract.contract import Contract

from eigensdk._types import Operator
from eigensdk.contracts import ABIs


class ELWriter:
    def __init__(
        self,
        allocation_manager:Contract,
        avs_directory: Contract,
        delegation_manager: Contract,
        permissioncontrol:Contract,
        reward_cordinator: Contract,
        strategy_manager: Contract,
        logger: logging.Logger,
        eth_http_client: Web3,
    ):
        self.allocation_manager: Contract = allocation_manager
        self.avs_directory: Contract = avs_directory
        self.delegation_manager: Contract = delegation_manager
        self.permissioncontrol: Contract = permissioncontrol
        self.reward_cordinator: Contract = reward_cordinator
        self.strategy_manager: Contract = strategy_manager
        self.eth_http_client: Web3 = eth_http_client
        self.logger: logging.Logger = logger

    
    
    #AllocationManager

    def modify_allocations(
        self,
        operator_address: Address,
        allocations: List[Dict[str, Any]],
        wait_for_receipt: bool
    ) -> Any:
        
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        try:
            # Obtain transaction options (e.g., gas, nonce, etc.) without sending the transaction.
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Create and sign the transaction to modify allocations.
            # Adjust the method call to match your contract's ABI.
            tx = self.allocation_manager.functions.ModifyAllocations(
                operator_address,
                allocations
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create ModifyAllocations tx: {e}") from e

        try:
            # Send the transaction using your tx manager.
            # Depending on your implementation, you may not need a context parameter.
            receipt = self.tx_mgr.Send(tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt
    
    def clear_deallocation_queue(
        self,
        ctx: Any,
        operator_address: Address,
        strategies: List[Address],
        nums_to_clear: List[int],
        wait_for_receipt: bool
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
            # The contract function is assumed to be called 'ClearDeallocationQueue'
            # and expects operator_address, strategies, and nums_to_clear.
            tx = self.allocation_manager.functions.ClearDeallocationQueue(
                operator_address,
                strategies,
                nums_to_clear
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create ClearDeallocationQueue tx: {e}") from e

        try:
            # Send the transaction using the transaction manager.
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def set_allocation_delay(
        self,
        ctx: Any,
        operator_address: Address,
        delay: int,
        wait_for_receipt: bool
    ) -> Any:
        
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Create the transaction. Adjust the function name and parameters to match your contract's ABI.
            tx = self.allocation_manager.functions.SetAllocationDelay(operator_address, delay).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create InitializeAllocationDelay tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def deregister_from_operator_sets(
        self,
        ctx: Any,
        operator: Address,
        request: Dict[str, Any]
    ) -> Any:
        
        if self.allocation_manager is None:
            raise ValueError("AllocationManager contract not provided")

        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Depending on your contract ABI, you may pass the parameters individually.
            # Here we assume the contract function expects:
            #   operator, avs, operatorSetIds
            tx = self.allocation_manager.functions.DeregisterFromOperatorSets(
                operator,
                request["AVSAddress"],
                request["OperatorSetIds"]
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create DeregisterFromOperatorSets tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, request["WaitForReceipt"])
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def register_for_operator_sets(
        self,
        ctx: Any,
        registry_coordinator_addr: Address,
        request: Dict[str, any]
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
                request["BlsKeyPair"]
            )
        except Exception as e:
            raise ValueError(f"failed to get public key registration params: {e}") from e

        try:
            data = AbiEncodeRegistrationParams(RegistrationTypeNormal, request["Socket"], pubkey_reg_params)
        except Exception as e:
            raise ValueError(f"failed to encode registration params: {e}") from e

        try:
            register_params = {
                "Avs": request["AVSAddress"],
                "OperatorSetIds": request["OperatorSetIds"],
                "Data": data
            }
            tx = self.allocation_manager.functions.RegisterForOperatorSets(
                request["OperatorAddress"],
                register_params
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create RegisterForOperatorSets tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, request["WaitForReceipt"])
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt 

    #delegationmanager
    
    def update_operator_details(self, ctx: Any, operator: Dict[str, Any], wait_for_receipt: bool) -> Any:
        
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")
        
        # Log that we're updating operator details
        self.logger.info(f"updating operator details of operator {operator['Address']} to EigenLayer")
        
        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Create the transaction by calling ModifyOperatorDetails on the contract.
            # Here, we assume that the contract function accepts the operator address and the delegation approver address.
            tx = self.delegation_manager.functions.ModifyOperatorDetails(
                operator["Address"],
                operator["DelegationApproverAddress"]
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create ModifyOperatorDetails tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        self.logger.info(
            f"successfully updated operator details, txHash: {receipt.txHash}, operator: {operator['Address']}"
        )

        return receipt

    def update_meta_data_uri(self, ctx: Any, operator_address: Address, uri: str, wait_for_receipt: bool) -> Any:
        
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")

        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Create the transaction by calling the contract function.
            tx = self.delegation_manager.functions.UpdateOperatorMetadataURI(operator_address, uri).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create UpdateOperatorMetadataURI tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        self.logger.info(f"successfully updated operator metadata uri, txHash: {receipt.txHash}")

        return receipt
    
    def register_as_operator(self, ctx: Any, operator: Dict[str, any], wait_for_receipt: bool) -> Any:
        
        if self.delegation_manager is None:
            raise ValueError("DelegationManager contract not provided")
        
        self.logger.info(f"registering operator {operator['Address']} to EigenLayer")
        
        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            tx = self.delegation_manager.functions.RegisterAsOperator(
                operator["DelegationApproverAddress"],
                operator["AllocationDelay"],
                operator["MetadataUrl"]
            ).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create RegisterAsOperator tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        self.logger.info(f"tx successfully included, txHash: {receipt.txHash}")
        return receipt

    
    #permisssioncontrol
    
    def remove_permission(self, ctx: Any, request: Dict[str, any]) -> Any:
        
        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no-send tx opts: {e}") from e

        try:
            tx = self.NewRemovePermissionTx(tx_opts, request)
        except Exception as e:
            raise ValueError(f"failed to create NewRemovePermissionTx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, request["WaitForReceipt"])
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt


    def new_remove_permission_tx(self, tx_opts: Dict[str, any], request: Dict[str, any]) -> Any:
        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")
        
        try:
            tx = self.permissioncontrol.functions.RemoveAppointee(
                request["AccountAddress"],
                request["AppointeeAddress"],
                request["Target"],
                request["Selector"]
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create RemovePermission tx: {e}") from e

        return tx
    
    
    def new_set_permission_tx(self, tx_opts: Dict[str, any], request: Dict[str, any]) -> Any:
        
        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")
        
        try:
            tx = self.permissioncontrol.functions.SetAppointee(
                request["AccountAddress"],
                request["AppointeeAddress"],
                request["Target"],
                request["Selector"]
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create SetPermission tx: {e}") from e

        return tx


    def set_permission(self, ctx: Any, request: Dict[str, any]) -> Any:
        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no-send tx opts: {e}") from e

        try:
            tx = self.NewSetPermissionTx(tx_opts, request)
        except Exception as e:
            raise ValueError(f"failed to create NewSetPermissionTx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, request["WaitForReceipt"])
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt
    
    
    def new_accept_admin_tx(self, tx_opts: Dict[str, any], request: Dict[str, any]) -> Any:
        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")
        
        try:
            tx = self.permissioncontrol.functions.AcceptAdmin(
                request["AccountAddress"]
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create AcceptAdmin tx: {e}") from e
        
        return tx

    
    def accept_admin(self, ctx: Any, request: Dict[str, any]) -> Any:
        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            tx = self.NewAcceptAdminTx(tx_opts, request)
        except Exception as e:
            raise ValueError(f"failed to create AcceptAdmin transaction: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, request["WaitForReceipt"])
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    
    def new_add_pending_admin_tx(self, tx_opts: Dict[str, any], request: Dict[str, any]) -> Any:
        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")
        
        try:
            tx = self.permissioncontrol.functions.AddPendingAdmin(
                request["AccountAddress"],
                request["AdminAddress"]
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create AddPendingAdmin tx: {e}") from e

        return tx

    
    def new_remove_admin_tx(self, tx_opts: Dict[str, any], request: Dict[str, any]) -> Any:
        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")
        
        try:
            tx = self.permissioncontrol.functions.RemoveAdmin(
                request["AccountAddress"],
                request["AdminAddress"]
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create RemoveAdmin tx: {e}") from e

        return tx

    
    def new_remove_pending_admin_tx(self, tx_opts: Dict[str, any], request: Dict[str, any]) -> Any:
        if self.permissioncontrol is None:
            raise ValueError("permission contract not provided")
        
        try:
            tx = self.permissioncontrol.functions.RemovePendingAdmin(
                request["AccountAddress"],
                request["AdminAddress"]
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create RemovePendingAdmin tx: {e}") from e

        return tx

    def remove_pending_admin(self, ctx: Any, request: Dict[str, any]) -> Any:
        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            tx = self.NewRemovePendingAdminTx(tx_opts, request)
        except Exception as e:
            raise ValueError(f"failed to create RemovePendingAdmin transaction: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, request["WaitForReceipt"])
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    #rewardcordinator 
    
    def set_claimer_for(self, ctx: Any, claimer: Address, wait_for_receipt: bool) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        try:
            no_send_tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no-send tx opts: {e}") from e

        try:
            tx = self.reward_cordinator.functions.SetClaimerFor(claimer).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create SetClaimerFor tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def process_claim(self, ctx: Any, claim: Any, recipient_address: Address, wait_for_receipt: bool) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Build the transaction. Note: In web3.py, transaction options are passed
            # to the `transact()` method rather than as a function argument.
            tx = self.reward_cordinator.functions.ProcessClaim(claim, recipient_address).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create ProcessClaim tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    

    def set_operator_avs_split(self, ctx: Any, operator: Address, avs: Address, split: int, wait_for_receipt: bool) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            tx = self.reward_cordinator.functions.SetOperatorAVSSplit(operator, avs, split).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create SetOperatorAVSSplit tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def set_operator_pi_split(self, ctx: Any, operator: Address, split: int, wait_for_receipt: bool) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # Call the contract function SetOperatorPISplit.
            tx = self.reward_cordinator.functions.SetOperatorPISplit(operator, split).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create SetOperatorPISplit tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt


    def set_operator_set_split(self, ctx: Any, operator: Address, operator_set: Dict[str, any], split: int, wait_for_receipt: bool) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")
        
        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            # The operator_set parameter is expected to match the structure required by your contract's ABI.
            tx = self.reward_cordinator.functions.SetOperatorSetSplit(
                operator,
                operator_set,
                split
            ).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create SetOperatorSetSplit tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    def process_claims(self, ctx: Any, claims: List[Any], recipient_address: Address, wait_for_receipt: bool) -> Any:
        if self.reward_cordinator is None:
            raise ValueError("RewardsCoordinator contract not provided")

        if not claims:
            raise ValueError("claims is empty, at least one claim must be provided")

        try:
            tx_opts = self.tx_mgr.GetNoSendTxOpts()
        except Exception as e:
            raise ValueError(f"failed to get no send tx opts: {e}") from e

        try:
            tx = self.reward_cordinator.functions.ProcessClaims(claims, recipient_address).transact(tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create ProcessClaims tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send tx: {e}") from e

        return receipt

    #strategy

    
    def deposit_erc20_into_strategy(self, ctx: Any, strategy_addr: Address, amount: int, wait_for_receipt: bool) -> Any:
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
            _, underlying_token_contract, underlying_token_addr = self.elChainReader.GetStrategyAndUnderlyingERC20Token(ctx, strategy_addr)
        except Exception as e:
            raise ValueError(f"failed to get strategy and underlying ERC20 token: {e}") from e

        # Approve the strategy manager to spend the tokens.
        try:
            tx = underlying_token_contract.functions.Approve(self.strategy_manager_addr, amount).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create approve token transfer tx: {e}") from e

        try:
            # Send the approval transaction.
            _ = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send approval tx: {e}") from e

        # Deposit tokens into the strategy.
        try:
            tx = self.strategy_manager.functions.DepositIntoStrategy(strategy_addr, underlying_token_addr, amount).transact(no_send_tx_opts)
        except Exception as e:
            raise ValueError(f"failed to create DepositIntoStrategy tx: {e}") from e

        try:
            receipt = self.tx_mgr.Send(ctx, tx, wait_for_receipt)
        except Exception as e:
            raise ValueError(f"failed to send deposit tx: {e}") from e

        self.logger.info(f"deposited {amount} into strategy {strategy_addr}")
        return receipt