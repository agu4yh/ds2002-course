from urllib.request import urlretrieve
import boto3
# import urllib

# vars
bucket_name = 'ds2002-agu4yh'
expires_in = 604800

# create client
s3 = boto3.client("s3", region_name="us-east-1")

# get image from url
# puppy = requests.get("https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg")
# puppy = urllib.request.urlrequest("https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg") 
urlretrieve("https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "puppy.jpg") 

# upload file to bucket in s3
resp = s3.put_object(
    Body = "puppy.jpg",
    Bucket = bucket_name,
    Key = "puppy.jpg",
    ACL = 'public-read'
)

# presign the file
response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': "puppy.jpg"},
    ExpiresIn=expires_in
    )

print(response)

# presigned url: https://ds2002-agu4yh.s3.amazonaws.com/puppy.jpg?AWSAccessKeyId=ASIAW3MEAQIBUIUWYG6L&Signature=XfFMiRkwMtQonq6YJn%2B4WaDNR30%3D&x-amz-security-token=FwoGZXIvYXdzEAcaDPWt1L7kQwEGLR%2B8liLEAdvlkuJKyCt%2FlnvxHvE0CxhSHuS9xADhRtOPhyR3%2Ff%2FIJaXkrM91WvfHYnCUEL2gZxCe3lpXViApgB2E5Txh9jkEC424eNnFTJlKgQS36quoODNQ0YERYALjU1VzbyrQjdOUM%2FviceuGyxiWAlWuV%2FViweqfI8Q%2B9P13cm6LNG2xkcYRKQ9FdJ3ryDVFwllVNIXCPbmkI37t4SuALi6l2tpOY81rd%2FyI%2FdkeSN784eb1n6SVIbselwTGnfYlaosHuorRT0ko9q35rgYyLUT5529uDQCetFLrOqQT%2FnUlBZP6WduD0NJv4PAwvlU2FgSCc2lz8CLhfyGaEQ%3D%3D&Expires=1709675119