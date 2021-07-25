"""
	This file defines regular expression patterns, which are matched to
	input queries.
"""

import re


def cases(scraper, region: str="world") -> str:
	return scraper.get_total_cases_region(region)

def deaths(scraper, region: str="world") -> str:
	return scraper.get_total_deaths_region(region)

def recoveries(scraper, region: str="world") -> str:
	return scraper.get_total_recoveries_region(region)

def active(scraper, region: str="world") -> str:
	return scraper.get_total_active_region(region)


REGION_PATTERNS = {

	# Total cases in a region.
	re.compile("[\w\s]+ cases"): cases,
	re.compile("cases [\w\s]+"): cases,
	re.compile("[\w\s]+ cases [\w\s]"): cases,

	# Deaths.
	re.compile("[\w\s]+ deaths"): deaths,
	re.compile("deaths+ [\w\s]"): deaths,
	re.compile("[\w\s]+ deaths [\w\s]+"): deaths,
	re.compile("[\w\s]+ died"): deaths,
	re.compile("died [\w\s]+"): deaths,
	re.compile("[\w\s]+ died [\w\s]+"): deaths,

	# Recoveries.
	re.compile("[\w\s]+ recoveries"): recoveries,
	re.compile("recoveries [\w\s]+"): recoveries,
	re.compile("[\w\s]+ recoveries [\w\s]+"): recoveries,
	re.compile("[\w\s]+ recovered"): recoveries,
	re.compile("recovered [\w\s]+"): recoveries,
	re.compile("[\w\s]+ recovered [\w\s]+"): recoveries,

	# Active cases.
	re.compile("[\w\s]+ active"): active,
	re.compile("active [\w\s]+"): active,
	re.compile("[\w\s]+ active [\w\s]+"): active,

}


TOTAL_PATTERNS = {

	# Total worldwide cases.
	re.compile("total cases"): cases,
	re.compile("cases [\w\s]+"): cases,
	re.compile("[\w\s]+ cases"): cases,
	re.compile("[\w\s]+ cases [\w\s]"): cases,
	re.compile("[\w\s]+ worldwide"): cases,
	re.compile("worldwide [\w\s]+"): cases,
	re.compile("[\w\s]+ worldwide [\w\s]+"): cases,

	# Total deaths.
	re.compile("total deaths"): deaths,
	re.compile("[\w\s]+ deaths"): deaths,
	re.compile("deaths [\w\s]+"): deaths,
	re.compile("[\w\s]+ deaths [\w\s]+"): deaths,
	re.compile("[\w\s]+ died"): deaths,
	re.compile("died [\w\s]+"): deaths,
	re.compile("[\w\s]+ died [\w\s]+"): deaths,

	# Total recoveries.
	re.compile("total recoveries"): recoveries,
	re.compile("total recovered"): recoveries,
	re.compile("[\w\s]+ recoveries"): recoveries,
	re.compile("recoveries [\w\s]+"): recoveries,
	re.compile("[\w\s]+ recoveries [\w\s]+"): recoveries,
	re.compile("[\w\s]+ recovered"): recoveries,
	re.compile("recovered [\w\s]+"): recoveries,
	re.compile("[\w\s]+ recovered [\w\s]+"): recoveries,

	# Total active cases.
	re.compile("total active"): active,
	re.compile("[\w\s]+ active"): active,
	re.compile("active [\w\s]+"): active,
	re.compile("[\w\s]+ active [\w\s]+"): active,

}


# For terminating the program.
EXIT_PATTERNS = {

	re.compile("stop"),
	re.compile("[\w\s]+ stop"),
	re.compile("stop [\w\s]+"),
	re.compile("[\w\s]+ stop [\w\s]+"),

	re.compile("exit"),
	re.compile("[\w\s]+ exit"),
	re.compile("exit [\w\s]+"),
	re.compile("[\w\s]+ exit [\w\s]+"),

	re.compile("quit"),
	re.compile("[\w\s]+ quit"),
	re.compile("quit [\w\s]+"),
	re.compile("[\w\s]+ quit [\w\s]+"),

	re.compile("terminate"),
	re.compile("[\w\s]+ terminate"),
	re.compile("terminate [\w\s]+"),
	re.compile("[\w\s]+ terminate [\w\s]+")

}