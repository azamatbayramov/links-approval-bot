from datetime import datetime


class ExportFilenameGenerator:
    @staticmethod
    def generate() -> str:
        return f"export_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv"
