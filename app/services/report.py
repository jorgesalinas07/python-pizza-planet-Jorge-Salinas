from app.common.http_methods import GET
from flask import Blueprint
from app.controllers.report import ReportController
from app.services.base import BaseService

report = Blueprint('report', __name__)

report_base_service = BaseService(entity = "report",
        entitycontroller = ReportController())

@report.route('/', methods=GET)
def get_report():
    return report_base_service.get_all() 
    