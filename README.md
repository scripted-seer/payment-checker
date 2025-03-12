# Payment Checker
![Python script for creating and checking TRON wallets](https://github.com/user-attachments/assets/e98af15e-7244-46a2-95f1-e32e4092d548)

## Introduction

Payment Checker is a Python project designed to manage and verify user payments. This system allows you to create a separate wallet for each customer, automatically check their payment status, and, upon confirmation, transfer funds to your main wallet.

## Features

- **Automatic Wallet Creation:** Creates a unique wallet for each user.
- **Payment Verification:** Periodically checks the status of each wallet to confirm payment receipt.
- **Funds Transfer:** Transfers funds from individual wallets to your main wallet upon payment confirmation.
- **Easy Integration:** Easily integrates with your sales and transaction management system.
- **Scalability:** Modular code design allows for easy expansion and addition of new features.

## Installation

Ensure Python is installed, then install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## File Structure

- **`main.py`**: The main file that contains the logic for wallet creation, payment verification, and funds transfer.
- **`requirements.txt`**: A file listing all the necessary libraries and dependencies required to run the project.

## Usage

1. **Setup:** Install all required dependencies as mentioned above.
2. **Run the project:** Execute the main file:

    ```bash
    python main.py
    ```

3. **Workflow:**
   - **Wallet Creation:** When a purchase is made, a unique wallet is created for the user.
   - **Payment Verification:** The system automatically checks the wallet for payment confirmation.

## Example Code

```python
def create_wallet(user_id):
    """
    Create a unique wallet for the user.
    """
    # Implementation for wallet creation
    pass

def check_payment(wallet_id):
    """
    Verify if the payment has been received in the wallet.
    """
    # Implementation for payment verification
    pass

def aggregate_funds(wallet_ids, main_wallet):
    """
    Transfer funds from individual wallets to the main wallet.
    """
    # Implementation for funds transfer
    pass

if __name__ == '__main__':
    # Example usage:
    user_id = "user123"
    wallet_id = create_wallet(user_id)
    
    if check_payment(wallet_id):
        print(f"Payment received from user {user_id}. Transferring funds...")
        aggregate_funds([wallet_id], main_wallet="main_wallet_001")
    else:
        print("Payment not yet received.")
```


## Contributing

Contributions are welcome. If you have suggestions, ideas, or improvements, feel free to submit a Pull Request or create an Issue in this repository.


