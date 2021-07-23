# Python Web Development with Django Course

ซอร์สโค้ดสำหรับศึกษาเพิ่มเติม

## 1. ติดตั้งและรันโปรเจคท์

##### 1.1 Clone โปรเจคท์

```bash
git clone https://github.com/SonNavigator/pea.git
```

##### 1.2 ไปที่ working directory  (pea)
```bash
cd pea
```

##### 1.3 สร้าง virtual environment

```bash
# สร้าง virtual environment ชื่อว่า env (อยู่ใน root directory)
python -m venv env

# Activate (เรียกใช้งาน) virtual environment
env/Scripts/activate  # (Windows)

source env/bin/activate  # (macOS)
```

##### 1.4 ติดตั้ง dependencies และ packages & libraries ทุกตัวที่ต้องใช้
ตอนนี้มี env แล้ว แต่จะยังไม่สามารถรันโปรเจคท์ได้เพราะยังไม่ได้ติดตั้งไลบรารี่ต่าง ๆ เข้ามา

```bash
pip install -r requirements.txt
```
เสร็จแล้วทุก ๆ ไลบรารี่ที่ใช้ ซึ่งได้ถูกลิสต์ไว้ในไฟล์ requirements.txt 
จะถูกติดตั้งพร้อมสำหรับที่จะใช้ในโปรเจคท์

##### 1.5 รันโปรเจคท์

```bash
python manage.py runserver
```