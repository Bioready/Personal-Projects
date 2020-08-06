# IMPORT MODULES
from __future__ import print_function
import gspread
import pandas as pd


googleaccount = gspread.service_account(filename='credentials.json')
googlesheet = googleaccount.open_by_key('1DKWj1mHuLp453tzbcTfWpvEkUfGp_VzgCsmcQl0gBw8')
RedWines = googlesheet.worksheet("Red Wine")
WhiteWines = googlesheet.worksheet("White Wine")

RedsDF = pd.DataFrame(RedWines.get_all_records())
WhitesDF = pd.DataFrame(WhiteWines.get_all_records())


def SelectRandomWine(**kwargs):
    selection = input("Red or White?     ")
    if selection == 'red':
        randomredwine = RedsDF.sample(n=1)
        print(randomredwine)
    if selection == 'white':
        randomwhitewine = WhitesDF.sample(n=1)
        print(randomwhitewine)
    else:
        print("Invalid input.  Please select 'red' or 'white' (case sensitive)")


SelectRandomWine()
