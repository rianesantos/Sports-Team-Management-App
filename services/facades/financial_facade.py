import services.services as sv

class FinancialFacade:
    """
    Facade para o subsistema Financeiro.
    Simplifica o acesso às funcionalidades de registro e saldo.
    """
    def register_income(self):
        sv.register_income()

    def register_expense(self):
        sv.register_expense()
    
    def get_current_balance(self):
        # A função que expõe o saldo, utilizando o serviço ou Data Manager
        return sv.get_current_balance()