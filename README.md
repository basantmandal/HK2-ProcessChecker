# HK2_ProcessChecker - Python Process Checker

## Introduction

This Python3 Script - Monitors where a defined process is running or not under a specific user? In case the process is not running, it fires the process and send a email as an notification. This script has been tested on Ubuntu 20 & Ubuntu 20 Server Only.

This script can be very useful for servers where Java Services are run along side PHP or other environment. Everytime Manual Check cannot be done, Here this kinds of script are useful.

## Features
1. Lightweight
2. Does not depends on any 3rd Party Library

## Library Used

- smtplib - Built In Module (Sending SMTP Mails)
- psutil - Built in Module (For Process)
- subprocess - Built in Module (Creates Sub Process)