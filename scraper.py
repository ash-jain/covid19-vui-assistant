from bs4 import BeautifulSoup
import requests

class Scraper:

    def __init__(self):
        self.data = {}
        self._html_file = self.make_request()
        self.scraper = BeautifulSoup(self._html_file, 'lxml')
        self.set_data()


    def set_data(self) -> None:

        table = [row.select("td") for row in self.scraper.select("#main_table_countries_today > tbody:first-of-type > tr")]
        for row in table:
            if not row:
                continue
            # { region : [total cases, total deaths, total recovered, total active] }
            try:
                self.data.update({ row[1].get_text(strip=True).lower() : [ row[2].get_text(strip=True), row[4].get_text(strip=True), row[6].get_text(strip=True), row[8].get_text(strip=True) ] })
            except:
                continue

        # Fallback if total data can't be scraped accurately.
        if self.data['world'] is None:
            main_counter_wrap = self.scraper.select("#maincounter-wrap")
            self.data['world'][0] = main_counter_wrap[0].div.span.get_text(strip=True)
            self.data['world'][1] = main_counter_wrap[1].div.span.get_text(strip=True)
            self.data['world'][2] = main_counter_wrap[2].div.span.get_text(strip=True)
            self.data['world'][3] = self.scraper.select("#panel_active .number-table-main")[0].get_text(strip=True)


    def update_data(self) -> str:
        
        current_total = self.data['world'][0]

        new_html = self.make_request()
        bs = BeautifulSoup(new_html, 'lxml')
        new_total = bs.select("#maincounter-wrap")[0].div.span.text

        if new_total != current_total:
            self.html = new_html
            self.set_all()
            return "The data is being updated."
        else:
            return "The data is up to date."


    def make_request(self) -> str:
        response = requests.get("https://worldometers.info/coronavirus")

        if response.status_code != 200:
            raise Exception(f"No response from the server, make sure you have proper internet connection! \nProgram ended with status code {response.status_code}")

        return response.text


    def get_total_cases_region(self, region) -> str:
        return f"Total cases in {region.title()} are {self.data[region][0]}.\n"


    def get_total_deaths_region(self, region) -> str:
        return f"Total deaths in {region.title()} are {self.data[region][1]}.\n"


    def get_total_recoveries_region(self, region) -> str:
        return f"Total patients recovered in {region.title()} are {self.data[region][2]}.\n"


    def get_total_active_region(self, region) -> str:
        return f"Total active cases in {region.title()} are {self.data[region][3]}.\n"


    def get_regions(self) -> str:
        return list(self.data)


    def __str__(self) -> str:
        obj = ""
        for key, val in self.data.items():
            obj += key.title() + ":\nTotal cases: " + val[0] + "\nTotal deaths: " + val[1] + "\nTotal recoveries: " + val[2] + "\nTotal active: " + val[3] + "\n\n"
        return obj

        #TODO one-liner.
    
    # For debugging
    def print_data(self) -> None:
        print(self.data)


if __name__ == "__main__":

    sc = Scraper()
    print(sc)

