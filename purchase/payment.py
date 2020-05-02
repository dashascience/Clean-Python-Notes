class Payment:
    def do_payment(self, user, amount):
        print(f"Payment of ${amount} successfully done!")
		
class CreditPayment:
    def do_credit_payment(self, user, amount):
        print(f"Payment of ${amount} successfully done!")
	
__all__ = ["CreditPayment"]