from PIL import Image
from utils.data import extrait_donnees

def get_color(value, minval, maxval):

    normalized_value = (value - minval) / (maxval - minval)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    red = (255, 0, 0)

    if normalized_value <= 0.5:

        factor = normalized_value / 0.5
        color = (
            int(blue[0] + factor * (white[0] - blue[0])),
            int(blue[1] + factor * (white[1] - blue[1])),
            int(blue[2] + factor * (white[2] - blue[2]))
        )
    else:

        factor = (normalized_value - 0.5) / 0.5
        color = (
            int(white[0] + factor * (red[0] - white[0])),
            int(white[1] + factor * (red[1] - white[1])),
            int(white[2] + factor * (red[2] - white[2]))
        )

    return color


data = extrait_donnees('data/156250-TAVG-Data.csv', separator=",")

yearly_sum = {}
yearly_count = {}

for record in data:
    year = record['Year']
    temperature = record['Temperature']
    
    if temperature != 'NaN':
        temp_value = float(temperature)
        
        if year not in yearly_sum:
            yearly_sum[year] = {'Temperature': 0.0}
            yearly_count[year] = 0
        
        yearly_sum[year]['Temperature'] += temp_value
        yearly_count[year] += 1

yearly_averages = []
for year in yearly_sum:
    if yearly_count[year] > 0:
        avg_temperature = yearly_sum[year]['Temperature'] / yearly_count[year]
        yearly_averages.append({
            'Year': int(year),
            'Average Temperature': avg_temperature
        })

yearly_averages.sort(key=lambda x: x['Year'])


v20_years_temp_sum = 0

interval = (1940, 1960)
for entry in yearly_averages:
    if interval[0] < entry["Year"] <= interval[1]:
        v20_years_temp_sum += entry['Average Temperature']

v20_years_temp_avr = v20_years_temp_sum / 20
#print(v20_years_temp_avr)
v20_years_temp_avr = float(f"{v20_years_temp_avr:.3f}")
#print(v20_years_temp_avr)

anomalies = [float(f"{(entry["Average Temperature"] - v20_years_temp_avr):.3f}") for entry in yearly_averages]

colors = [get_color(val, min(anomalies), max(anomalies)) for val in anomalies]



image = Image.new('RGB', (len(colors)*5, 200))

for x in range(len(colors)*5):
    for y in range(200):
        image.putpixel((x, y), colors[x//5])

image.show()