## Android book reading application for kids using synthesis personalized (caretaker’s) voice (API)
source code นี้เป็นโค้ดที่ใช้พัฒนาในโครงการ แอปพลิเคชันแอนดรอยด์สำหรับอ่านหนังสือให้กับเด็ก โดยใช้เสียงสังเคราะห์ของผู้เลี้ยงดู
Android book reading application for kids using synthesis personalized (caretaker’s) voice ของนิสิตมหาวิทยาลัยศรีนครินทร์วิโรฒ 
โดยเป็นส่วนหนึ่งของการศึกษาตามหลักสูตรวิทยาศาสตร์บัณฑิต ภาควิชาวิทยาการคอมพิวเตอร์

>มีสมาชิกผู้จัดทำดังนี้

1.นางสาวกฤติยา      สุวรรณมาลัย   
2.นางสาวปภาพินท์   ทรัพย์มี     
3.นางสาวณัฐกฤตา    หาญเจริญกุล

>โดยมีอาจารย์ที่ปรึกษาคือ 

1.อ.ดร.นภา  เเซ่เบ๊ 

2.อ.บรรพตรี คมขำ

---
### API Document
api|method|รายละเอียด
|--|--|--|
/get_tales|GET|return ข้อมูลนิทานทั้งหมด|
/api_embed|POST|return embedding vector และเสียงสังเคราะห์ตัวอย่าง|
/api_syn_voice|POST|return เสียงสังเคราะห์และเนื้อเรื่องของนิทานที่เลือก|

---
### Installation
สำหรับการใช้ครั้งแรกให้ทำตามขั้นตอนด้านล่าง 

ทำการติดตั้งไลบรารี่ lame ในเครื่อง เพื่อบันทึก mp3 ได้  โดย
- ติดตั้ง chocolatey โดยใส่คำสั่งด้านล่างใน cmd

 ```
 $ @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin" 
 ```

- วิธีเช็คว่ามี chocolatey อยู่ในเครื่องแล้วหรือยังให้ใช้คำสั่ง

 ```$ choco --version ```

- หากติดตั้งเรียบร้อยอยู่แล้ว ใช้คำสั่งด้านล่างเพื่อติดตั้ง lame

 ```$ choco install lame ```

- เช็ค version lame โดย

 ```$ lame --version ```
 
 **ติดตั้ง module ที่เกี่ยวข้อง**

รันคำสั่ง  ```pip install -r requirements.txt ``` 

-----------------------------------
ใช้คำสั่งด้านล่างเพื่อรันโปรเจค
```
$ set FLASK_APP=app.py
$ python -m flask run
```

