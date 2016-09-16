form = """
	<form method="POST">
		What is your birthday
		<br />
		<label for="month">Month</label> <input type="text" name="month" value='%(month)'/>
		<label for="Day">Day</label> <input type="text" name="Day" value='%(day)'/>
		<label for="Year">Year</label> <input type="text" name="Year" value='%(year)'/>
		<div>%(error)s</div>
		<br/>
		<br/>
		<input type="submit"/>
	</form>
"""

class MainPage(webapp2.RequestHandler):
	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form % {"error" : error, 
										"month": escape_html(month),
										"day":escape_html(day),
										"year":escape_html(year)})

	def get(self):
		self.write_form()

	def post(self):
		user_month = self.request.get("month")
		user_day = self.request.get("day")
		user_year = self.request.get("year")

		month = valid_month(user_month)
		day = valid_day(user_day)
		yaer = valid_year(user_year)

		if not (month and day and year):
			self.write_form("That doesn't look valid to me, friend.", user_month, user_day, user_year)
		else:
			self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks!")

app = webapp2.WSGIApplication([
	('/', MainPage),
	("/thanks", ThanksHandler)

	], debug=True)