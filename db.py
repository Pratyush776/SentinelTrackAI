from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models import Department, Attacker, Alert, ForensicReport, Incident

async def init_db():
    # Connect to local MongoDB
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    
    # Access the database object
    database = client.honeypot_db
    
    # Initialize Beanie
    await init_beanie(
        database=database, 
        document_models=[Department, Attacker, Alert, ForensicReport, Incident]
    )
    print("\n[CONSOLE LOG] =================")
    print("✅ SUCCESS: MongoDB Honeypot Database Connection Active!")
    print("================================\n")