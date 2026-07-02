#ADMISSION NUMBER:C027-01-2287/2024

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional, Literal

app = FastAPI(
    title="GigHub Freelance Gigs API",
    description="A FastAPI for managing freelance gigs.\nAdmission Number: C027-01-2287/2024",
    version="1.0.0"
)


class GigCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=20, max_length=500)
    category: Literal["Marketing", "Data", "Consulting"]
    budget: float = Field(..., gt=0)
    client_name: str = Field(..., min_length=2, max_length=50)


class GigUpdate(BaseModel):
    budget: Optional[float] = Field(None, gt=0)
    status: Optional[Literal["Open", "In Progress", "Closed"]] = None


# Allowed categories
ALLOWED_CATEGORIES = [
    "Marketing",
    "Data",
    "Consulting"
]

# Allowed status
ALLOWED_STATUS = [
    "Open",
    "Closed",
    "In Progress"
]

#ADMISSION NUMBER : C027-01-2287/2024

gigs_db = [
    {
        "id": 1,
        "title": "Social Media Marketing",
        "description": "Develop a complete social media strategy to increase brand awareness and customer engagement.",
        "category": "Marketing",
        "budget": 1000,
        "currency": "USD",
        "status": "Open",
        "client_name": "Antony Kamau"
    },
    {
        "id": 2,
        "title": "Retail Sales Data Analysis",
        "description": "Analyze monthly sales records and prepare visual reports to identify trends and improve business decisions.",
        "category": "Data",
        "budget": 1450,
        "currency": "USD",
        "status": "Open",
        "client_name": "Denis Otieno"
    },
    {
        "id": 3,
        "title": "Startup Business Consultation",
        "description": "Advise a technology startup on business planning, operational improvements, and long-term growth strategies.",
        "category": "Consulting",
        "budget": 2400,
        "currency": "USD",
        "status": "In Progress",
        "client_name": "Faith Wanjiru"
    },
    {
        "id": 4,
        "title": "Email Marketing Campaign",
        "description": "Create and manage an email marketing campaign targeting new customers while improving conversion rates.",
        "category": "Marketing",
        "budget": 3050,
        "currency": "USD",
        "status": "Closed",
        "client_name": "John Mwangi"
    },
    #ADMISSION NUMBER:C027-01-2287/2024
    {
        "id": 5,
        "title": "Customer Database Cleanup",
        "description": "Clean up customer records, remove duplicate entries, and prepare accurate datasets for business reporting.",
        "category": "Data",
        "budget": 1000,
        "currency": "USD",
        "status": "Closed",
        "client_name": "Lucy Achieng"
    },
    {
        "id": 6,
        "title": "Financial Planning Advisory",
        "description": "Provide financial planning advice and recommend budgeting strategies for a growing small business.",
        "category": "Consulting",
        "budget": 2000,
        "currency": "USD",
        "status": "In Progress",
        "client_name": "Michael Kimani"
    },
    {
        "id": 7,
        "title": "Digital Advertising",
        "description": "Review online advertising and recommend improvements to maximize customer reach and return on investment.",
        "category": "Marketing",
        "budget": 2400,
        "currency": "USD",
        "status": "Open",
        "client_name": "Sarah Johnson"
    },
    #ADMISSION NUMBER:C027-01-2287/2024
    {
        "id": 8,
        "title": "Business Intelligence Dashboard",
        "description": "Organize business data and prepare reports that help managers monitor key performance indicators.",
        "category": "Data",
        "budget": 1000,
        "currency": "USD",
        "status": "Open",
        "client_name": "Peter Njoroge"
    },
    #ADMISSION NUMBER:C027-01-2287/2024
    {
        "id": 9,
        "title": "Human Resource",
        "description": "Review human resource policies and recommend practical improvements that support development.",
        "category": "Consulting",
        "budget": 3500,
        "currency": "USD",
        "status": "Open",
        "client_name": "Jane Mercy Wambui"
    },
    {
        "id": 10,
        "title": "Content Promotion",
        "description": "Design a content marketing strategy that improves website traffic and increases audience engagement.",
        "category": "Marketing",
        "budget": 2500,
        "currency": "USD",
        "status": "In Progress",
        "client_name": "David Kimani"
    },
    {
        "id": 11,
        "title": "Data Visualization",
        "description": "Transform customer survey results into meaningful charts and reports that support decision making.",
        "category": "Data",
        "budget": 1590,
        "currency": "USD",
        "status": "Closed",
        "client_name": "Grace Onega"
    },
    {
        "id": 12,
        "title": "Market Expansion Consultant",
        "description": "Research new business opportunities and recommend expansion ideas.",
        "category": "Consulting",
        "budget": 2400,
        "currency": "USD",
        "status": "Open",
        "client_name": "James Otieno"
    }
]
#ADMISSION NUMBER:C027-01-2287/2024

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the GigHub Freelance Gigs API!",
        "student": "Admission Number: C027-01-2287/2024"
    }


@app.get("/gigs")
def get_all_gigs(
    category: Optional[str] = Query(None),
    min_budget: Optional[float] = Query(None),
    max_budget: Optional[float] = Query(None)
):
    filtered_gigs = gigs_db

    if category:
        filtered_gigs = [
            gig for gig in filtered_gigs
            if gig["category"].lower() == category.lower()
        ]

    if min_budget is not None:
        filtered_gigs = [
            gig for gig in filtered_gigs
            if gig["budget"] >= min_budget
        ]

    if max_budget is not None:
        filtered_gigs = [
            gig for gig in filtered_gigs
            if gig["budget"] <= max_budget
        ]

    return filtered_gigs

#ADMISSION NUMBER:C027-01-2287/2024
@app.get("/gigs/search")
def search_gigs(q: str = Query(..., min_length=1)):
    results = []

    for gig in gigs_db:
        if q.lower() in gig["title"].lower():
            results.append(gig)

    return results


@app.post("/gigs")
def create_gig(gig: GigCreate):
    new_gig = {
        "id": len(gigs_db) + 1,
        "title": gig.title,
        "description": gig.description,
        "category": gig.category,
        "budget": gig.budget,
        "currency": "USD",
        "status": "Open",
        "client_name": gig.client_name
    }

    gigs_db.append(new_gig)

    return {
        "message": "Gig created successfully.",
        "gig": new_gig
    }
@app.get("/gigs/{gig_id}")
def get_gig_by_id(gig_id: int):
    for gig in gigs_db:
        if gig["id"] == gig_id:
            return gig

    raise HTTPException(
        status_code=404,
        detail="Gig not found"
    )
#ADMISSION NUMBER:C027-01-2287/2024
@app.put("/gigs/{gig_id}")
def update_gig(gig_id: int, gig: GigUpdate):
    for existing_gig in gigs_db:
        if existing_gig["id"] == gig_id:

            if gig.budget is not None:
                existing_gig["budget"] = gig.budget

            if gig.status is not None:
                existing_gig["status"] = gig.status

            return {
                "message": "Gig updated successfully.",
                "gig": existing_gig
            }

    raise HTTPException(
        status_code=404,
        detail="Gig not found"
    )
    


@app.delete("/gigs/{gig_id}")
def delete_gig(gig_id: int):
    for index, gig in enumerate(gigs_db):
        if gig["id"] == gig_id:
            deleted_gig = gigs_db.pop(index)

            return {
                "message": "Gig deleted successfully.",
                "gig": deleted_gig
            }

    raise HTTPException(
        status_code=404,
        detail="Gig not found"
    )
