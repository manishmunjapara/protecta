# loganalyzer/analyzer.py

class LogAnalyzer:
    def __init__(self, log_data=None):
        self.logs = log_data.splitlines() if log_data else []

    def load_log(self, text):
        self.logs = text.splitlines()

    def total_lines(self):
        return len(self.logs)

    def search_keyword(self, keyword):
        return [line for line in self.logs if keyword in line]

    def count_keyword(self, keyword):
        return sum(1 for line in self.logs if keyword in line)

    def get_unique_ips(self):
        return list(set(line.split()[0] for line in self.logs if line.strip()))

    def filter_by_status(self, status_code):
        return [line for line in self.logs if f' {status_code} ' in line]

    def error_lines(self):
        return [line for line in self.logs if "error" in line.lower()]

    def get_summary(self):
        return {
            "total_lines": self.total_lines(),
            "unique_ips": len(self.get_unique_ips()),
            "error_lines": len(self.error_lines())
        }

    def print_top_lines(self, n=5):
        return self.logs[:n]
