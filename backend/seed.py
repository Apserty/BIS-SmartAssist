from database import SessionLocal
from models import Standard, Laboratory


standards = [
    {
        "is_number": "IS 10500:2012",
        "title": "Drinking Water - Specification",
        "category": "Food and Agriculture",
        "description": "Indian Standard for drinking water specification.",
        "status": "Active",
        "year": "2012",
        "official_url": "https://standards.bis.gov.in/"
    },

    {
        "is_number": "IS 456:2000",
        "title": "Plain and Reinforced Concrete - Code of Practice",
        "category": "Civil Engineering",
        "description": "Code of practice for the general structural use of plain and reinforced concrete.",
        "status": "Active",
        "year": "2000",
        "official_url": "https://standards.bis.gov.in/"
    },

    {
        "is_number": "IS 302 (Part 1):2024",
        "title": "Safety of Household and Similar Electrical Appliances - Part 1 General Requirements",
        "category": "Electrical Engineering",
        "description": "General safety requirements for household and similar electrical appliances.",
        "status": "Active",
        "year": "2024",
        "official_url": "https://standards.bis.gov.in/"
    }
]


laboratories = [

    {
        "lab_code": "8102006",
        "name": "Shriram Institute For Industrial Research, Delhi",
        "location": "19-University Road, Delhi - 110007",
        "testing_scope": "BIS recognized testing laboratory. Testing scope should be verified through official BIS LIMS.",
        "official_url": "https://lims.bis.gov.in/home/labs/"
    },

    {
        "lab_code": "8138306",
        "name": "Testtex India Laboratories Private Limited, Noida",
        "location": "C-57, Sector-65, Noida, Uttar Pradesh - 201301",
        "testing_scope": "BIS recognized testing laboratory. Testing scope should be verified through official BIS LIMS.",
        "official_url": "https://lims.bis.gov.in/home/labs/"
    },

    {
        "lab_code": "6130526",
        "name": "REACT Compliance and Testing Laboratories LLP, Bengaluru",
        "location": "Service Road, Vijayanagar, Bengaluru, Karnataka - 560040",
        "testing_scope": "BIS recognized testing laboratory. Testing scope should be verified through official BIS LIMS.",
        "official_url": "https://lims.bis.gov.in/home/labs/"
    },

    {
        "lab_code": "6133516",
        "name": "CVR Labs Private Limited, Chennai",
        "location": "Saidapet, Chennai, Tamil Nadu - 600015",
        "testing_scope": "BIS recognized testing laboratory. Testing scope should be verified through official BIS LIMS.",
        "official_url": "https://lims.bis.gov.in/home/labs/"
    },

    {
        "lab_code": "9139736",
        "name": "Sleen India Biz Venture Private Limited, Agra",
        "location": "Agra, Uttar Pradesh - 282006",
        "testing_scope": "BIS recognized testing laboratory. Testing scope should be verified through official BIS LIMS.",
        "official_url": "https://lims.bis.gov.in/home/labs/"
    },

    {
        "lab_code": "8163826",
        "name": "Swastik Electronics Testing Centre, Ghaziabad",
        "location": "Mainapur Industrial Area, Ghaziabad, Uttar Pradesh - 201003",
        "testing_scope": "BIS recognized testing laboratory. Testing scope should be verified through official BIS LIMS.",
        "official_url": "https://lims.bis.gov.in/home/labs/"
    }
]


db = SessionLocal()

try:

    # -----------------------------
    # ADD STANDARDS
    # -----------------------------

    for item in standards:

        existing = db.query(Standard).filter(
            Standard.is_number == item["is_number"]
        ).first()

        if not existing:

            standard = Standard(**item)

            db.add(standard)


    # -----------------------------
    # ADD LABORATORIES
    # -----------------------------

    for item in laboratories:

        existing = db.query(Laboratory).filter(
            Laboratory.lab_code == item["lab_code"]
        ).first()

        if not existing:

            laboratory = Laboratory(**item)

            db.add(laboratory)


    db.commit()

    print("BIS standards and laboratories added successfully!")


finally:

    db.close()