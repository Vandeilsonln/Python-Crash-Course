import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('./Project_2-Data_Visualization/exercises/_images/na_populations.svg')