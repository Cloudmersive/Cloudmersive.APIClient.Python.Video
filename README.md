# cloudmersive_video_api_client
The video APIs help you convert, encode, and transcode videos.

This Python package provides a native API client for [Cloudmersive Video and Media Services](https://cloudmersive.com/video-and-media-services-api)

- API version: v1
- Package version: 3.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_video_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_video_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cloudmersive_video_api_client
from cloudmersive_video_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_video_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_video_api_client.VideoApi(cloudmersive_video_api_client.ApiClient(configuration))
input_file = '/path/to/file.txt' # file | Input file to perform the operation on.
file_url = 'file_url_example' # str | Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. (optional)
max_width = 56 # int | Optional; Maximum width of the output video, up to the original video width. Defaults to 250 pixels. (optional)
max_height = 56 # int | Optional; Maximum height of the output video, up to the original video width. Defaults to 250 pixels. (optional)
preserve_aspect_ratio = true # bool | Optional; If false, the original video's aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. (optional)
frame_rate = 56 # int | Optional; Specify the frame rate of the output video. Defaults to 24 frames per second. (optional)
extend_processing_time = true # bool | Optional; If true, will allow additional processing time for the video file conversion, using one API call per additional minute over the 5 minute default processing time, up to a maximum of 25 total minutes. This is generally necessary for files larger than 500 MB or longer than 30 minutes. (optional)
start_time = '2013-10-20T19:20:30+01:00' # datetime | Optional; Specify the desired starting time of the GIF video in TimeSpan format. (optional)
time_span = '2013-10-20T19:20:30+01:00' # datetime | Optional; Specify the desired length of the GIF video in TimeSpan format. Limit is 30 minutes. (optional)

try:
    # Convert Video to Animated GIF format.
    api_response = api_instance.video_convert_to_gif(input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, extend_processing_time=extend_processing_time, start_time=start_time, time_span=time_span)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_convert_to_gif: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*VideoApi* | [**video_convert_to_gif**](docs/VideoApi.md#video_convert_to_gif) | **POST** /video/convert/to/gif | Convert Video to Animated GIF format.
*VideoApi* | [**video_convert_to_mov**](docs/VideoApi.md#video_convert_to_mov) | **POST** /video/convert/to/mov | Convert Video to MOV format.
*VideoApi* | [**video_convert_to_mp4**](docs/VideoApi.md#video_convert_to_mp4) | **POST** /video/convert/to/mp4 | Convert Video to MP4 format.
*VideoApi* | [**video_convert_to_webm**](docs/VideoApi.md#video_convert_to_webm) | **POST** /video/convert/to/webm | Convert Video to WEBM format.
*VideoApi* | [**video_get_info**](docs/VideoApi.md#video_get_info) | **POST** /video/convert/get-info | Get detailed information about a video or audio file


## Documentation For Models

 - [MediaInformation](docs/MediaInformation.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



