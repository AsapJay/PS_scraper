'''
Created on Dec 2, 2016

@author: JR
'''
from PSStoreScraper import PSStoreScraper
from DealChecker import DealChecker
from DealEmailer import DealEmailer


class ScraperMain(object):
    
    def main(self):
        
        game_list = ['Call of Duty' , 'Dungeon Defenders' , 'dead rising' , 'destiny' ]
        output_file = "playstation_deals.txt"
        scraper = PSStoreScraper()
        scraper.scrape_site(output_file)
        dealcheck = DealChecker(output_file)
        dealcheck.set_game_list(game_list)
        match_list = dealcheck.return_matches()
        deal_email = DealEmailer("")
        deal_email.send_matches(match_list)
        
#         for match in match_list:
#             print(match)
        
    
    

if __name__ == '__main__':
    scraper = ScraperMain()
    scraper.main()
    


