from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Standard, Laboratory


# =========================================================
# CREATE DATABASE TABLES
# =========================================================

Base.metadata.create_all(bind=engine)


# =========================================================
# FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="BIS SmartAssist API",
    description="Dynamic API for BIS Standards and Services",
    version="1.0"
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():

    return {
        "message": "BIS SmartAssist API is running!",
        "status": "success"
    }


# =========================================================
# STANDARDS - GET ALL / SEARCH
# =========================================================

@app.get("/api/standards")
def get_standards(
    q: str = "",
    db: Session = Depends(get_db)
):

    query = db.query(Standard)

    if q.strip():

        search = f"%{q.strip()}%"

        query = query.filter(
            (Standard.is_number.ilike(search)) |
            (Standard.title.ilike(search)) |
            (Standard.category.ilike(search)) |
            (Standard.description.ilike(search))
        )

    standards = query.all()

    result = []

    for standard in standards:

        result.append({

            "id": standard.id,

            "is_number": standard.is_number,

            "title": standard.title,

            "category": standard.category,

            "description": standard.description,

            "status": standard.status,

            "year": standard.year,

            "official_url": standard.official_url

        })

    return {

        "message": "Standards API is working!",

        "search": q,

        "count": len(result),

        "standards": result

    }


# =========================================================
# STANDARD - GET BY ID
# =========================================================

@app.get("/api/standards/{standard_id}")
def get_standard(
    standard_id: int,
    db: Session = Depends(get_db)
):

    standard = db.query(Standard).filter(
        Standard.id == standard_id
    ).first()


    if not standard:

        return {

            "message": "Standard not found",

            "status": "error"

        }


    return {

        "message": "Standard found",

        "status": "success",

        "standard": {

            "id": standard.id,

            "is_number": standard.is_number,

            "title": standard.title,

            "category": standard.category,

            "description": standard.description,

            "status": standard.status,

            "year": standard.year,

            "official_url": standard.official_url

        }

    }


# =========================================================
# STANDARDS - SEARCH BY CATEGORY
# =========================================================

@app.get("/api/standards/category/{category}")
def get_standards_by_category(
    category: str,
    db: Session = Depends(get_db)
):

    standards = db.query(Standard).filter(
        Standard.category.ilike(f"%{category}%")
    ).all()


    result = []


    for standard in standards:

        result.append({

            "id": standard.id,

            "is_number": standard.is_number,

            "title": standard.title,

            "category": standard.category,

            "description": standard.description,

            "status": standard.status,

            "year": standard.year,

            "official_url": standard.official_url

        })


    return {

        "message": "Category search completed",

        "category": category,

        "count": len(result),

        "standards": result

    }


# =========================================================
# LABORATORIES - GET ALL / SEARCH
# =========================================================

@app.get("/api/labs")
def get_laboratories(
    q: str = "",
    db: Session = Depends(get_db)
):

    query = db.query(Laboratory)


    # -----------------------------------------------------
    # SEARCH
    # -----------------------------------------------------

    if q.strip():

        search = f"%{q.strip()}%"


        query = query.filter(

            (Laboratory.lab_code.ilike(search)) |

            (Laboratory.name.ilike(search)) |

            (Laboratory.location.ilike(search)) |

            (Laboratory.testing_scope.ilike(search))

        )


    laboratories = query.all()


    result = []


    # -----------------------------------------------------
    # CONVERT DATABASE RECORDS TO JSON
    # -----------------------------------------------------

    for lab in laboratories:

        result.append({

            "id": lab.id,

            "lab_code": lab.lab_code,

            "name": lab.name,

            "location": lab.location,

            "testing_scope": lab.testing_scope,

            "official_url": lab.official_url

        })


    return {

        "message": "Laboratory search completed",

        "search": q,

        "count": len(result),

        "labs": result

    }
# =========================================================
# HALLMARKING - DYNAMIC INFORMATION
# =========================================================

@app.get("/api/hallmarking")
def get_hallmarking():

    return {

        "message": "Hallmarking information retrieved successfully",

        "hallmarking": {

            "title": "BIS Hallmarking",

            "description":
                "Hallmarking is the accurate determination and official recording "
                "of the proportionate content of precious metal in precious-metal articles.",

            "metals": [
                "Gold",
                "Silver"
            ],

            "huid": {

                "title": "HUID",

                "description":
                    "HUID stands for Hallmark Unique Identification. "
                    "It is a six-digit alphanumeric number that is unique "
                    "for each hallmarked gold item and is traceable."
            },

            "hallmark_components": [

                "BIS Logo",

                "Purity of the article in caratage and fineness",

                "Six-digit alphanumeric HUID number"

            ],

            "consumer_verification": {

                "title": "Consumer Verification",

                "description":
                    "Consumers can verify the HUID of hallmarked jewellery "
                    "using the Verify HUID feature in the BIS CARE App."

            },

            "jeweller_registration": {

                "title": "Jeweller Registration",

                "description":
                    "Jewellers selling hallmarked gold and silver jewellery "
                    "or artefacts are required to obtain BIS registration "
                    "according to the applicable rules."

            },

            "official_links": {

                "hallmarking_overview":
                    "https://www.bis.gov.in/hallmarking-overview/?lang=en",

                "hallmarking_faq":
                    "https://www.bis.gov.in/hallmarking-overview/hallmarking-faqs/hallmarking-faq/?lang=en",

                "bis_care":
                    "https://www.bis.gov.in/bis-apps/?lang=en",

                "jeweller_registration":
                    "https://www.bis.gov.in/apply-for-jewellers-registration/?lang=en",

                "hallmarking_centres":
                    "https://www.bis.gov.in/hallmarking-overview/hallmarking-centre/list-of-hallmarking-centres/?lang=en",

                "mandatory_hallmarking":
                    "https://www.bis.gov.in/hallmarking-overview/mandatory-hallmarking-order/?lang=en"

            }

        }

    }
# =========================================================
# CONSUMER - DYNAMIC INFORMATION
# =========================================================

@app.get("/api/consumer")
def get_consumer():

    return {

        "message": "Consumer information retrieved successfully",

        "consumer": {

            "title": "BIS Consumer Support",

            "description":
                "BIS provides consumers with information, complaint registration "
                "and guidance related to standards, certification and product quality.",

            "services": [

                {
                    "title": "Register a Complaint",

                    "description":
                        "Consumers can register complaints related to BIS standards, "
                        "certification, hallmarking and quality-related issues.",

                    "url":
                        "https://www.bis.gov.in/consumer-overview/online-complaint-registration/?lang=en"
                },

                {
                    "title": "Know Your Standard",

                    "description":
                        "Search and access information about Indian Standards using "
                        "an IS number or product-related keyword.",

                    "url":
                        "https://www.bis.gov.in/know-your-standard/?lang=en"
                },

                {
                    "title": "BIS CARE App",

                    "description":
                        "Use BIS CARE services to verify licence details, HUID and "
                        "access other consumer-oriented BIS services.",

                    "url":
                        "https://www.bis.gov.in/bis-apps/?lang=en"
                }

            ],

            "consumer_guidance": [

                "Check the relevant Indian Standard for the product.",

                "Verify applicable BIS certification or marking requirements.",

                "For hallmarked gold jewellery, verify the HUID through BIS CARE.",

                "Use official BIS channels to register complaints or obtain assistance."

            ],

            "official_links": {

                "complaint_registration":
                    "https://www.bis.gov.in/consumer-overview/online-complaint-registration/?lang=en",

                "know_your_standard":
                    "https://www.bis.gov.in/know-your-standard/?lang=en",

                "bis_care":
                    "https://www.bis.gov.in/bis-apps/?lang=en",

                "consumer_overview":
                    "https://www.bis.gov.in/consumer-overview/?lang=en"

            }

        }

    }
# =========================================================
# TRAINING - DYNAMIC INFORMATION
# =========================================================

@app.get("/api/training")
def get_training():

    return {

        "message": "Training information retrieved successfully",

        "training": {

            "title": "BIS Training & Capacity Building",

            "description":
                "BIS conducts training and capacity-building programmes "
                "to improve understanding of standards, conformity assessment "
                "and quality-related practices.",

            "programmes": [

                {
                    "title": "Standards & Standardization",

                    "description":
                        "Learn about Indian Standards, standardization activities "
                        "and the role of BIS in developing standards."
                },

                {
                    "title": "Conformity Assessment",

                    "description":
                        "Understand BIS certification, conformity assessment "
                        "schemes and related requirements."
                },

                {
                    "title": "Quality & Testing",

                    "description":
                        "Training related to quality management, testing "
                        "and laboratory-related practices."
                }

            ],

            "benefits": [

                "Improve understanding of Indian Standards.",

                "Learn about BIS certification and conformity assessment.",

                "Understand quality and testing practices.",

                "Build awareness of BIS services and procedures."

            ],

            "official_links": {

                "training_programmes":
                    "https://www.bis.gov.in/training-programmes/?lang=en",

                "training_calendar":
                    "https://www.bis.gov.in/training-programmes/?lang=en",

                "bis_home":
                    "https://www.bis.gov.in/?lang=en"

            }

        }

    }
# =========================================================
# DASHBOARD - DYNAMIC INFORMATION
# =========================================================

@app.get("/api/dashboard")
def get_dashboard(db: Session = Depends(get_db)):

    # Get live counts from database
    standards_count = db.query(Standard).count()
    laboratories_count = db.query(Laboratory).count()

    return {

        "message": "BIS SmartAssist dashboard data retrieved successfully",

        "dashboard": {

            "title": "BIS SmartAssist",

            "subtitle":
                "Intelligent assistance for Indian Standards and BIS Services.",

            "statistics": {

                "standards": standards_count,

                "laboratories": laboratories_count,

                "services": 7

            },

            "services": [

                {
                    "title": "Smart Standard Finder",

                    "description":
                        "Find relevant Indian Standards using product names, "
                        "keywords or IS numbers.",

                    "page":
                        "pages/standards.html"
                },

                {
                    "title": "Certification Navigator",

                    "description":
                        "Understand BIS certification pathways and access "
                        "official certification resources.",

                    "page":
                        "pages/certification.html"
                },

                {
                    "title": "Laboratory Finder",

                    "description":
                        "Find BIS recognized laboratories and explore "
                        "available testing information.",

                    "page":
                        "pages/laboratories.html"
                },

                {
                    "title": "Hallmarking",

                    "description":
                        "Understand hallmarking, HUID and precious-metal "
                        "quality information.",

                    "page":
                        "pages/hallmarking.html"
                },

                {
                    "title": "Consumer Support",

                    "description":
                        "Access BIS consumer services, complaint registration "
                        "and official guidance.",

                    "page":
                        "pages/consumer.html"
                },

                {
                    "title": "Training",

                    "description":
                        "Explore BIS training and capacity-building information.",

                    "page":
                        "pages/training.html"
                },

                {
                    "title": "AI SmartAssist",

                    "description":
                        "Ask questions in natural language and receive "
                        "BIS-focused guidance.",

                    "page":
                        "pages/assistant.html"
                }

            ],

            "official_links": {

                "bis_home":
                    "https://www.bis.gov.in/?lang=en",

                "standards":
                    "https://www.bis.gov.in/know-your-standard/?lang=en",

                "certification":
                    "https://www.bis.gov.in/product-certification/product-certification-overview/?lang=en",

                "laboratories":
                    "https://lims.bis.gov.in/home/labs/"

            }

        }

    }