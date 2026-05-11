from app.core.schemas import IntentResult, PolicyResult
from app.data.policies import BANK_POLICIES

class PolicyNode:
    def process(self, intent_result: IntentResult) -> PolicyResult:
        """
        Dựa trên Intent (ý định) đã nhận diện, truy xuất chính sách ngân hàng tương ứng.
        """
        # Lấy nhãn ý định từ kết quả của IntentNode
        intent = intent_result.intent.lower()
        
        print(f"Đang tìm kiếm chính sách cho ý định: {intent}...")
        
        # Tìm nội dung chính sách trong BANK_POLICIES (file app/data/policies.py)
        # Nếu không tìm thấy nhãn chính xác, sẽ trả về nội dung mặc định (default)
        policy_content = BANK_POLICIES.get(intent, BANK_POLICIES["default"])
        
        # Trả về đối tượng PolicyResult theo đúng Schema đã định nghĩa
        return PolicyResult(
            policy_content=policy_content,
            source="Hệ thống tri thức nội bộ Ngân hàng"
        )