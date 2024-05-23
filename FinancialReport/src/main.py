from patterns.report_factory import ReportFactory
from patterns.report_adapter import ReportAdapter
from patterns.csv_utils import parse_file

def main():
    rides = parse_file("taxi-data.csv")

    # reporte en consola
    print_report = ReportFactory.create_report("print", rides)
    print_adapter = ReportAdapter(print_report)
    print_report_content = print_adapter.generate()
    print("Reporte consola")
    print(print_report_content)

    # reporte html
    html_report = ReportFactory.create_report("html", rides)
    html_adapter = ReportAdapter(html_report)
    html_report_content = html_adapter.generate()
    from patterns.web_report import create_file
    create_file(html_report_content)
    print("\nReporte html correcto")

if __name__ == "__main__":
    main()
