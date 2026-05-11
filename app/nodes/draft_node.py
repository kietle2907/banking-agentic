from app.core.schemas import IntentResult, PriorityResult, PolicyResult
from app.clients.ollama_client import OllamaClient

class DraftNode:
    def __init__(self):
        # Khởi tạo client kết nối với Ollama
        self.llm_client = OllamaClient()

    def process(self, request_message: str, intent: IntentResult, priority: PriorityResult, policy: PolicyResult) -> str:
        # 1. Chuẩn bị câu lệnh (prompt) hướng dẫn AI cách trả lời
        prompt = f"""
Bạn là một nhân viên hỗ trợ khách hàng lịch sự và chuyên nghiệp của ngân hàng.
Dựa vào các thông tin sau, hãy viết MỘT câu trả lời ngắn gọn, trực tiếp cho khách hàng.

Thông tin:
- Tin nhắn của khách hàng: "{request_message}"
- Ý định được dự đoán: {intent.intent}
- Mức độ ưu tiên: {priority.level}
- Chính sách/Hướng dẫn của ngân hàng: {policy.policy_content}

Yêu cầu:
- Trả lời bằng tiếng Việt.
- Dựa sát vào "Chính sách/Hướng dẫn" ở trên.
- Không tự bịa thêm thông tin ngoài chính sách.
- Thể hiện sự đồng cảm nếu mức độ ưu tiên là 'high' (cao).

Câu trả lời của bạn:
"""
        
        # 2. Gọi Ollama để sinh câu trả lời
        print("Đang gọi Ollama để soạn thảo câu trả lời...")
        draft_reply = self.llm_client.generate_response(prompt)
        
        return draft_reply.strip()