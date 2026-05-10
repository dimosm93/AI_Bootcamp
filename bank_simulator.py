class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        # 1. Κάνε το balance PRIVATE χρησιμοποιώντας διπλό underscore
        self.__balance = balance

    # Getter μέθοδος για να διαβάζουμε το private balance
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Επιτυχής κατάθεση {amount}€. Νέο υπόλοιπο: {self.get_balance()}€")
        else:
            print("Σφάλμα: Το ποσό πρέπει να είναι θετικό!")

    def withdraw(self, amount):
        # 2. TODO: Συμπλήρωσε τον έλεγχο. 
        # Πρέπει το amount να είναι θετικό ΚΑΙ να μην ξεπερνάει το self.get_balance()
        if amount > 0 and amount <= self.get_balance():
            self.__balance -= amount
            print(f"Επιτυχής ανάληψη {amount}€. Νέο υπόλοιπο: {self.get_balance()}€")
        else:
            print("Σφάλμα: Ανεπαρκές υπόλοιπο ή άκυρο ποσό!")

    def apply_interest(self):
        pass


class SavingsAccount(Account):
    def apply_interest(self):
        # 3. TODO: Πρόσθεσε τόκο 2% στο υπόλοιπο.
        # Πάρε το τρέχον balance, υπολόγισε το 2% και κάνε κατάθεση (deposit) αυτό το ποσό!
        interest = self.get_balance() * 0.02
        self.deposit(interest)
        print("Εφαρμόστηκε τόκος αποταμίευσης 2%.")


class InvestmentAccount(Account):
    def apply_interest(self):
        # Τόκος 10% για τον επενδυτικό
        interest = self.get_balance() * 0.10
        self.deposit(interest)
        print("Εφαρμόστηκε επενδυτικός τόκος 10%.")


# ==========================================
# ΚΕΝΤΡΙΚΟ ΜΕΝΟΥ (CLI)
# ==========================================
print("--- Καλώς ήρθατε στον Προσομοιωτή Τράπεζας ---")
name = input("Δώστε το όνομά σας για τη δημιουργία λογαριασμού: ")
acc_type = input("Τύπος λογαριασμού (savings / investment): ").strip().lower()
initial_money = float(input("Αρχική κατάθεση (€): "))

if acc_type == "savings":
    account = SavingsAccount(name, initial_money)
else:
    account = InvestmentAccount(name, initial_money)

while True:
    print("\n--- Επιλογές ---")
    print("1. Προβολή Υπολοίπου")
    print("2. Κατάθεση")
    print("3. Ανάληψη")
    print("4. Εφαρμογή Τόκου")
    print("5. Έξοδος")
    
    choice = input("Επιλέξτε ενέργεια (1-5): ")
    
    if choice == "1":
        print(f"Υπόλοιπο: {account.get_balance()}€")
    elif choice == "2":
        amt = float(input("Ποσό κατάθεσης: "))
        account.deposit(amt)
    elif choice == "3":
        amt = float(input("Ποσό ανάληψης: "))
        account.withdraw(amt)
    elif choice == "4":
        account.apply_interest()
    elif choice == "5":
        print("Ευχαριστούμε που μας προτιμήσατε!")
        break
    else:
        print("Άκυρη επιλογή!")