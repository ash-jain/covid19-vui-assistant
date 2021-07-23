"""
	This file defines regular expression patterns, which are matched to input queries.
"""

import re
from scraper import Scraper


sc = Scraper()

INPUT_PATTERNS = {

	# Total cases in a region.

	re.compile("[\w\s]+ total cases"): lambda region: sc.get_total_cases_region(region),
	re.compile("total cases [\w\s]+"): lambda region: sc.get_total_cases_region(region),
	re.compile("total [\w\s]+ cases"): lambda region: sc.get_total_cases_region(region),
	re.compile("[\w\s]+ total cases [\w\s]+"): lambda region: sc.get_total_cases_region(region),
	re.compile("[\w\s]+ total [\w\s]+ cases"): lambda region: sc.get_total_cases_region(region),
	re.compile("total [\w\s]+ cases [\w\s]+"): lambda region: sc.get_total_cases_region(region),
	re.compile("[\w\s]+ total [\w\s]+ cases [\w\s]+"): lambda region: sc.get_total_cases_region(region),


	# Deaths.

	re.compile("[\w\s]+ deaths"): lambda region: sc.get_total_deaths_region(region),
	re.compile("deaths+ [\w\s]"): lambda region: sc.get_total_deaths_region(region),
	re.compile("[\w\s]+ deaths [\w\s]+"): lambda region: sc.get_total_deaths_region(region),

	re.compile("[\w\s]+ total deaths"): lambda region: sc.get_total_deaths_region(region),
	re.compile("total deaths [\w\s]+"): lambda region: sc.get_total_deaths_region(region),
	re.compile("total [\w\s]+ deaths"): lambda region: sc.get_total_deaths_region(region),
	re.compile("[\w\s]+ total deaths [\w\s]+"): lambda region: sc.get_total_deaths_region(region),
	re.compile("[\w\s]+ total [\w\s]+ deaths"): lambda region: sc.get_total_deaths_region(region),
	re.compile("total [\w\s]+ deaths [\w\s]+"): lambda region: sc.get_total_deaths_region(region),
	re.compile("[\w\s]+ total [\w\s]+ deaths [\w\s]+"): lambda region: sc.get_total_deaths_region(region),

	re.compile("[\w\s]+ died"): lambda region: sc.get_total_deaths_region(region),
	re.compile("died [\w\s]+"): lambda region: sc.get_total_deaths_region(region),
	re.compile("[\w\s]+ died [\w\s]+"): lambda region: sc.get_total_deaths_region(region),


	# Recoveries.

	re.compile("[\w\s]+ recoveries"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("recoveries [\w\s]+"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("[\w\s]+ recoveries [\w\s]+"): lambda region: sc.get_total_recoveries_region(region),

	re.compile("[\w\s]+ recovered"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("recovered [\w\s]+"): lambda region: sc.get_total_recoveries_region(region),        
	re.compile("[\w\s]+ recovered [\w\s]+"): lambda region: sc.get_region_total_recovered(region),

	re.compile("[\w\s]+ total recoveries"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("total recoveries [\w\s]+"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("total [\w\s]+ recoveries"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("[\w\s]+ total recoveries [\w\s]+"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("[\w\s]+ total [\w\s]+ recoveries"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("total [\w\s]+ recoveries [\w\s]+"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("[\w\s]+ total [\w\s]+ recoveries [\w\s]+"): lambda region: sc.get_total_recoveries_region(region),

	re.compile("[\w\s]+ total recovered"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("total recovered [\w\s]+"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("total [\w\s]+ recovered"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("[\w\s]+ total recovered [\w\s]+"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("[\w\s]+ total [\w\s]+ recovered"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("total [\w\s]+ recovered [\w\s]+"): lambda region: sc.get_total_recoveries_region(region),
	re.compile("[\w\s]+ total [\w\s]+ recovered [\w\s]+"): lambda region: sc.get_total_recoveries_region(region),


	# Active cases.

	re.compile("[\w\s]+ active cases"): lambda region: sc.get_total_active_region(region),
	re.compile("active cases [\w\s]+"): lambda region: sc.get_total_active_region(region),
	re.compile("active [\w\s]+ cases"): lambda region: sc.get_total_active_region(region),
	re.compile("[\w\s]+ active cases [\w\s]+"): lambda region: sc.get_total_active_region(region),
	re.compile("[\w\s]+ active [\w\s]+ cases"): lambda region: sc.get_total_active_region(region),
	re.compile("active [\w\s]+ cases [\w\s]+"): lambda region: sc.get_total_active_region(region),
	re.compile("[\w\s]+ active [\w\s]+ cases [\w\s]+"): lambda region: sc.get_total_active_region(region),


	# Total worldwide cases.

	re.compile("total cases"): sc.get_total_cases_region('world'),

	re.compile("cases worldwide"): sc.get_total_cases_region('world'),
	re.compile("[\w\s]+ cases worldwide"): sc.get_total_cases_region('world'),
	re.compile("cases worldwide [\w\s]+"): sc.get_total_cases_region('world'),
	re.compile("cases [\w\s]+ worldwide"): sc.get_total_cases_region('world'),
	re.compile("[\w\s]+ cases worldwide [\w\s]+"): sc.get_total_cases_region('world'),
	re.compile("[\w\s]+ cases [\w\s]+ worldwide"): sc.get_total_cases_region('world'),
	re.compile("cases [\w\s]+ worldwide [\w\s]+"): sc.get_total_cases_region('world'),
	re.compile("[\w\s]+ cases [\w\s]+ worldwide [\w\s]+"): sc.get_total_cases_region('world'),
	
	re.compile("cases world"): sc.get_total_cases_region('world'),
	re.compile("[\w\s]+ cases world"): sc.get_total_cases_region('world'),
	re.compile("cases world [\w\s]+"): sc.get_total_cases_region('world'),
	re.compile("cases [\w\s]+ world"): sc.get_total_cases_region('world'),
	re.compile("[\w\s]+ cases world [\w\s]+"): sc.get_total_cases_region('world'),
	re.compile("[\w\s]+ cases [\w\s]+ world"): sc.get_total_cases_region('world'),
	re.compile("cases [\w\s]+ world [\w\s]+"): sc.get_total_cases_region('world'),
	re.compile("[\w\s]+ cases [\w\s]+ world [\w\s]+"): sc.get_total_cases_region('world'),       


	# Total deaths.

	re.compile("[\w\s]+ deaths"): sc.get_total_deaths_region('world'),
	re.compile("deaths [\w\s]+"): sc.get_total_deaths_region('world'),
	re.compile("[\w\s]+ deaths [\w\s]+"): sc.get_total_deaths_region('world'),

	re.compile("total deaths"): sc.get_total_deaths_region('world'),
	re.compile("[\w\s]+ total deaths"): sc.get_total_deaths_region('world'),
	re.compile("total deaths [\w\s]+"): sc.get_total_deaths_region('world'),
	re.compile("total [\w\s]+ deaths"): sc.get_total_deaths_region('world'),
	re.compile("[\w\s]+ total deaths [\w\s]+"): sc.get_total_deaths_region('world'),
	re.compile("[\w\s]+ total [\w\s]+ deaths"): sc.get_total_deaths_region('world'),
	re.compile("total [\w\s]+ deaths [\w\s]+"): sc.get_total_deaths_region('world'),
	re.compile("[\w\s]+ total [\w\s]+ deaths [\w\s]+"): sc.get_total_deaths_region('world'),

	re.compile("[\w\s]+ died"): sc.get_total_deaths_region('world'),
	re.compile("died [\w\s]+"): sc.get_total_deaths_region('world'),
	re.compile("[\w\s]+ died [\w\s]+"): sc.get_total_deaths_region('world'),


	# Total recoveries.

	re.compile("total recoveries"): sc.get_total_recoveries_region('world'),
	re.compile("[\w\s]+ total recoveries"): sc.get_total_recoveries_region('world'),
	re.compile("total recoveries [\w\s]+"): sc.get_total_recoveries_region('world'),
	re.compile("total [\w\s]+ recoveries"): sc.get_total_recoveries_region('world'),
	re.compile("[\w\s]+ total recoveries [\w\s]+"): sc.get_total_recoveries_region('world'),
	re.compile("[\w\s]+ total [\w\s]+ recoveries"): sc.get_total_recoveries_region('world'),
	re.compile("total [\w\s]+ recoveries [\w\s]+"): sc.get_total_recoveries_region('world'),
	re.compile("[\w\s]+ total [\w\s]+ recoveries [\w\s]+"): sc.get_total_recoveries_region('world'),

	re.compile("total recovered"): sc.get_total_recoveries_region('world'),
	re.compile("[\w\s]+ total recovered"): sc.get_total_recoveries_region('world'),
	re.compile("total recovered [\w\s]+"): sc.get_total_recoveries_region('world'),
	re.compile("total [\w\s]+ recovered"): sc.get_total_recoveries_region('world'),
	re.compile("[\w\s]+ total recovered [\w\s]+"): sc.get_total_recoveries_region('world'),
	re.compile("[\w\s]+ total [\w\s]+ recovered"): sc.get_total_recoveries_region('world'),
	re.compile("total [\w\s]+ recovered [\w\s]+"): sc.get_total_recoveries_region('world'),
	re.compile("[\w\s]+ total [\w\s]+ recovered [\w\s]+"): sc.get_total_recoveries_region('world'),


	# Total active cases.

	re.compile("active cases"): sc.get_total_active_region('world'),
	re.compile("total active"): sc.get_total_active_region('world'),
	re.compile("[\w\s]+ total active"): sc.get_total_active_region('world'),
	re.compile("total cases [\w\s]+"): sc.get_total_active_region('world'),
	re.compile("total [\w\s]+ cases"): sc.get_total_active_region('world'),
	re.compile("[\w\s]+ total cases [\w\s]+"): sc.get_total_active_region('world'),
	re.compile("[\w\s]+ total [\w\s]+ cases"): sc.get_total_active_region('world'),
	re.compile("total [\w\s]+ cases [\w\s]+"): sc.get_total_active_region('world'),
	re.compile("[\w\s]+ total [\w\s]+ cases [\w\s]+"): sc.get_total_active_region('world'),


	re.compile("cases [\w\s]+"): lambda region: sc.get_total_cases_region(region),
	re.compile("[\w\s]+ cases"): lambda region: sc.get_total_cases_region(region),
	re.compile("[\w\s]+ cases [\w\s]"): lambda region: sc.get_total_cases_region(region),

}


# For terminating the program.
EXIT_PATTERNS = {
	re.compile("stop"): exit,
	re.compile("[\w\s]+ stop"): exit,
	re.compile("stop [\w\s]+"): exit,
	re.compile("[\w\s]+ stop [\w\s]+"): exit,

	re.compile("exit"): exit,
	re.compile("[\w\s]+ exit"): exit,
	re.compile("exit [\w\s]+"): exit,
	re.compile("[\w\s]+ exit [\w\s]+"): exit,

	re.compile("quit"): exit,
	re.compile("[\w\s]+ quit"): exit,
	re.compile("quit [\w\s]+"): exit,
	re.compile("[\w\s]+ quit [\w\s]+"): exit,

	re.compile("terminate"): exit,
	re.compile("[\w\s]+ terminate"): exit,
	re.compile("terminate [\w\s]+"): exit,
	re.compile("[\w\s]+ terminate [\w\s]+"): exit
}