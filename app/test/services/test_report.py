import pytest

def test_get_report_service(client, report_uri, create_orders):
    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))
    pytest.assume(response.json['ingredient'])
    pytest.assume(response.json['client_data'])
    pytest.assume(response.json['month_with_more_revenue'])