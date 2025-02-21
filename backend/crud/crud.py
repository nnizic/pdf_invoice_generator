from fastapi import APIRouter, Depends, HTTPException
from database import dynamodb
from models import InvoiceCreate
import uuid

router = APIRouter()

@router.post("/create")
async def create_invoice(invoice: InvoiceCreate):
    table = dynamodb.Table("Invoices")
    invoice_id = str(uuid.uuid4())
    table.put_item(Item={"id": invoice_id, **invoice.dict()})
    return {"id": invoice_id, "message": "Invoice created"}

