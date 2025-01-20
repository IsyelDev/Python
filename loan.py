from datetime import datetime, timedelta

class Loan:
    """
    Clase para representar un préstamo.
    """
    def __init__(self, user: str, amount: float, due_date: str):
        """
        Inicializa un nuevo préstamo.
        :param user: Nombre del usuario.
        :param amount: Monto del préstamo.
        :param due_date: Fecha de vencimiento en formato YYYY-MM-DD.
        """
        self.user = user
        self.amount = amount
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = "Pending"

    def is_overdue(self) -> bool:
        """
        Verifica si el préstamo está vencido.
        """
        return datetime.now() > self.due_date

    def __str__(self) -> str:
        """
        Representación en texto del préstamo.
        """
        status = "Overdue" if self.is_overdue() else self.status
        return f"User: {self.user}, Amount: ${self.amount:.2f}, Due Date: {self.due_date.date()}, Status: {status}"


class LoanManager:
    """
    Clase para gestionar préstamos.
    """
    def __init__(self):
        self.loans = []

    def add_loan(self, user: str, amount: float, due_date: str):
        """
        Agrega un nuevo préstamo al sistema.
        :param user: Nombre del usuario.
        :param amount: Monto del préstamo.
        :param due_date: Fecha de vencimiento en formato YYYY-MM-DD.
        """
        loan = Loan(user, amount, due_date)
        self.loans.append(loan)
        print(f"Loan added: {loan}")

    def check_overdue_loans(self):
        """
        Verifica y notifica préstamos vencidos.
        """
        overdue_loans = [loan for loan in self.loans if loan.is_overdue()]
        if overdue_loans:
            print("\n=== Overdue Loans ===")
            for loan in overdue_loans:
                print(f"Notification: Loan for {loan.user} is overdue! Please remind them.")
                loan.status = "Overdue"
        else:
            print("\nNo overdue loans at the moment.")

    def list_loans(self):
        """
        Lista todos los préstamos.
        """
        if not self.loans:
            print("No loans registered.")
            return
        print("\n=== Loan List ===")
        for loan in self.loans:
            print(loan)


if __name__ == "__main__":
    manager = LoanManager()

    try:
        # Agregar préstamos
        manager.add_loan("Alice", 500.0, "2025-01-15")
        manager.add_loan("Bob", 300.0, "2025-01-25")
        manager.add_loan("Charlie", 1000.0, "2025-01-10")

        # Mostrar préstamos registrados
        manager.list_loans()

        # Verificar préstamos vencidos
        manager.check_overdue_loans()
    except Exception as e:
        print(f"Error: {e}")
