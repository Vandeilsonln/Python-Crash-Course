from os import chdir
import json
import pygal
from pygal.style import RotateStyle, LightColorizedStyle
from country_codes import get_country_code

# Set CWD
chdir('./Project_2-Data_Visualization/exercises')

# Load the data into a list

filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}

# Print the 2010 population for each country.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop

wm_style = RotateStyle('#3366bb', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops1)
wm.add('10m-1bn', cc_pops2)
wm.add('>1bn', cc_pops3)

wm.render_to_file('./_images/world_population.svg')
