class CustomerRequest:
    WEEKENDS = ('(sat)', '(sun)')
    def __init__(self, customer_type, requested_dates):
        self.customer_type = customer_type
        self.request_dates = requested_dates
        self.set_weekends_and_weekdays()

    def set_weekends_and_weekdays(self):
        weekdays_count = 0
        weekends_count = 0

        for day in self.request_dates:
            if day.endswith(self.WEEKENDS):
                weekends_count+=1
            else:
                weekdays_count+=1
        self.weekdays_count = weekdays_count
        self.weekends_count = weekends_count