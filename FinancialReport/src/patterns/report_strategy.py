#strategy, estrategia para cada formato
class ReportContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def generate_report(self):
        return self.strategy.generate_report()
