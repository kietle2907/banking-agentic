from app.core.schemas import CustomerRequest, AgentResponse
from app.nodes.intent_node import IntentNode
from app.nodes.priority_node import PriorityNode
from app.nodes.policy_node import PolicyNode
from app.nodes.draft_node import DraftNode
from app.nodes.validation_node import ValidationNode
from app.nodes.router_node import RouterNode

class Orchestrator:
    def __init__(self):
        # Khởi tạo tất cả các nút khi hệ thống bắt đầu chạy
        self.intent_node = IntentNode()
        self.priority_node = PriorityNode()
        self.policy_node = PolicyNode()
        self.draft_node = DraftNode()
        self.validation_node = ValidationNode()
        self.router_node = RouterNode()

    def process_request(self, request: CustomerRequest) -> AgentResponse:
        print(f"\n--- NHẬN YÊU CẦU MỚI: {request.message} ---")
        
        # 1. Nhận diện Ý định [cite: 182]
        intent_result = self.intent_node.process(request)
        
        # 2. Đánh giá Mức độ ưu tiên [cite: 183]
        priority_result = self.priority_node.process(request.message, intent_result)
        
        # 3. Trích xuất Chính sách ngân hàng [cite: 188]
        policy_result = self.policy_node.process(intent_result)
        
        # 4. Nhờ AI dự thảo câu trả lời [cite: 189]
        draft_reply = self.draft_node.process(request.message, intent_result, priority_result, policy_result)
        
        # 5. Kiểm duyệt câu trả lời của AI [cite: 190]
        validation_result = self.validation_node.process(draft_reply, intent_result, priority_result)
        
        # 6. Ra quyết định cuối cùng (Gửi hoặc chuyển nhân viên) [cite: 191]
        routing_decision = self.router_node.process(validation_result, priority_result, draft_reply)
        
        # Gom nhóm thông tin trung gian (trace) để dễ dàng theo dõi lỗi [cite: 192]
        trace = {
            "intent_confidence": intent_result.confidence,
            "priority_reason": priority_result.reason,
            "policy_source": policy_result.source,
            "validation": validation_result
        }
        
        # Trả về kết quả hoàn chỉnh cho khách hàng theo đúng Schema [cite: 126, 127]
        return AgentResponse(
            intent=intent_result.intent,
            priority=priority_result.level,
            draft_reply=routing_decision["final_response"],
            status=routing_decision["action"],
            trace=trace
        )