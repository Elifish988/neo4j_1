<div dir="rtl">

# My CRUD App

אפליקציה זו מדגימה פעולות CRUD (Create, Read, Update, Delete) על פוסטים ברשתות חברתיות באמצעות MongoDB ו-PyMongo.

## עץ התיקיות

<div dir="ltr">

```python
my_crud_app/
│
├── app.py                   # הקובץ הראשי להרצת האפליקציה
├── config.py                # קובץ לשמירת פרטי חיבור למסד הנתונים
├── database.py              # קובץ לניהול חיבור למסד הנתונים
├── models/                  # תיקיית המודלים
│   └── social_post.py       # מודל לייצוג פוסט ברשתות חברתיות
├── services/                # תיקיית השירותים
│   └── post_service.py      # קובץ לניהול פעולות CRUD על הפוסטים
└── README.md                # הקובץ הזה
```

</div>

## דרישות מוקדמות

- Python 3.x
- pymongo
- MongoDB Community Server
- MongoDB Compass

## התקנה

1. הורד והתקן את MongoDB Community Server ו-MongoDB Compass.
2. התקן את התלותות על ידי הרצת הפקודה הבאה:

```bash
pip install pymongo
```

</div>