from datetime import datetime
import pytest

from app.controllers.order import OrderController
from app.controllers.report import ReportController


def test_get_all(app, create_repeted_clients_and_ingredients_order):
    orders, most_repeated_ingredient_id, month_with_more_revenue, top_3_clients = create_repeted_clients_and_ingredients_order
    month_with_more_revenue = datetime.strptime(month_with_more_revenue, '%m/%d/%Y')
    created_order_result = []
    for order in orders:
        created_order, error = OrderController.create(order)
        pytest.assume(error is None)
        created_order_result.append(created_order)
    report_from_db, error = ReportController.get_all()
    pytest.assume(error is None)
    pytest.assume(report_from_db['ingredient']['id'] == most_repeated_ingredient_id)
    pytest.assume(report_from_db['client_data']['clients'][0]['client_name'] == top_3_clients[0]["client_name"])
    pytest.assume(report_from_db['client_data']['clients'][1]['client_name'] == top_3_clients[1]["client_name"])
    pytest.assume(report_from_db['client_data']['clients'][2]['client_name'] == top_3_clients[2]["client_name"])
    pytest.assume(report_from_db['month_with_more_revenue'] == month_with_more_revenue.month)
    
