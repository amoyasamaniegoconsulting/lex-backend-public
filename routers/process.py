from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from  database import get_db
from  services.flowService import FlowService
from  errors import AppError

router = APIRouter()

@router.get("/process")
async def read_processes(db: AsyncSession = Depends(get_db)):
    return await FlowService.get_all_processes(db)

@router.get("/process/{process_id}")
async def read_process(process_id: int, db: AsyncSession = Depends(get_db)):
    return await FlowService.get_process_by_id(db, process_id)  # No necesitas try-except aquí
