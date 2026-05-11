from app.core.schemas import PriorityResult

class RouterNode:
    def process(self, validation_result: dict, priority: PriorityResult, draft_reply: str) -> dict:
        print("Đang ra quyết định điều hướng...")
        
        # 1. Nếu câu trả lời không hợp lệ, lập tức chuyển cho nhân viên
        if not validation_result["is_valid"]:
            return {
                "action": "escalated", 
                "final_response": "Xin lỗi, hiện tại hệ thống tự động không thể đưa ra giải pháp hoàn chỉnh. Yêu cầu của bạn đang được chuyển đến nhân viên hỗ trợ trực tiếp."
            }
        
        # 2. Nếu ưu tiên cao (high risk), gửi câu trả lời nhưng vẫn cảnh báo chuyển nhân viên
        if priority.level == "high":
            return {
                "action": "escalated", 
                "final_response": f"{draft_reply}\n\n[Hệ thống: Sự cố của bạn thuộc nhóm rủi ro cao. Chúng tôi đã ưu tiên chuyển tiếp thông tin này cho Chuyên viên bảo mật để hỗ trợ bạn ngay lập tức.]"
            }
        
        # 3. Các trường hợp bình thường, gửi câu trả lời của AI
        return {
            "action": "sent", 
            "final_response": draft_reply
        }