'''
Created on Dec 1, 2016

@author: JR
'''

class DealChecker(object):
    def __init__(self , dealFile):
        self.dealFile = dealFile
        self.game_list = None
        pass
    
    def set_game_list(self , game_list):
        self.game_list = game_list
        self.__convert_matches_to_lower()
        
    def return_matches(self):
        if self.game_list is None:
            return []
        matches = []
        file = open(self.dealFile , 'r')
        for line in file:
            for game in self.game_list:
                if game in line:
                    matches.append(line)
        return matches
    
    def __convert_matches_to_lower(self):
        self.game_list = [str(x).lower() for x in self.game_list]
        
            

if __name__ == '__main__':
    instance = DealChecker('playstation_deals.txt')
    games = ['Call Of Duty' , 'BattleField']
    instance.set_game_list(games)
    for games in instance.game_list:
        print(games)
     
            
    
    
