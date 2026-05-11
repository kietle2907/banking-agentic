import requests
import json

# URL của server Agent chúng ta vừa chạy
API_URL = "http://localhost:8001/api/chat"

# Các trường hợp test giả lập tin nhắn khách hàng
test_cases = [
    "Tôi bị rơi mất thẻ tín dụng hôm qua, làm sao để khóa thẻ?",  # Intent: lost_or_stolen_card (Priority: High)
    "Tôi chuyển khoản cho bạn tôi từ sáng mà giờ nó vẫn chưa nhận được", # Intent: transfer_not_received_by_recipient (Priority: Medium)
    "Cho tôi hỏi phí duy trì tài khoản hàng tháng là bao nhiêu?" # Intent: thông tin chung (Priority: Low)
]

print("BẮT ĐẦU KIỂM THỬ AI AGENT...\n" + "="*40)

for msg in test_cases:
    print(f"\n[Khách hàng]: {msg}")
    
    # Gửi request lên server
    payload = {"message": msg}
    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        print(f"[Ý định nhận diện]: {result['intent']}")
        print(f"[Mức độ ưu tiên]: {result['priority'].upper()}")
        print(f"[Hành động]: {result['status']}")
        print(f"[AI Agent trả lời]: {result['draft_reply']}")
    else:
        print(f"Lỗi kết nối: {response.status_code} - {response.text}")