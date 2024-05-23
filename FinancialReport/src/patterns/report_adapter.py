#adapter pattern, unifica generación de reportes
class ReportAdapter:
    def __init__(self, report):
        self.report = report

    def generate(self):
        return self.report.generate_report()
