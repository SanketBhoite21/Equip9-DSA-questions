import bisect

class MaintenanceLog:
    def __init__(self, maintenance_logs):
        # Sort logs by date
        self.dates = []
        self.costs = []
        self.prefix_sum = []
        total = 0

        for _, date, cost in maintenance_logs:
            self.dates.append(date)
            self.costs.append(cost)
            total += cost
            self.prefix_sum.append(total)
    
    def query_cost(self, start_date, end_date):
        # Find range indices
        left = bisect.bisect_left(self.dates, start_date)
        right = bisect.bisect_right(self.dates, end_date) - 1

        if left > right:
            return 0  # No records in range
        
        return self.prefix_sum[right] - (self.prefix_sum[left - 1] if left > 0 else 0)

if __name__ == "__main__":
    
    
    maintenance_logs = [
        (101, "2024-01-01", 500),
        (102, "2024-01-10", 300),
        (101, "2024-01-15", 700)
    ]
    queries = [("2024-01-01", "2024-01-10"), ("2024-01-01", "2024-01-15")]
    
    log = MaintenanceLog(maintenance_logs)
    result = [log.query_cost(start, end) for start, end in queries]
    
    print("Total maintenance costs:", result)