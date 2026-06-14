from fastapi import FastAPI, HTTPException
from db import init_db
from models import Department, Attacker, Alert, ForensicReport, Incident
from beanie import PydanticObjectId

app = FastAPI(title="Honeypot & Threat Logging System API")

@app.on_event("startup")
async def startup_event():
    await init_db()

# ==================== CRUD: CREATE / INSERT ====================
@app.post("/departments/", tags=["Departments"])
async def add_department(dept: Department):
    await dept.insert()
    return {"status": "Department added to tracking", "data": dept}

@app.post("/attackers/", tags=["Attackers"])
async def register_attacker(attacker: Attacker):
    await attacker.insert()
    return {"status": "Threat actor profile registered", "data": attacker}

@app.post("/alerts/", tags=["Alerts"])
async def log_alert(alert: Alert):
    await alert.insert()
    return {"status": "Alert logged", "data": alert}

@app.post("/incidents/", tags=["Incidents"])
async def create_incident(incident: Incident):
    await incident.insert()
    return {"status": "Incident opened", "data": incident}

# ==================== CRUD: READ / LINK RESOLUTION ====================
@app.get("/alerts/{alert_id}", tags=["Alerts"])
async def fetch_alert_details(alert_id: PydanticObjectId):
    alert = await Alert.get(alert_id, fetch_links=True)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert record not found")
    return alert

# ==================== CRUD: UPDATE / LINKING ====================
@app.put("/incidents/{incident_id}/link-attacker/{attacker_id}", tags=["Incidents"])
async def link_attacker_to_incident(incident_id: PydanticObjectId, attacker_id: PydanticObjectId):
    incident = await Incident.get(incident_id)
    attacker = await Attacker.get(attacker_id)
    
    if not incident or not attacker:
        raise HTTPException(status_code=404, detail="Incident or Attacker profile missing")
    
    if incident.associated_attackers is None:
        incident.associated_attackers = []
        
    incident.associated_attackers.append(attacker)
    await incident.save()
    return {"status": f"Attacker {attacker.ip_address} mapped to Incident '{incident.title}'"}

# ==================== CRUD: DELETE & DROP ====================
@app.delete("/attackers/{attacker_id}", tags=["Attackers"])
async def purge_attacker(attacker_id: PydanticObjectId):
    attacker = await Attacker.get(attacker_id)
    if not attacker:
        raise HTTPException(status_code=404, detail="Attacker not found")
    await attacker.delete()
    return {"status": f"Attacker record {attacker_id} permanently erased."}

@app.delete("/system/drop-alerts", tags=["System Maintenance"])
async def drop_alerts_collection():
    await Alert.get_motor_collection().drop()
    return {"status": "Alerts collection dropped completely."}