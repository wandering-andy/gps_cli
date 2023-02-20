"""
Python gpsd cli
https://github.com/MartijnBraam/gpsd-py3
"""
import math
import click
import gpsd

# TODO error catching around this
try:
    gpsd.connect()
except:
    print("An error occurred while trying to connect.")

# TODO error catching around this
err = 0
location = gpsd.get_current()
if location.mode >= 2:
    lat = location.lat
    lon = location.lon
    print("Unable to determine altitude.")
elif location.mode < 2:
    err = err++
    if err > 5:
        print("Could not obtain satellite fix.")
        exit()
else:
    lat = location.lat
    lon = location.lon
    alt = location.alt

def convert_meters_to_feet():
    '''this is a docstring'''
    feet = alt * 3.281
    return feet

def convert_dd_to_dms(dd):
    '''this is a docstring'''
    degrees = int(dd)
    minutes = int((dd - degrees) * 60)
    seconds = (dd - degrees - minutes / 60) * 3600
    return degrees, minutes, seconds

def convert_dd_to_ddm(dd):
    '''this is a docstring'''
    degrees = int(dd)
    minutes = (dd - degrees) * 60.0
    return degrees, minutes

@click.command()
@click.option('--format', type=click.Choice(['DMS','DD','DMM'], case_sensitive=False),
              default='DD', show_default=True, help='format of GPS coordinates')
@click.option('--units', type=click.Choice(['ft','m'], case_sensitive=False),
              default='ft', show_default=True, help='units used for altitude')
@click.option('--pretty', is_flag=True, help='print output in a pretty format')
def print_gps(format, units, pretty):
    '''this is a docstring'''
    if format == 'DDM':
        lat = convert_dd_to_ddm(lat)
        lon = convert_dd_to_ddm(lon)
    elif format == 'DMS':
        lat = convert_dd_to_dms(lat)
        lon = convert_dd_to_dms(lon)
    else:
        # TODO not really sure what should go here. Maybe not necessary?
    if units == 'ft':
        alt = convert_meters_to_feet(alt)
    else:
        # TODO not really sure what should go here. I guess since there's only two options
        # it's really just a flag and should be rewritten like the pretty option 
    # TODO Need to change formatting based on GPS format
    if pretty:
        click.echo("Latitude: {}° {}' {}\"".format(*lat_dms))
        click.echo("Longitude: {}° {}' {}\"".format(*lon_dms))
        click.echo("Altitude: "+alt)
