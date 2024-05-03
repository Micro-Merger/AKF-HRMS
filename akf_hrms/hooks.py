app_name = "akf_hrms"
app_title = "Akf Hrms"
app_publisher = "Nabeel Saleem"
app_description = "Al Khidmat Foundation Human Resource Management System Application."
app_email = "nabeel.socail.use@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/akf_hrms/css/akf_hrms.css"
# app_include_js = "/assets/akf_hrms/js/akf_hrms.js"

# include js, css files in header of web template
# web_include_css = "/assets/akf_hrms/css/akf_hrms.css"
# web_include_js = "/assets/akf_hrms/js/akf_hrms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "akf_hrms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    # "Overtime Claim Form" : "public/js/custom_doctype_js/overtime_claim_form.js",
    "Staffing Plan": "public/js/staffing_plan.js",
    "Loan": "public/js/loan.js",
    "Loan Application": "public/js/loan_application.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "akf_hrms/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "akf_hrms.utils.jinja_methods",
# 	"filters": "akf_hrms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "akf_hrms.install.before_install"
# after_install = "akf_hrms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "akf_hrms.uninstall.before_uninstall"
# after_uninstall = "akf_hrms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "akf_hrms.utils.before_app_install"
# after_app_install = "akf_hrms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "akf_hrms.utils.before_app_uninstall"
# after_app_uninstall = "akf_hrms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "akf_hrms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
    # "ToDo": "custom_app.overrides.CustomToDo",
    # "Attendance": "akf_hrms.overrides.attendance.Attendance",
    # "Attendance Request": "akf_hrms.overrides.attendance_request.AttendanceRequest",
    "Employee Onboarding": "akf_hrms.overrides.employee_onboarding.EmployeeOnboarding",
    "Employee Separation": "akf_hrms.overrides.employee_separation.EmployeeSeparation",
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "*": {
        # 		"on_update": "method",
        # 		"on_cancel": "method",
        # 		"on_trash": "method"
    },
    "Employee Onboarding": {
        "before_submit": "akf_hrms.overrides.submit_on_completed.submit_on_complete"
    },
    "Employee Separation": {
        "before_submit": "akf_hrms.overrides.submit_on_completed.submit_on_complete"
    },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"akf_hrms.tasks.all"
# 	],
# 	"daily": [
# 		"akf_hrms.tasks.daily"
# 	],
# 	"hourly": [
# 		"akf_hrms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"akf_hrms.tasks.weekly"
# 	],
# 	"monthly": [
# 		"akf_hrms.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "akf_hrms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "akf_hrms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "akf_hrms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["akf_hrms.utils.before_request"]
# after_request = ["akf_hrms.utils.after_request"]

# Job Events
# ----------
# before_job = ["akf_hrms.utils.before_job"]
# after_job = ["akf_hrms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"akf_hrms.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# fixtures = ["Custom Field"]
