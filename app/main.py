from fastapi import FastAPI
from app.core.schemas import CustomerRequest, AgentResponse
from app.agent.orchestrator import Orchestrator

# Khởi tạo ứng dụng
app = FastAPI(title="Banking AI Agent")

# Khởi tạo Orchestrator (Nó sẽ tự động tải AI model của bạn vào bộ nhớ)
orchestrator = Orchestrator()

# Tạo cổng giao tiếp POST tại địa chỉ /api/chat
@app.post("/api/chat", response_model=AgentResponse)
def chat_with_agent(request: CustomerRequest):
    """
    Nhận tin nhắn từ khách hàng và trả về câu trả lời từ AI Agent
    """
    # Chỉ cần đưa yêu cầu cho Nhạc trưởng, mọi thứ sẽ được xử lý tự động!
    response = orchestrator.process_request(request)
    return response

@app.get("/")
def read_root():
    return {"message": "Server Banking AI Agent đang hoạt động!"}