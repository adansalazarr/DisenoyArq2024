#factory pattern
from patterns.print_reporter import PrintReporter
from patterns.web_report import WebReporter

class ReportFactory:
    @staticmethod
    def create_report(report_type, rides):
        if report_type == "print": #consola
            return PrintReporter(rides)
        elif report_type == "html": #html
            return WebReporter(rides)
        else:
            raise ValueError("Error")
