# שלב 1: בחירת תמונת בסיס
FROM python:3.12-slim

# שלב 2: הגדרת תקיית העבודה בתוך הקונטיינר
WORKDIR /app

# שלב 3: העתקת קובץ הדרישות (requirements.txt) אל הקונטיינר
COPY requirements.txt .

# שלב 4: התקנת התלויות של הפרויקט
RUN pip install --no-cache-dir -r requirements.txt


# שלב 5: העתקת כל קבצי הפרויקט לקונטיינר
COPY . .

EXPOSE 8000

# שלב 7: הפקודה שתופעל כשהקונטיינר יתחיל
CMD ["python", "app.py"]
