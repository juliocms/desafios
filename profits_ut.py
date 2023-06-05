from profits import AcquirerLTDA
import unittest

class AcquirerLTDATests(unittest.TestCase):

    def setUp(self):
        # Dados das transações e contratos
        self.transactions = [
            {"transaction_id": 1, "client_id": 3545, "total_amount": 3000, "discount_percentage": 6.99},
            {"transaction_id": 2, "client_id": 3545, "total_amount": 4500, "discount_percentage": 0.45},
            {"transaction_id": 3, "client_id": 3509, "total_amount": 69998, "discount_percentage": 0},
            {"transaction_id": 4, "client_id": 3510, "total_amount": 1, "discount_percentage": None},
            {"transaction_id": 5, "client_id": 4510, "total_amount": 34, "discount_percentage": 40},
        ]

        self.contracts = [
            {"contract_id": 3, "client_id": 3545, "client_name": "Magazine Luana", "percentage": 2.00, "is_active": True},
            {"contract_id": 4, "client_id": 3545, "client_name": "Magazine Luana", "percentage": 1.95, "is_active": False},
            {"contract_id": 5, "client_id": 3509, "client_name": "Lojas Italianas", "percentage": 1, "is_active": True},
            {"contract_id": 6, "client_id": 3510, "client_name": "Carrerfive", "percentage": 3.00, "is_active": True},
        ]

        # Criar instância da classe
        self.acquirer = AcquirerLTDA()

    def test_profit_calculate(self):
        # Resultado esperado
        waited_result = 845.411

        # Calcular o ganho total
        profit = self.acquirer.profit_calculate(self.transactions, self.contracts)

        # Verificar se o resultado está correto
        self.assertAlmostEqual(profit, waited_result, delta=0.001)

if __name__ == '__main__':
    unittest.main()
