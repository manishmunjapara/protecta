# preventer.py

class ProblemPreventer:
    def __init__(self):
        self.issues = []

    def add_issue(self, issue):
        self.issues.append(issue)
        return f"Issue '{issue}' added."

    def list_issues(self):
        return self.issues

    def remove_issue(self, issue):
        if issue in self.issues:
            self.issues.remove(issue)
            return f"Issue '{issue}' removed."
        return f"Issue '{issue}' not found."

    def clear_issues(self):
        self.issues.clear()
        return "All issues cleared."

    def has_issues(self):
        return len(self.issues) > 0

    def issue_count(self):
        return len(self.issues)

    def find_issue(self, keyword):
        return [issue for issue in self.issues if keyword.lower() in issue.lower()]

    def replace_issue(self, old, new):
        if old in self.issues:
            idx = self.issues.index(old)
            self.issues[idx] = new
            return f"Issue '{old}' replaced with '{new}'."
        return f"Issue '{old}' not found."

    def summary(self):
        return f"Total issues: {len(self.issues)}"

    def is_issue_present(self, issue):
        return issue in self.issues
