# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def star_names():
    for i in targets:
        print(i)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def name_and_type():
    for star, info in targets.items():
        print(f"{star}: {info['Spectral Type']}")
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def stars_mag():
    for star, info in targets.items():
        if info['Magnitude'] > 0.1:
            print(f"{star} has magnitude {info['Magnitude']}")
# 4) Look up another target, add all the necessary information to the targets list. 
targets["Deneb"] = {
    "RA": "20h 41m 25.9s",
    "Dec": "+45° 16′ 49″",
    "Magnitude": 1.25,
    "Spectral Type": "A2Ia"
}
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def dec_to_deg(dec_str):
    dec_str = dec_str.replace("−", "-").replace("+", "")  
    deg = int(dec_str.split("°")[0])
    return deg

def brightest_near_20():
    closest_star = None
    closest_diff = 1000
    for star, info in targets.items():
        dec_deg = dec_to_deg(info["Dec"])
        diff = abs(dec_deg - 20)
        if diff < closest_diff:
            closest_diff = diff
            closest_star = star
    print(f"Brightest star near 20° declination is: {closest_star}")

# 6) What is your favorite constellation?
#My favorite constellation is Taurus

star_names()
name_and_type()
stars_mag()
brightest_near_20()

