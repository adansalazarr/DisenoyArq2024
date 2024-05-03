import os
import pytest
from datetime import datetime
from unittest.mock import patch, mock_open
from patterns.csv_utils import parse_file, Ride
from patterns.web_report import create_file, create_content

@pytest.fixture
def csv_data(): #datros simulación para probar csv
    return "TaxiID,lpep_pickup_datetime,lpep_dropoff_datetime,passenger_count,trip_distance,total_amount,\n17083,2018-01-01 00:18:50,2018-01-01 00:24:39,5,0.7,7.3"

@pytest.fixture
def rides(): #objeto ride para probar html
    return [Ride(error="", taxi_id=17083, pick_up_time=datetime.strptime("2018-01-01 00:18:50", '%Y-%m-%d %H:%M:%S'),
                 drop_of_time=datetime.strptime("2018-01-01 00:24:39", '%Y-%m-%d %H:%M:%S'), passenger_count=5,
                 trip_distance=0.7, tolls_amount=7.3)]

def test_csv(mocker, csv_data):
    openfile = mock_open(read_data=csv_data)
    mocker.patch('builtins.open', openfile) #leemos desde datos simulación
    rides = parse_file('test_file.csv')
    assert len(rides) > 0
    for ride in rides:
        assert ride.taxi_id #validamos que existe al menos un id valido

def test_html(rides):
    html_content = create_content(rides) #create content genera contenido
    create_file(html_content)
    assert os.path.exists("financial-report.html") #validanmos creación
    os.remove("financial-report.html") #lo borramos
