#!/usr/bin/env python3

import mechanicalsoup


browser = mechanicalsoup.StatefulBrowser()
browser.open("http://jkorpela.fi/forms/testing.html")
browser.select_form('form[action="http://jkorpela.fi/cgi-bin/echo.cgi"]').print_summary()
browser["Comments"] = "12341234"
browser["hidden field"] = "test"
browser["box"] = "yes"
#browser.launch_browser()
response = browser.submit_selected()
#print(response.text)
browser.launch_browser()