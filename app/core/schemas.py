from pydantic import BaseModel
from typing import List, Optional

# Dữ liệu đầu vào từ khách hàng
class CustomerRequest(BaseModel):
    message: str

# Kết quả từ Intent Node
class IntentResult(BaseModel):
    intent: str
    confidence: float

# Kết quả từ Priority Node
class PriorityResult(BaseModel):
    level: str  # low, medium, high
    reason: str

# Kết quả từ Policy Node
class PolicyResult(BaseModel):
    policy_content: str
    source: str

# Kết quả cuối cùng của Agent
class AgentResponse(BaseModel):
    intent: str
    priority: str
    draft_reply: str
    status: str  # "sent", "need_more_info", "escalated"
    trace: Optional[dict] = None # Dùng để theo dõi quá trình xử lý của các nút