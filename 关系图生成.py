import csv
import math
from pyecharts import options as opts
from pyecharts.charts import Graph

# Load the interaction data
csv_file_path = '人物关系数据.csv'
character_data = []

with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header
    for row in reader:
        char1, char2, frequency = row
        character_data.append(((char1, char2), int(frequency)))

# Load character appearance data
appearance_csv_file_path = '人物出现次数.csv'
character_frequencies = {}

with open(appearance_csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header
    for row in reader:
        character, count = row
        character_frequencies[character] = int(count)

# Define a base size for all nodes
base_size = 50  # Basic size for all nodes
size_variation = 40  # Maximum additional size based on frequency

# Calculate the maximum frequency for scaling node sizes
max_char_freq = max(character_frequencies.values())

# Calculate link thickness based on frequency
max_freq = max(freq for ((_, _), freq) in character_data)
min_thickness = 2  # Minimum thickness of the links
max_thickness = 20  # Maximum thickness of the links

# Define nodes and links
# Define nodes with slightly varying sizes based on appearance counts
nodes = [{
    "name": name,
    "symbolSize": base_size + (character_frequencies[name] / max_char_freq) * size_variation,
    "itemStyle": {"normal": {"color": "#9A755A"}}
} for name in character_frequencies]

links = [{
    "source": char1,
    "target": char2,
    "value": freq,
    "lineStyle": {
        "normal": {
            "width": min_thickness + (freq / max_freq) * (max_thickness - min_thickness),
            "color": "#e4d3b9"
        }
    }
} for (char1, char2), freq in character_data]

# Create and render the graph
c = (
    Graph()
    .add("", nodes, links, repulsion=10000)
    .set_global_opts(title_opts=opts.TitleOpts(title = " "))
    .render("character_interaction_network.html")
)



