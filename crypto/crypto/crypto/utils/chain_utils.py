
import re

from crypto.models.chains_model import *

def format_chain(url_image):
    bnb = 'https://assets.coingecko.com/coins/images/825/small/bnb-icon2_2x.png?1644979850'
    
    if(url_image == bnb):
        return chains.bnb
    else:
        return chains.unknown
    
    