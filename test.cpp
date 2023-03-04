import sentinelhub

# pass the credentials directly to the sentinelhub.Session constructor
from sentinelhub import SHConfig, SentinelHubError

config = SHConfig()

try:
    config.sh_client_id = '<your_client_id>'
    config.sh_client_secret = '<your_client_secret>'
except SentinelHubError as e:
    print("Failed to set up Sentinel Hub configuration: {}".format(e))

# Create a sentinelhub.DataSource object with the data you need
from sentinelhub import DataSource
# Create a DataSource object for Sentinel-2 Level-1C data
data_source = DataSource('S2L1C')

# Request the data using the sentinelhub.DataCollection object and the sentinelhub.filters module to specify the geographical area, date range, and other filters.
from sentinelhub import DataCollection, bbox, CRS, SentinelHubRequest, WcsRequest, MimeType

# Define the bounding box for the area of interest
bbox = bbox.BBox(bbox=[-118.475, 33.775, -118.215, 34.125], crs=CRS.WGS84)

# Define the time range for the data
time_interval = ('2021-01-01', '2021-03-01')

# Create a SentinelHubRequest object to download the data
request = SentinelHubRequest(
    data_source=data_source,
    data_folder='data_folder',
    bbox=bbox,
    time=time_interval,
    data_collection=DataCollection.SENTINEL2_L1C,
    additional_data=[],
    resolution='10m',
    maxcc=0.5,
    config=config
)

