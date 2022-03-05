

def format_chain(raw_img_url):
    img_url = str(raw_img_url).split('/')[-1]
    
    # Chain list
    bnb   = 'bnb-icon2_2x.png?1644979850'
    eth   = 'ethereum.png?1595348880'
    sol   = 'solana.png?1640133422'
    fan   = 'Fantom.png?1558015016'
    matic = 'matic-token-icon.png?1624446912'
    avax  = 'coin-round-red.png?1604021818'
    cro   = 'oCw2s3GI_400x400.jpeg?1645172042'
    polis = 'circlePolisLogo.png?1573787189'
    
    
    if(img_url == bnb):
        return 'bnb'
    
    elif(img_url == eth):
        return 'eth'
    
    elif(img_url == sol):
        return 'sol'
    
    elif(img_url == fan):
        return 'fan'
    
    elif(img_url == matic):
        return 'matic'
    
    elif(img_url == avax):
        return 'avax'
    
    elif(img_url == cro):
        return 'cro'
    
    elif(img_url == polis):
        return 'polis'

    else:
        return raw_img_url
    
    