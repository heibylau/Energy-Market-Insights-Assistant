from datetime import datetime
from units import can_to_us, us_to_can
import requests

def label_price(df):
    df = df.copy()

    df["price_type"] = df["year"].apply(
        lambda y: "historical" if y <= 2025 else "forecast"
    )

    return df

def prepare_prices(df, unit_choice):
    url = "https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json"
    response = requests.get(url).json()

    latest = response["observations"][-1]
    usd_to_cad = float(latest["FXUSDCAD"]["v"])
    cad_to_usd = 1 / usd_to_cad
    print(usd_to_cad)

    df = df.copy()

    if unit_choice == "USD/MMBtu":
        df["display_price"] = df.apply(
            lambda x:
                can_to_us(x["price"], cad_to_usd)
                if x["unit"] == "CAD/GJ"
                else x["price"],
            axis=1
        )
    else:
        df["display_price"] = df.apply(
            lambda x:
                us_to_can(x["price"], usd_to_cad)
                if x["unit"] == "USD/MMBtu"
                else x["price"],
            axis=1
        )

    return df