class Account:
    # Tüm hesapları saklayan static liste
    accounts = []

    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        Account.accounts.append(self)  # Hesabı tüm hesaplar listesine ekle
        Bank.track_transaction(f"Yeni hesap açıldı: {account_number}, Sahibi: {owner}")

    def deposit(self, amount):
        """Hesaba para yatırma işlemi."""
        if amount > 0:
            self.balance += amount
            print(f"{amount} TL yatırıldı. Güncel bakiye: {self.balance} TL")
            Bank.track_transaction(f"Para yatırma: {amount} TL, Hesap: {self.account_number}")
        else:
            print("Geçersiz miktar. Lütfen pozitif bir değer giriniz.")

    def withdraw(self, amount):
        """Hesaptan para çekme işlemi."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} TL çekildi. Güncel bakiye: {self.balance} TL")
            Bank.track_transaction(f"Para çekme: {amount} TL, Hesap: {self.account_number}")
        elif amount > self.balance:
            print(f"Yetersiz bakiye. Mevcut bakiye: {self.balance} TL")
        else:
            print("Geçersiz miktar. Lütfen pozitif bir değer giriniz.")

    def view_balance(self):
        """Hesap detaylarını ve bakiyeyi görüntüleme."""
        print(f"Hesap Sahibi: {self.owner}")
        print(f"Hesap Numarası: {self.account_number}")
        print(f"Bakiye: {self.balance} TL")


class Bank:
    # İşlem geçmişi için static liste
    transaction_history = []

    @staticmethod
    def display_bank_info():
        """Banka hakkında genel bilgileri görüntüleme."""
        print("Bankamız, tüm müşterilerimize kaliteli hizmet sunmayı taahhüt eder.")
        print(f"Toplam hesap sayısı: {len(Account.accounts)}")
        print(f"Toplam işlem sayısı: {len(Bank.transaction_history)}")

    @staticmethod
    def track_transaction(description):
        """İşlem geçmişine açıklama ekleme."""
        Bank.transaction_history.append(description)

    @staticmethod
    def display_transaction_history():
        """İşlem geçmişini görüntüleme."""
        print("\nİşlem Geçmişi:")
        for transaction in Bank.transaction_history:
            print(transaction)


# Ana program
def main():
    # Örnek hesaplar oluşturma
    account1 = Account("TR123456", "Ahmet Yılmaz", 5000.0)
    account2 = Account("TR654321", "Elif Demir", 10000.0)

    # Hesap işlemleri
    account1.view_balance()
    account1.deposit(2000)
    account1.withdraw(1000)
    account1.withdraw(7000)  # Yetersiz bakiye durumu

    account2.view_balance()
    account2.withdraw(3000)

    # Banka bilgileri ve işlem geçmişi
    Bank.display_bank_info()
    Bank.display_transaction_history()


if __name__ == "__main__":
    main()
