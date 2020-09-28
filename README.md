# Archivist

#### CENTRALIZE YOUR DIGITAL ASSETS.

Archivist is an easy tool to help organizing all your digital assets.

The software is under MIT license.

This project is W.I.P, and has a long way to go.

## 1.Background
For most of people, what they really need is to deal with their
valuable files(pictures, music, video, pdf and documents). 

Archivist aims to be a tool which helps to manage all the valuable
files simply.

## 2. Environment
- Windows 10
- Anaconda
- Python3.8
- PyQt5

## 3.Dependency
Before you start, make sure everything is set
```shell script
pip install -r requirements.txt
``` 
You can also use conda to reach the same environment
```shell script
conda env create -f environment.yml
```
If the network is fine then it should be done within a few minutes.

## 4. Usage
- Clone the repository
```shell script
git clone https://github.com/Oderschvank/Archivist.git
```
then just run Archivist.py directly
```shell script
python Archivist.py
```

## 5.Project Structure
1. Archivist.py is the entrance of the software, the object controller 
will be created here.

2./core holds Archivies.db by default. If Archivies.db is imported from
other place, then it will be here and replace the older one.

## 6.Dev Log
09/28/20 Basic feature is nearly done. Right now, each file can hold 
a tag, a rating and a keyword seperately.

## 7. TO-DO
-[ ] For each file, can hold more than just one tag and one keyword.