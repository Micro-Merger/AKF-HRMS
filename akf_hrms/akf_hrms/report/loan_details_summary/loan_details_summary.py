# Copyright (c) 2024, Nabeel Saleem and contributors
# For license information, please see license.txt

import frappe
from datetime import timedelta, datetime
from frappe import msgprint, _


@frappe.whitelist(allow_guest=True)
def execute(filters=None):
    columns, data = [], []
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    columns = [
        _("Company") + ":Link/Company:140",
        _("Employee ID") + ":Dynamic Link/Employee:140",
        _("Employee Name") + ":Data:140",
        _("Branch") + ":Link/Branch:140",
        _("Loan Application ID") + ":Link/Loan Application:140",
        _("Loan ID") + ":Data:140",
        _("Loan Type") + ":Link/Loan Category:140",
        _("Total Intallments") + ":Int:140",
        _("Principal Amount") + ":Currency:140",
        _("Amount Paid") + ":Currency:140",
        _("Pending Amount") + ":Currency:140",
        _("Loan Status") + ":Select:140",
        _("Repayment Start Date") + ":Date:140",
    ]
    return columns


def get_data(filters):
    result = get_query_result(filters)
    return result


def get_conditions(filters):
    conditions = ""

    if filters.get("company"):
        conditions += " AND company = %(company)s"
    if filters.get("applicant"):
        conditions += " AND applicant = %(applicant)s"
    if filters.get("branch"):
        conditions += " AND branch = %(branch)s"
    if filters.get("loan_type"):
        conditions += " AND loan_type = %(loan_category)s"
    if filters.get("repayment_start_date"):
        conditions += " AND repayment_start_date = %(repayment_start_date)s"

    return conditions


def get_query_result(filters):
    conditions = get_conditions(filters)
    result = frappe.db.sql(
        """
        SELECT 
			company,
			applicant,
			applicant_name,
            branch, 
            loan_application,
            name,
            loan_category,
            repayment_periods,
            total_payment,
            total_amount_paid,
            (total_payment-total_amount_paid),
            status,
            repayment_start_date
        FROM 
            `tabLoan`
        WHERE
            docstatus != 2
        {0}
    """.format(
            conditions if conditions else ""
        ),
        filters,
        as_dict=0,
    )
    return result
