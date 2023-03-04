# contain all the code needed to interact with the SentinelHub API
# write functions to make API requests and process the responses
# use the requests library to make HTTP requests to the API, and the json library to parse the responses


# Import the required packages at the beginning of the file
#  importing the necessary packages for using the SentinelHub API and working with dates and times
import os
from sentinelhub import SentinelHubRequest, BBox, DataCollection, \
    SentinelHubDownloadClient, SentinelHubCatalog, SHConfig
from datetime import datetime

# Import the required configuration variables from config.py
# Importing the SENTINELHUB_API_KEY and SENTINELHUB_INSTANCE_ID variables from config.py
from config import SENTINELHUB_API_KEY, SENTINELHUB_INSTANCE_ID

# Set up SentinelHub API credentials
# Setting the instance ID and API key in the SHConfig instance
config = SHConfig()
config.instance_id = SENTINELHUB_INSTANCE_ID
config.sh_client_id = ''
config.sh_client_secret = ''
config.auth_config = {'SH_CLIENT_ID': '', 'SH_CLIENT_SECRET': ''}
config.api_key = SENTINELHUB_API_KEY

# Define a function that takes a bounding box and a date range, and returns a list of Sentinel-2 images for that area and time period
# A function that takes a bounding box, start date, and end date as input, and uses the SentinelHub API to download Sentinel-2 images for the specified area and time period
# Images are saved in a local folder named sentinel_images, and the function returns a list of file paths for the downloaded images
def get_sentinel_images(bbox, start_date, end_date):
    """
    Downloads Sentinel-2 images for the specified bounding box and date range.

    :param bbox: A bounding box in the format (minx, miny, maxx, maxy).
    :param start_date: A string representing the start date in ISO format (e.g. "2022-01-01").
    :param end_date: A string representing the end date in ISO format (e.g. "2022-01-31").
    :return: A list of file paths for the downloaded images.
    """
    # Create SentinelHub request
    request = SentinelHubRequest(
        data_folder='sentinel_images',
        evalscript='(B08 + B04)/(B08 - B04)',
        input_data=[
            SentinelHubRequest.input_data(
                data_collection=DataCollection.SENTINEL2_L1C,
                time_interval=(start_date, end_date),
                mosaicking_order='leastCC'
            )
        ],
        responses=[
            SentinelHubRequest.output_response('default', 'png')
        ],
        bbox=bbox,
        config=config
    )

    # Download images
    download_client = SentinelHubDownloadClient(config=config)
    request.download(download_client)

    # Get image paths
    images = []
    for filename in os.listdir('sentinel_images'):
        if filename.endswith('.png'):
            images.append(os.path.join('sentinel_images', filename))
    return images
