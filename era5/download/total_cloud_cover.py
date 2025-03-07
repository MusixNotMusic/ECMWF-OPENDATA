import cdsapi

dataset = "reanalysis-era5-single-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": ["total_cloud_cover"],
    "year": ["2025"],
    "month": ["03"],
    "day": ["01"],
    "time": ["00:00", "01:00", "02:00"],
    "data_format": "grib",
    "download_format": "zip"
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()