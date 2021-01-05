import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central Ametrica', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('./Project_2-Data_Visualization/exercises/_images/americas.svg')