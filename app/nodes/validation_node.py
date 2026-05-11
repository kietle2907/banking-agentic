from app.core.schemas import IntentResult, PriorityResult

class ValidationNode:
    def process(self, draft_reply: str, intent: IntentResult, priority: PriorityResult) -> dict:
        print("Đang kiểm duyệt câu trả lời...")
        
        # Kiểm tra độ dài câu trả lời
        if len(draft_reply.strip()) < 15:
            return {"is_valid": False, "feedback": "Câu trả lời quá ngắn hoặc trống."}
        
        # (Tùy chọn) Có thể kiểm tra thêm từ khóa cảnh báo nếu là lỗi mạng từ Ollama
        if "quá tải" in draft_reply.lower() or "xin lỗi, tôi không thể" in draft_reply.lower():
             return {"is_valid": False, "feedback": "AI không thể tạo câu trả lời hợp lệ."}
        
        # Nếu mọi thứ ổn
        return {"is_valid": True, "feedback": "Câu trả lời đạt chuẩn."}