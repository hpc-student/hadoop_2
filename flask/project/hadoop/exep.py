@app.errorhandler(2)
def page_not_found(error):
	app.logger.error('Page not found: %s', (request.path))
return render_template('404.htm'), 2
