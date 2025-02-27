# **eigensdk-python**


This document outlines the steps taken by the iF3 team to improve and update the eigensdk-python SDK.
### 1. Deploying Eigen Contracts via Makefile

To streamline the deployment process of Eigen contracts, a `Makefile` has been integrated into the SDK. This addition facilitates automated deployment of contracts, ensuring consistency and reducing manual intervention.

**Steps:**

1. **Install Dependencies:** Ensure all necessary dependencies are installed.
    
2. **Execute Makefile:** Run the following command in your terminal:
    
    ```bash
    make run
    ```
    
    This command will automatically deploy the Eigen contracts.
    

### 2. Updating Contract Calls

The contract calls within `elcontract/reader.py` have been revised to address compatibility issues arising from the recent Eigen slashing update. These modifications are crucial to maintain the SDK's functionality with the updated system.

**Steps:**

1. **Identify Issues:** Determine which contract calls are incompatible with the new updates.
    
2. **Implement Changes:** Modify the identified calls in accordance with the latest Eigen documentation.
    
3. **Test Modifications:** Verify that the changes function as intended.
    

### 3. Writing Tests for Updates

To validate the recent updates, new tests have been developed. These tests focus on the updated contract interactions, ensuring the system operates as expected.

**Steps:**

1. **Develop Tests:** Create tests that encompass various scenarios related to the updates.
    
2. **Run Tests:** Execute the tests and analyze the outcomes.
    
3. **Debug if Necessary:** If issues are detected, refine the code and rerun the tests until successful.
    

### 4. Merging Updates into the Main Codebase

After thorough testing, the updates have been integrated into the primary codebase. Path configurations have been adjusted to ensure compatibility with previous updates, eliminating the need for additional changes.

**Steps:**

1. **Merge Code:** Incorporate the changes into the main branch.
    
2. **Verify Compatibility:** Ensure the new code harmonizes with existing components.
    
3. **Update Documentation:** Revise any relevant documentation to reflect the recent changes.
    

### 5. Integrating and Running Tests

The newly developed tests have been added to the main test suite and executed to confirm the stability and accuracy of the updates.

**Steps:**

1. **Incorporate Tests:** Add the new tests to the existing test framework.
    
2. **Execute Comprehensive Testing:** Run all tests to ensure overall system integrity.
    
3. **Address Any Issues:** If any tests fail, investigate and resolve the underlying problems.
    

**Note:** For more detailed information and access to complete documentation, please visit the 

# *run and test*
get project 
```sh
git clone git@github.com:zellular-xyz/eigensdk-python.git
git checkout iF3-Slashing
```

## install eigensdk-python package

```sh
cd iF3-Slashing
virtualenv .venv
source .vnev/bin/activate
pip install .
```

## deploy contract and run anvil

```sh
make run
```

_Hint:_ To stop the anvil, use:

```sh
make kill
```

## Running Tests

Navigate to the test directory:

```sh
cd tests/elreader/
```

Run the test script using pytest:

```sh
pytest -s ./test_el_reader.py
```

