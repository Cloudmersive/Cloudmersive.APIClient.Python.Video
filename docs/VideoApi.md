# cloudmersive_video_api_client.VideoApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**video_convert_to_gif**](VideoApi.md#video_convert_to_gif) | **POST** /video/convert/to/gif | Convert Video to Animated GIF format.
[**video_convert_to_mov**](VideoApi.md#video_convert_to_mov) | **POST** /video/convert/to/mov | Convert Video to MOV format.
[**video_convert_to_mp4**](VideoApi.md#video_convert_to_mp4) | **POST** /video/convert/to/mp4 | Convert Video to MP4 format.
[**video_convert_to_webm**](VideoApi.md#video_convert_to_webm) | **POST** /video/convert/to/webm | Convert Video to WEBM format.
[**video_get_info**](VideoApi.md#video_get_info) | **POST** /video/convert/get-info | Get detailed information about a video or audio file


# **video_convert_to_gif**
> str video_convert_to_gif(input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, extend_processing_time=extend_processing_time, start_time=start_time, time_span=time_span)

Convert Video to Animated GIF format.

Automatically detect video file format and convert it to animated GIF format. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, OGV, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Maximum output file size is 50GB. Default height is 250 pixels, while preserving the video's aspect ratio.

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **max_width** | **int**| Optional; Maximum width of the output video, up to the original video width. Defaults to 250 pixels. | [optional] 
 **max_height** | **int**| Optional; Maximum height of the output video, up to the original video width. Defaults to 250 pixels. | [optional] 
 **preserve_aspect_ratio** | **bool**| Optional; If false, the original video&#39;s aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. | [optional] 
 **frame_rate** | **int**| Optional; Specify the frame rate of the output video. Defaults to 24 frames per second. | [optional] 
 **extend_processing_time** | **bool**| Optional; If true, will allow additional processing time for the video file conversion, using one API call per additional minute over the 5 minute default processing time, up to a maximum of 25 total minutes. This is generally necessary for files larger than 500 MB or longer than 30 minutes. | [optional] 
 **start_time** | **datetime**| Optional; Specify the desired starting time of the GIF video in TimeSpan format. | [optional] 
 **time_span** | **datetime**| Optional; Specify the desired length of the GIF video in TimeSpan format. Limit is 30 minutes. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_convert_to_mov**
> str video_convert_to_mov(input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality, extend_processing_time=extend_processing_time)

Convert Video to MOV format.

Automatically detect video file format and convert it to MOV format. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, OGV, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Maximum output file size is 50GB.

### Example
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
max_width = 56 # int | Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. (optional)
max_height = 56 # int | Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. (optional)
preserve_aspect_ratio = true # bool | Optional; If false, the original video's aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. (optional)
frame_rate = 56 # int | Optional; Specify the frame rate of the output video. Defaults to original video frame rate. (optional)
quality = 56 # int | Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. (optional)
extend_processing_time = true # bool | Optional; If true, will allow additional processing time for the video file conversion, using one API call per additional minute over the 5 minute default processing time, up to a maximum of 25 total minutes. This is generally necessary for files larger than 500 MB or longer than 30 minutes. (optional)

try:
    # Convert Video to MOV format.
    api_response = api_instance.video_convert_to_mov(input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality, extend_processing_time=extend_processing_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_convert_to_mov: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **max_width** | **int**| Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. | [optional] 
 **max_height** | **int**| Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. | [optional] 
 **preserve_aspect_ratio** | **bool**| Optional; If false, the original video&#39;s aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. | [optional] 
 **frame_rate** | **int**| Optional; Specify the frame rate of the output video. Defaults to original video frame rate. | [optional] 
 **quality** | **int**| Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. | [optional] 
 **extend_processing_time** | **bool**| Optional; If true, will allow additional processing time for the video file conversion, using one API call per additional minute over the 5 minute default processing time, up to a maximum of 25 total minutes. This is generally necessary for files larger than 500 MB or longer than 30 minutes. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_convert_to_mp4**
> str video_convert_to_mp4(input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality, extend_processing_time=extend_processing_time)

Convert Video to MP4 format.

Automatically detect video file format and convert it to MP4 format. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, OGV, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Maximum output file size is 50GB.

### Example
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
max_width = 56 # int | Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. (optional)
max_height = 56 # int | Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. (optional)
preserve_aspect_ratio = true # bool | Optional; If false, the original video's aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. (optional)
frame_rate = 56 # int | Optional; Specify the frame rate of the output video. Defaults to original video frame rate. (optional)
quality = 56 # int | Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. (optional)
extend_processing_time = true # bool | Optional; If true, will allow additional processing time for the video file conversion, using one API call per additional minute over the 5 minute default processing time, up to a maximum of 25 total minutes. This is generally necessary for files larger than 500 MB or longer than 30 minutes. (optional)

try:
    # Convert Video to MP4 format.
    api_response = api_instance.video_convert_to_mp4(input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality, extend_processing_time=extend_processing_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_convert_to_mp4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **max_width** | **int**| Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. | [optional] 
 **max_height** | **int**| Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. | [optional] 
 **preserve_aspect_ratio** | **bool**| Optional; If false, the original video&#39;s aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. | [optional] 
 **frame_rate** | **int**| Optional; Specify the frame rate of the output video. Defaults to original video frame rate. | [optional] 
 **quality** | **int**| Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. | [optional] 
 **extend_processing_time** | **bool**| Optional; If true, will allow additional processing time for the video file conversion, using one API call per additional minute over the 5 minute default processing time, up to a maximum of 25 total minutes. This is generally necessary for files larger than 500 MB or longer than 30 minutes. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_convert_to_webm**
> str video_convert_to_webm(input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality, extend_processing_time=extend_processing_time)

Convert Video to WEBM format.

Automatically detect video file format and convert it to WEBM format. Supports many input video formats, including AVI, ASF, FLV, MP4, MPEG/MPG, Matroska/WEBM, 3G2, OGV, MKV, M4V and MOV. Uses 1 API call per 10 MB of file size. Maximum output file size is 50GB.

### Example
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
max_width = 56 # int | Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. (optional)
max_height = 56 # int | Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. (optional)
preserve_aspect_ratio = true # bool | Optional; If false, the original video's aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. (optional)
frame_rate = 56 # int | Optional; Specify the frame rate of the output video. Defaults to original video frame rate. (optional)
quality = 56 # int | Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. (optional)
extend_processing_time = true # bool | Optional; If true, will allow additional processing time for the video file conversion, using one API call per additional minute over the 5 minute default processing time, up to a maximum of 25 total minutes. This is generally necessary for files larger than 500 MB or longer than 30 minutes. (optional)

try:
    # Convert Video to WEBM format.
    api_response = api_instance.video_convert_to_webm(input_file, file_url=file_url, max_width=max_width, max_height=max_height, preserve_aspect_ratio=preserve_aspect_ratio, frame_rate=frame_rate, quality=quality, extend_processing_time=extend_processing_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_convert_to_webm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 
 **max_width** | **int**| Optional; Maximum width of the output video, up to the original video width. Defaults to original video width. | [optional] 
 **max_height** | **int**| Optional; Maximum height of the output video, up to the original video width. Defaults to original video height. | [optional] 
 **preserve_aspect_ratio** | **bool**| Optional; If false, the original video&#39;s aspect ratio will not be preserved, allowing customization of the aspect ratio using maxWidth and maxHeight, potentially skewing the video. Default is true. | [optional] 
 **frame_rate** | **int**| Optional; Specify the frame rate of the output video. Defaults to original video frame rate. | [optional] 
 **quality** | **int**| Optional; Specify the quality of the output video, where 100 is lossless and 1 is the lowest possible quality with highest compression. Default is 50. | [optional] 
 **extend_processing_time** | **bool**| Optional; If true, will allow additional processing time for the video file conversion, using one API call per additional minute over the 5 minute default processing time, up to a maximum of 25 total minutes. This is generally necessary for files larger than 500 MB or longer than 30 minutes. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_get_info**
> str video_get_info(input_file, file_url=file_url)

Get detailed information about a video or audio file

Retrieve detailed information about a video or audio file, including format, dimensions, file size, bit rate, duration and start time. Compatible with many formats, including: AVI, ASF, FLV, GIF, MP4, MPEG/MPG, Matroska/WEBM, MOV, AIFF, ASF, CAF, MP3, MP2, MP1, Ogg, OMG/OMA, and WAV. Uses 1 API call per 10 MB of file size.

### Example
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

try:
    # Get detailed information about a video or audio file
    api_response = api_instance.video_get_info(input_file, file_url=file_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoApi->video_get_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_file** | **file**| Input file to perform the operation on. | 
 **file_url** | **str**| Optional; URL of a video file being used for conversion. Use this option for files larger than 2GB. | [optional] 

### Return type

**str**

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

