import frappe
from frappe.model.mapper import get_mapped_doc
from frappe import throw, _
from frappe.model.naming import make_autoname


@frappe.whitelist()
@frappe.whitelist()
def set_autoname(doc, method):
	company_abbr = frappe.db.get_value("Company",doc.company,"Company")
	if company_abbr:
		if doc.doctype="Stock Entry":
			yy = doc.posting_date.strftime("%Y")
			mm = doc.posting_date.strftime("%m")
			series = company_abbr+"SE"+yy+ mm + ".###";
			doc.name =make_autoname(series)
