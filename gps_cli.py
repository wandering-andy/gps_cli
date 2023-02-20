"""
Python gpsd cli
https://github.com/MartijnBraam/gpsd-py3
"""

import click
import gpsd


@click.command()
@click.option('--format', type=click.Choice(['DMS','DD','DMM'], case_sensitive=False),
              default='DD', help='format of GPS coordinates')
@click.option('--units', type=click.Choice(['ft','m'], case_sensitive=False),
              default='ft', help='units used for altitude')
@click.option('--datum', default='WGS84', help='datum to display lat/long')
def print_gps():
    echo (lat, long, alt)

def convert_metertofeet(meter):
    feet = meter * 3.281
    return (feet)


def convert_DDtoDMS():
    return ()


def convert_DDtoDMM():
    return ()

# Tried following this code with no luck. gps isn't a part of gpsd like they says it is.
# https://gpsd.gitlab.io/gpsd/gpsd-client-example-code.html#_example_2python
# session = gps.gps(mode=gps.WATCH_ENABLE)
# #Keep trying to read the session until there is a fix
# try:
#     while 0 == session.read():
#         if not (gps.MODE_SET & session.valid):
#             #not use, probably not a valid TPV message
#             continue

# Delete below once they actually get used.
gpsd.connect()
