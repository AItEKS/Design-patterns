from typing import List
from Source.Models.storage_row_model import storage_row_model
from Source.Models.storage_turn_model import storage_turn_model


class process_storage_turn:
    @staticmethod
    def process_storage_turn(transactions: List[storage_row_model]) -> List[storage_turn_model]:
        storage_turnover = []

        grouped_transactions: dict = {}
        for transaction in transactions:
            key = {transaction.period, transaction.nomenclature, transaction.unit, transaction.storage_name}
            if key not in grouped_transactions:
                grouped_transactions[key] = []
            grouped_transactions[key].append(transaction)

        for key, group in grouped_transactions.items():
            turnover = sum(transaction.count if transaction.type_tranzaction else -transaction.count for transaction in group)

            storage_turn = storage_turn_model()
            storage_turn.storage_name = key[3]
            storage_turn.unit = key[2]
            storage_turn.turnover = turnover
            storage_turn.nomenclature = key[1]
            storage_turn.period =key[0]

            storage_turnover.append(storage_turn)

        return storage_turnover