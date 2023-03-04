# contain all the configuration variables for your project, such as API keys and access tokens. You can use this file to store sensitive information that you don't want to hardcode into your main Python files.

# Authenticate with the SentinelHub API
SENTINELHUB_API_KEY = "your-api-key-here"
SENTINELHUB_INSTANCE_ID = "your-instance-id-here"

# Authenticate with the GHGSat AI model
GHGSAT_API_KEY = "your-api-key-here"
GHGSAT_MODEL_ID = "your-model-id-here"

# Green roof estimation settings
# Specify the cost per square foot for installing a green roof
GREEN_ROOF_COST_PER_SQ_FT = 20.0

# stores the machine learning model used to estimate the suitable areas for green roofs, which in this case is set to "random-forest"
GREEN_ROOF_ESTIMATION_MODEL = "random-forest"


