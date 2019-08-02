# MovieDownloader
This software will enable downloading movie from a link. 
I used Apache 2.4 http webserver for this project. 
Apache webserver should be configure for php and python. 
Initially, I wanted to use only php aside html for this project.
Since installing and configure php_pthread is hoplessly hard, I gave up :-( !

## Dependecies
* Python 2.7 
* Php 7.2
* Apache 2.4

## Interface

The interface is pretty simple. I can use any webbrowser to access this following page as follows

```
http://localhost:433/
```
Note that I change the default port from 8080 to 433

The website is mobile friendly, so I can use my cell phone to see contents perfectly. 
I have saved this webapge to my mobile home scrren. 

## Background software
* Axel 

Here is where the magic happens. Axel is command line downloading software as alternative of wget. 
It can create multiple connection to download the content very fast. I use 8 connections as default parameter. 
When a request has been submitted, python creates a thread to run axel at background. 

## Recommendation

If you are windows user, please use chocolatey and cmder to make you life easier, cheers !!!!








