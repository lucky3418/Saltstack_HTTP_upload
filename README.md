# Saltstack_HTTP_upload
SaltStack scripts for uploading screenshots to a HTTP server

Need a saltstack beacon created, that will look for a file that is created - file name will be between 1000000.jpg (or maybe bmp or png) to 9999999.jpg.
When the file is found (interval should be variable, but by default every second), it will upload the flie to a URL that will be stored in either grains or pillar.

Here is info on the [http moudle](https://docs.saltstack.com/en/latest/topics/tutorials/http.html)