import cdsapi
import zipfile
import os

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

# 定义下载文件的路径
download_path = "./data/era5/downloaded_data.zip"

client = cdsapi.Client()
client.retrieve(dataset, request, download_path)

print(f"文件已下载到 {download_path}")

# 定义解压路径
extract_path = "./data/grid/"

# 创建解压目录（如果不存在）
os.makedirs(extract_path, exist_ok=True)

# 解压文件
with zipfile.ZipFile(download_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print(f"文件已解压到 {extract_path}")

extracted_files  = os.listdir(extract_path)

if extracted_files:
    original_file_path = os.path.join(extract_path, extracted_files[0])
    new_file_path = os.path.join(extract_path, "renamed_file.grib")
    
    # 重命名文件
    os.rename(original_file_path, new_file_path)
    print(f"文件已重命名为 {new_file_path}")
else:
    print("解压目录中没有找到文件")
