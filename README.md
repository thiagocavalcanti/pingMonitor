# pingMonitor
A simple script in python to monitor your network and saving in a .csv file

<b> Description </b>

Using subprocess, the scripts pings to google address (8.8.8.8) and counts the succesful responses and also if no response is acquired. After a minute, it writes out in a csv file (so you can create graphs with it), which each column is:

Month - Day - Hour - Minute - Avg time - Positive pings - Negative pings.

It was created because of a poor service of 'Vivo' internet provider, so I used to show them that my internet was not working at all, especially in some hours of the day, such as between 5pm-7pm (time that more people arrives in the building)
