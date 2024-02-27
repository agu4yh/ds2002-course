#!/bin/bash


curl https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png > google_logo.png
aws s3 cp google_logo.png s3://ds2002-agu4yh/
aws s3 presign --expires-in 604800 s3://ds2002-agu4yh/google_logo.png

#presigned url: https://ds2002-agu4yh.s3.us-east-1.amazonaws.com/google_logo.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAW3MEAQIBVAF2GEBI%2F20240227%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240227T175414Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEAMaDEjbmA%2B5cFKk6AO7vSLEAS0vTRkAb8ByhHkU%2FSseciBJs7fadJP4uZui6TGyaXaunP7rDS6PcQXyAuOzWiFzgw691C8%2Baf67QmWoau21zI891XeNASn9szkXE%2FyX8hz2%2Fl08fj2X8QGOFyvWw7%2BLbP3xIAXxL4tRWAB6X6uumd4Tfu69YEjUWQWIRL6oxjVHU9W%2BB0UIAkdgsSW66Xlodo%2F4iZ9dBBQq8oiQheDsbHfV0JUrKmNCHSVrqTFAO4grhDHkoLXxwRSeEya8grvDicwHopwomr34rgYyLfWpwgWrQCPdMVdzUqFipYb%2BpH0p5UQXTm6hFmTaj6W873nHa%2B6mhQjufQ2Yrw%3D%3D&X-Amz-Signature=e8024562d3b9ea6dd30196380df89c0df26d8d331d93869f4d53fdb799f33254