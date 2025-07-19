# Base class for accounts
class Account:
    def __init__(self):
        self.cust_id = 0
        self.bal = 0


class SBAccount(Account):
    def __init__(self, cust_id, bal):
        super().__init__()
        self.bal = bal
        self.cust_id = cust_id
        print("\n🔔 New SB Account created Successfully!")
        print(f"👤 Customer ID     : {cust_id}")
        print(f"💰 Initial Balance : ₹{bal:.2f}")

    def deposit(self, dep_amt):
        # Deposit amount if positive
        if dep_amt > 0:
            print(f"\n📥 Deposit of ₹{dep_amt:.2f}")
            print(f"   Before Deposit : ₹{self.bal:.2f}")
            self.bal += dep_amt
            print(f"   After Deposit  : ₹{self.bal:.2f}")
        else:
            print("⚠️ Invalid Amount!!!")

    def withdraw(self, with_amt):
        # Withdraw only if balance remains >= 1000 after withdrawal
        if self.bal > with_amt + 1000:
            print(f"\n💸 Withdrawal of ₹{with_amt:.2f}")
            print(f"   Before Withdrawal : ₹{self.bal:.2f}")
            self.bal -= with_amt
            print(f"   After Withdrawal  : ₹{self.bal:.2f}")
        else:
            print("❌ Insufficient Balance!!!")

    def calc_interest(self):
        # Calculate and add interest at 4% p.a. for one month
        print(f"\n📈 Calculating Interest on Balance: ₹{self.bal:.2f}")
        interest = 0.04 * self.bal / 12
        print(f"   Interest Rate: 4% annually")
        print(f"   Monthly Interest: ₹{interest:.2f}")
        self.bal += interest
        print(f"   New Balance: ₹{self.bal:.2f}")


class FDAccount(Account):
    def __init__(self, period, cust_id, bal):
        self.period = period
        self.cust_id = cust_id
        self.bal = bal
        super().__init__()
        print("\n🔐 Fixed Deposit Account Created!")
        print(f"👤 Customer ID   : {cust_id}")
        print(f"💰 Deposit Amount: ₹{bal:.2f}")
        print(f"🕒 Period        : {period} months")

    def calc_interest(self):
        return 0.0825 * self.bal * self.period / 12

    def close(self):
        # Close FD and credit interest
        print(f"\n🔓 Closing Fixed Deposit")
        print(f"   Balance Before Interest: ₹{self.bal:.2f}")
        interest = self.calc_interest()
        print(f"   Interest Earned        : ₹{interest:.2f}")
        self.bal += interest
        print(f"   Balance After Interest : ₹{self.bal:.2f}")


class Customer:
    def __init__(self, cust_id, name, address):
        self.cust_id = cust_id
        self.name = name
        self.address = address
        self.bal = 0
        self.period = 0
        self.sb = None  # SBAccount object
        self.fd = None  # FDAccount object

    def createAccount(self, val):
        # Create Savings Account
        if val == 1:
            self.bal = float(input("💵 Enter Initial Balance: ₹"))
            self.sb = SBAccount(self.cust_id, self.bal)
        # Create Fixed Deposit Account
        elif val == 2:
            self.bal = float(input("💵 Enter Initial Balance: ₹"))
            self.period = int(input("🕒 Enter Period (months): "))
            self.fd = FDAccount(self.period, self.cust_id, self.bal)
        else:
            print("❗ Invalid choice")

    def transaction(self, val):
        # Perform Deposit on SBAccount
        if val == 1:
            amt = float(input("💰 Enter Amount to Deposit: ₹"))
            self.sb.deposit(amt)
        elif val == 2:
            # Perform Withdrawal on SBAccount
            amt = float(input("💸 Enter Amount to Withdraw: ₹"))
            self.sb.withdraw(amt)
        elif val == 3:
            # Calculate interest on SBAccount
            self.sb.calc_interest()
        elif val == 4:
            # Close Fixed Deposit Account
            self.fd.close()
            print("✅ Fixed Deposit Account Closed Successfully!")
        else:
            print("❗ Invalid choice")


# Main Program
c = []
j = 0
cust_id = 1000000

print("\n" + "="*60)
print("🏦 Welcome to ABC Bank".center(60))
print("="*60)

while True:
    # Main menu
    print("\n📋 Main Menu")
    print("1.Savings Account")
    print("2.Fixed Deposit Account")
    print("3.Exit")
    ch1 = int(input("👉 Enter your choice: "))

    if ch1 == 1:
        ch2 = 0
        # Sub-menu for SBAccount
        while ch2 != 5:
            print("\n📘 Savings Account Menu")
            print("1.Open New SB Account")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Calculate Interest")
            print("5.Back to Main Menu")
            ch2 = int(input("👉 Enter your choice: "))

            if ch2 == 1:
                # Create new SBAccount
                name = input("👤 Enter your name: ")
                address = input("🏠 Enter your address: ")
                c.append(Customer(cust_id + j, name, address))
                c[j].createAccount(1)
                j += 1
            elif ch2 == 2:
                cus_id = int(input("🔑 Enter Customer ID: "))
                c[cus_id - cust_id].transaction(1)
            elif ch2 == 3:
                cus_id = int(input("🔑 Enter Customer ID: "))
                c[cus_id - cust_id].transaction(2)
            elif ch2 == 4:
                cus_id = int(input("🔑 Enter Customer ID: "))
                c[cus_id - cust_id].transaction(3)
            elif ch2 == 5:
                print("👋 Returning to Main Menu...")
            else:
                print("❗ Invalid choice")

    elif ch1 == 2:
        ch3 = 0
        # Sub-menu for FDAccount
        while ch3 != 3:
            print("\n📙 Fixed Deposit Menu")
            print("1.Open New FD Account")
            print("2.Close FD Account")
            print("3.Back to Main Menu")
            ch3 = int(input("👉 Enter your choice: "))

            if ch3 == 1:
                # Create new FDAccount
                name = input("👤 Enter your name: ")
                address = input("🏠 Enter your address: ")
                c.append(Customer(cust_id + j, name, address))
                c[j].createAccount(2)
                j += 1
            elif ch3 == 2:
                cus_id = int(input("🔑 Enter Customer ID: "))
                c[cus_id - cust_id].transaction(4)
            elif ch3 == 3:
                print("👋 Returning to Main Menu...")
            else:
                print("❗ Invalid choice")

    elif ch1 == 3:
        print("\n🙏 Thank you for banking with us! Have a great day!")
        print("="*60)
        break
    else:
        print("❗ Invalid choice")
