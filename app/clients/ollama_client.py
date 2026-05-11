import requests
from app.clients.base import BaseClient
from app.core.settings import settings

class OllamaClient(BaseClient):
    def __init__(self):
        # Lấy đường dẫn URL của Ollama từ file cấu hình (ví dụ: http://localhost:11434)
        self.base_url = settings.OLLAMA_BASE_URL
        self.model = settings.RESPONSE_MODEL

    def generate_response(self, prompt: str) -> str:
        url = f"{self.base_url}/api/generate"
        
        # Đóng gói dữ liệu gửi đi
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False # Trả về toàn bộ câu trả lời một lần thay vì từng chữ
        }
        
        try:
            # Gửi yêu cầu đến Ollama
            response = requests.post(url, json=payload)
            response.raise_for_status() # Kiểm tra xem có lỗi mạng không
            
            # Lấy nội dung câu trả lời
            result = response.json()
            return result.get("response", "Xin lỗi, tôi không thể tạo câu trả lời lúc này.")
        except Exception as e:
            print(f"Lỗi khi gọi Ollama: {e}")
            return "Hiện tại hệ thống đang quá tải, vui lòng thử lại sau."