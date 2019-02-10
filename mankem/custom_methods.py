import frappe
from frappe.model.mapper import get_mapped_doc
from frappe import throw, _
from frappe.model.naming import make_autoname
from frappe.utils import flt, getdate, add_months, get_last_day, fmt_money, nowdate


@frappe.whitelist()
@frappe.whitelist()
def set_autoname(doc, method):
	company_abbr = frappe.db.get_value("Company",doc.company,"abbr_series")
	if company_abbr:
		if doc.doctype=="Stock Entry":
			yy = getdate(doc.posting_date).strftime("%y")
			mm = getdate(doc.posting_date).strftime("%m")
			series = company_abbr+"SE"+yy+ mm + ".###";
			doc.name =make_autoname(series)
