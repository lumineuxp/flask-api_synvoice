สำหรับการใช้ครั้งแรกให้ใช้คำสั่ง pip install -r requirements.txt ในการติดตั้ง module ที่เกี่ยวข้อง

ทำการติดตั้งไลบรารี่ lame ในเครื่อง เพื่อบันทึก mp3 ได้  โดย
- ติดตั้ง chocolatey โดยใส่คำสั่งด้านล่างใน cmd
$ @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

- วิธีเช็คว่ามี chocolatey อยู่ในเครื่องแล้วหรือยังให้ใช้คำสั่ง
$ choco --version

- หากติดตั้งเรียบร้อยอยู่แล้ว ใช้คำสั่งด้านล่างเพื่อติดตั้ง lame
$ choco install lame

-เช็ค version lame โดย
$ lame --version

-----------------------------------
ใช้คำสั่งด้านล่างเพื่อรันโปรเจค

$ set FLASK_APP=app.py
$ python -m flask run


