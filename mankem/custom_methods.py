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
		yy = getdate(doc.posting_date).strftime("%y")
		mm = getdate(doc.posting_date).strftime("%m")
		if doc.doctype=="Stock Entry":
			series = company_abbr+"SE"+yy+ mm + ".###";
			doc.name =make_autoname(series)
		if doc.doctype=="Quotation":
			series = company_abbr+"QT"+yy+ mm + ".###";
			doc.name =make_autoname(series)
		if doc.doctype=="Delivery Note":
			series = company_abbr+"DN"+yy+ mm + ".###";
			doc.name =make_autoname(series)
		if doc.doctype=="Sales Invoice":
			series = company_abbr+"SI"+yy+ mm + ".###";
			doc.name =make_autoname(series)
		if doc.doctype=="Journal Entry":
			series = company_abbr+"JV"+yy+ mm + ".###";
			doc.name =make_autoname(series)
		if doc.doctype=="Purchase Invoice":
			series = company_abbr+"PI"+yy+ mm + ".###";
			doc.name =make_autoname(series)
		if doc.doctype=="Payment Entry":
			series = company_abbr+"PE"+yy+ mm + ".###";
			doc.name =make_autoname(series)
		if doc.doctype=="Purchase Order":
			series = company_abbr+"PO"+yy+ mm + ".###";
			doc.name =make_autoname(series)
		if doc.doctype=="Sales Order":
			series = company_abbr+"SO"+yy+ mm + ".###";
			doc.name =make_autoname(series)
