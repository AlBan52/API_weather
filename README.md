# Terminal Weather

The present script - ```console_weather.py``` could output the weather in choosen locations for actual date. The weather data is output to the terminal.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

Befor script ```console_weather.py``` running, you have to fill the locations list. For example:
```python
locations = ["London", "Paris", "New York"]
```
The name of any location could enter in languages from this list:
```ar af be ca da de el en et fr fa hi hu ia id it nb nl oc pl pt-br ro ru tr th uk vi zh-cn zh-tw```
For output results on needed language, you have to specify required language in this line:
```python
url_template = 'http://wttr.in/{}?m&lang=en'
``` 
### Output results

As results you get 3 or more tables in terminal with actual weather information in choosen locations.
Example of terminal outputs is on screenshot below.

![alt text](https://github.com/AlBan52/API_weather/blob/main/screenshots/example.png)

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).