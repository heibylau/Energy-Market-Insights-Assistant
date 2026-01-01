GJ_PER_MMBTU = 1 / 0.9482133
MMBTU_PER_GJ = 0.9482133

def can_to_us(price_cad: float, exchange_rate: float) -> float:
    '''
    Converts from CAD/GJ to USD/MMBtu
    Parameters: 
        price_cad: price in CAD per gigajoule
        exchange_rate: the exchange rate from CAD to USD
    '''
    usd = price_cad * exchange_rate
    usd_per_MMBTU = usd * GJ_PER_MMBTU
    return usd_per_MMBTU

def us_to_can(price_usd: float, exchange_rate: float) -> float:
    '''
    Converts from USD/MMBtu to CAD/GJ
    Parameters: 
        price_usd: price in USD per million British thermal units
        exchange_rate: the exchange rate from USD to CAD
    '''
    cad = price_usd * exchange_rate
    cad_per_gj = cad * MMBTU_PER_GJ
    return cad_per_gj