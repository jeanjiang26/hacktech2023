# contain code to access the SentinelHub API and download satellite imagery data for the area of interest
# use the SentinelHub Python package to access the API and download the data

# specifically for los angeles
# from sentinelhub import *
# import sentinelhub
from sentinelhub import MimeType
from sentinelhub import SentinelHubRequest, DataCollection, bbox_to_dimensions, BBox, CRS

# Define your SentinelHub API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Define the bounding box for Los Angeles
bbox = BBox(bbox=[-118.6682, 33.7045, -118.1553, 34.3373], crs=CRS.WGS84)

# Define the time range for the data you want to download
time_range = ('2022-01-01', '2022-01-31')

# Define the resolution and data collection you want to use
resolution = 10 # in meters
data_collection = DataCollection.SENTINEL2_L1C

# Convert the bounding box to pixel dimensions
width, height = bbox_to_dimensions(bbox.geometry, resolution=resolution)

# Define the SentinelHub request and download the data
request = SentinelHubRequest(
    data_folder='data_folder',
    evalscript='your_evalscript_code_here',
    input_data=[
        SentinelHubRequest.input_data(
            data_collection=data_collection,
            time_interval=time_range,
            mosaicking_order='leastCC'
        )
    ],
    responses=[
        SentinelHubRequest.output_response('default', MimeType.TIFF)
    ],
    bbox=bbox,
    size=(width, height),
    config={
        'instance_id': client_id,
        'client_secret': client_secret
    }
)
request.download_all()


# TO DO
# Note that you will need to replace your_evalscript with the actual evalscript you want to use to process the data, and data_folder with the path to the folder where you want to save the downloaded data
# Specify the path to the folder where you want to save the downloaded data, instead of using data_folder='data_folder'
