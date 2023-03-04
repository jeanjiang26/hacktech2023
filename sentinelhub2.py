# Import necessary libraries
from sentinelhub import SHConfig, SentinelHubRequest, DataCollection, bbox_to_dimensions, BBox, WcsRequest
import numpy as np
import matplotlib.pyplot as plt

# Define your SentinelHub credentials
config = SHConfig()
config.instance_id = 'YOUR_INSTANCE_ID'
config.sh_client_id = 'YOUR_CLIENT_ID'
config.sh_client_secret = 'YOUR_CLIENT_SECRET'

# Define the area of interest (AOI) as a bounding box
bbox = BBox(bbox=[-118.45, 33.80, -117.65, 34.35], crs='EPSG:4326')

# Define the time range and resolution of the data
time_interval = ('2022-01-01', '2022-01-31')
resolution = 30

# Define the Sentinel-2 data collection and bands to be used
data_collection = DataCollection.SENTINEL2_L2A
bands = ['B08', 'B04', 'B02']

# Convert the bounding box to pixel dimensions
dimensions = bbox_to_dimensions(bbox, resolution=resolution)

# Define the SentinelHubRequest object to download the data
request = SentinelHubRequest(
    data_collection=data_collection,
    evalscript='''//VERSION=3
    function setup() {
        return {
            input: [{
                bands: ["B02", "B04", "B08"],
                units: "DN"
            }],
            output: {
                bands: 3,
                sampleType: "FLOAT32"
            }
        };
    }

    function evaluatePixel(sample) {
        return [sample.B08, sample.B04, sample.B02];
    }''',
    input_data=[
        SentinelHubRequest.input_data(
            data_collection=data_collection,
            time_interval=time_interval,
            mosaicking_order='leastCC'
        )
    ],
    responses=[
        SentinelHubRequest.output_response('default', MimeType.TIFF)
    ],
    bbox=bbox,
    size=dimensions,
    config=config
)

# Execute the request and retrieve the data
data = request.get_data()

# Calculate the normalized difference vegetation index (NDVI)
ndvi = (data[..., 0] - data[..., 2]) / (data[..., 0] + data[..., 2])

# Define a threshold to identify urban areas
threshold = 0.3

# Create a binary mask of urban areas
urban_mask = np.where(ndvi < threshold, 1, 0)

# Plot the urban mask
plt.imshow(urban_mask, cmap='gray')
plt.title('Urban Mask')
plt.show()
