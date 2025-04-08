# datavault/vault.py

class DataVault:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)
        return f"Added: {item}"

    def remove_item(self, item):
        if item in self.data:
            self.data.remove(item)
            return f"Removed: {item}"
        return "Item not found."

    def get_all(self):
        return self.data

    def clear_data(self):
        self.data.clear()
        return "All data cleared."

    def find_item(self, item):
        return item in self.data

    def count_items(self):
        return len(self.data)

    def sort_data(self, reverse=False):
        try:
            self.data.sort(reverse=reverse)
            return "Data sorted."
        except Exception as e:
            return f"Sort error: {e}"

    def reverse_data(self):
        self.data.reverse()
        return "Data reversed."

    def get_item_by_index(self, index):
        try:
            return self.data[index]
        except IndexError:
            return "Invalid index."

    def update_item(self, old_item, new_item):
        if old_item in self.data:
            index = self.data.index(old_item)
            self.data[index] = new_item
            return f"Updated {old_item} to {new_item}"
        return "Old item not found."
