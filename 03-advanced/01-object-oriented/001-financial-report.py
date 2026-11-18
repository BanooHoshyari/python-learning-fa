from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


class FileHandler:
    def __init__(self, file_path: str, encoding: str = "utf-8"):
        self.file_path = Path(file_path)
        self.encoding = encoding

    def read(self) -> str:
        if not self.file_path.exists():
            return ""
        with self.file_path.open("r", encoding=self.encoding) as file:
            return file.read()

    def write(self, content: str) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w", encoding=self.encoding) as file:
            file.write(content)

    def append(self, content: str) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("a", encoding=self.encoding) as file:
            file.write(content)


class LogWriter(FileHandler):
    def __init__(self, log_path: str):
        super().__init__(log_path)

    def log(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.append(f"[{timestamp}] {message}\n")


class FinancialReport(FileHandler):
    def __init__(self, report_path: str, log_path: str):
        super().__init__(report_path)
        self.log_writer = LogWriter(log_path)

    def load_records(self):
        data = self.read()
        if not data.strip():
            return []

        try:
            records = json.loads(data)
            if isinstance(records, list):
                return records
        except json.JSONDecodeError:
            pass

        return []

    def save_records(self, records) -> None:
        payload = json.dumps(records, ensure_ascii=False, indent=2)
        self.write(payload)
        self.log_writer.log(f"Saved {len(records)} records to {self.file_path}")

    def add_record(self, title: str, amount: float) -> None:
        records = self.load_records()
        records.append({"title": title, "amount": amount})
        self.save_records(records)

    def total_income(self) -> float:
        records = self.load_records()
        return sum(item["amount"] for item in records if item.get("amount", 0) >= 0)

    def total_expense(self) -> float:
        records = self.load_records()
        return sum(abs(item["amount"]) for item in records if item.get("amount", 0) < 0)

    def summary(self):
        income = self.total_income()
        expense = self.total_expense()
        net = income - expense
        return {
            "income": income,
            "expense": expense,
            "net": net,
        }


if __name__ == "__main__":
    report = FinancialReport("financial_data.json", "financial.log")

    report.save_records([
        {"title": "Salary", "amount": 5000},
        {"title": "Rent", "amount": -1200},
        {"title": "Food", "amount": -350},
        {"title": "Freelance", "amount": 800},
    ])

    print(report.summary())
