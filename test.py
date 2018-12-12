# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:56:17 2018

@author: david
"""

def is_number(s) -> bool:
    """
    Tests if the value passed is a number.
    Returns True or False.
    """
    if isinstance(s, str):
        s = s.strip()
        return s.isnumeric()
    return isinstance(s, int) or isinstance(s, float)

def input_number():
    """
    Asks the user to enter a number.
    Validates the input and returns the given number.
    """
    while True:
        number = input()
        if is_number(number):
            number = int(number)
            break
    return number

def get_league():
    # List of available leagues
    league_list = [("England", "Premier-League-2018-2019"),("England", "Championship-League-2018-2019")]
    
    # enumerated list
    numbered_league_list = list(enumerate(league_list,1))
    
    # list of available options
    available_leagues = []
    
    # populate the list of available options
    for league in numbered_league_list:
        available_leagues.append(league[0])
        
    league_sel = ""
    
    while league_sel not in available_leagues:
        for league in numbered_league_list:
            print(league[0], league[1], sep="\t")
        print("\nPlease enter a number for one of the above leagues")
        league_sel = input_number()
    
    return league_list[league_sel-1]

print(get_league())
