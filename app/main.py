from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 定義職缺的資料格式 (這就像 Java 的 DTO 或 Entity)
class JobApplication(BaseModel):
    company: str
    position: str
    status: str = "Pending"  # 預設狀態是「待定」
    salary_range: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "只是秀在頁面上的文字!"}

# 新增一個 API 接口：用來「建立」職缺
@app.post("/jobs/")
def create_job(job: JobApplication):
    # 這裡我們先簡單回傳我們收到的資料，之後會教你怎麼存進資料庫
    return {"message": "成功收到職缺資料！", "data": job}




#from fastapi import FastAPI
#
#app = FastAPI()
#
#@app.get("/")
#def read_root():
#    return {"message": "Smart Job Tracker API is running!"}