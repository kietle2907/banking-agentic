from app.core.schemas import IntentResult, PriorityResult

class PriorityNode:
    def process(self, request_message: str, intent_result: IntentResult) -> PriorityResult:
        intent = intent_result.intent.lower()
        
        # Các vấn đề bảo mật, rủi ro cao trong BANKING77
        high_risk_intents = ["lost_or_stolen_card", "compromised_card", "card_swallowed", "fraud_or_scam_report"]
        # Các vấn đề thanh toán, giao dịch
        medium_risk_intents = ["declined_card_payment", "declined_transfer", "transfer_not_received_by_recipient"]
        
        if intent in high_risk_intents:
            return PriorityResult(level="high", reason=f"Ý định '{intent}' chứa rủi ro bảo mật hoặc thất thoát tài sản.")
        elif intent in medium_risk_intents:
            return PriorityResult(level="medium", reason=f"Ý định '{intent}' ảnh hưởng đến giao dịch của khách hàng.")
        else:
            return PriorityResult(level="low", reason="Yêu cầu truy vấn thông tin thông thường.")