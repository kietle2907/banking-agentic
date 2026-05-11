import requests
from app.core.schemas import CustomerRequest, IntentResult
from app.core.settings import settings

class IntentNode:
    def __init__(self):
        # Dùng URL từ settings và trỏ tới /api/intent
        self.api_url = f"{settings.OLLAMA_BASE_URL}/api/intent"
        print("Intent Node đã cấu hình để dùng API trên Google Colab.")

    def process(self, request: CustomerRequest) -> IntentResult:
        try:
            print(f"Đang gửi câu hỏi lên AI trên Colab...")
            response = requests.post(self.api_url, json={"message": request.message})
            response.raise_for_status()
            data = response.json()
            return IntentResult(intent=data["intent"], confidence=data["confidence"])
        except Exception as e:
            print(f"Lỗi khi gọi mô hình trên Colab: {e}")
            return IntentResult(intent="unknown", confidence=0.0)