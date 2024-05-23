class HTMLReporter:
    def __init__(self, financial_data):
        self.financial_data = financial_data

    def generate_report(self):
        report_lines = ["<html><body><table>"]
        for item in self.financial_data:
            name = item.get('name', 'N/A')
            amount = item.get('amount', 0)
            if amount < 0:
                amount_str = f'<span style="color:red">{amount}</span>'
            else:
                amount_str = f"{amount}"
            report_lines.append(f"<tr><td>{name}</td><td>{amount_str}</td></tr>")
        report_lines.append("</table></body></html>")

        return "\n".join(report_lines)
