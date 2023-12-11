from django.db import models

class StockMarketData(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=20)
    high = models.DecimalField(max_digits=5, decimal_places=2)
    low = models.DecimalField(max_digits=5, decimal_places=2)
    open = models.DecimalField(max_digits=5, decimal_places=2)
    close = models.DecimalField(max_digits=5, decimal_places=2)
    volume = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.trade_code} - {self.date}"
    
    class Meta:
        app_label = 'myapp'
    # def to_python(self, value):
    #         if isinstance(value, int):
    #             return value
    #         try:
    #             # Attempt to convert the value to an integer
    #             return int(value.replace(',', ''))
    #         except (ValueError, TypeError):
    #             # If conversion fails, raise a validation error
    #             raise models.ValidationError(
    #                 f'“{value}” value must be a decimal number.'
    #             )