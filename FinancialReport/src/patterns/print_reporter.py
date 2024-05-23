class PrintReporter:
    def __init__(self, rides):
        self.rides = rides

    def generate_report(self):
        builder = [self._create_table_headers()] #titulos
        for ride in self.rides:
            builder.append(self._add_ride(ride))
        return "\n".join(builder)

    def _create_table_headers(self):
        return "\t".join(["TaxiID", "Pickup time", "Dropoff time", "Passenger count", "Trip Distance", "Total amount"]) + "\n"

    def _add_ride(self, ride): #agregar datos
        return "\t".join([
            str(ride.taxi_id),
            ride.pick_up_time.isoformat(),
            ride.drop_of_time.isoformat(),
            str(ride.passenger_count),
            str(ride.trip_distance),
            self._format_amount(ride.tolls_amount)
        ]) + "\n"

    def _format_amount(self, amount): #formato para negativos
        if amount < 0:
            return f"({-amount})"
        return str(amount)
