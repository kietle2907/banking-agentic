# Banking AI-Agent: Hệ thống Hỗ trợ Khách hàng Tự động

## 1. Giới thiệu tổng quan
Dự án này xây dựng một AI Agentic Workflow đơn giản phục vụ trong lĩnh vực ngân hàng. Hệ thống có khả năng tiếp nhận tin nhắn từ khách hàng, phân loại ý định, tra cứu chính sách và tự động soạn thảo phản hồi dựa trên mô hình ngôn ngữ lớn (LLM).

Mục tiêu chính:
- Xây dựng quy trình xử lý tự động (pipeline) cho các yêu cầu ngân hàng.  
- Sử dụng mô hình đã fine-tune từ Lab 2 cho nút nhận diện ý định (Intent Detection).  
- Tích hợp LLM thông qua Ollama để sinh câu trả lời tự động.

## 2. Quy trình hoạt động (Workflow)
Hệ thống hoạt động theo một chuỗi các nút (nodes) điều phối bởi Orchestrator:  

1. Intent Detection Node: Nhận diện ý định khách hàng (sử dụng mô hình Unsloth từ Lab 2).  
2. Priority Node: Đánh giá mức độ ưu tiên (Thấp, Trung bình, Cao) dựa trên nội dung yêu cầu.  
3. Policy Retrieval Node: Tra cứu các FAQ và chính sách ngân hàng liên quan đến ý định đã xác định.  
4. Response Drafting Node: Sử dụng LLM (qua Ollama) để soạn thảo câu trả lời dựa trên chính sách và ngữ cảnh.  
5. Validation Node: Kiểm tra tính hợp lệ và đầy đủ của câu trả lời nháp.  
6. Router Node: Quyết định gửi phản hồi trực tiếp hoặc chuyển yêu cầu cho nhân viên hỗ trợ (Escalation).

## 3. Cấu trúc thư mục
Dự án được tổ chức theo cấu trúc chuẩn để dễ dàng bảo trì và mở rộng:  
```app/agent/```: Chứa Orchestrator điều phối toàn bộ workflow.  
```app/nodes/```: Chứa logic xử lý của từng nút trong hệ thống.  
```app/core/```: Chứa cấu hình (Settings) và khuôn mẫu dữ liệu (Schemas).  
```app/clients/```: Chứa bộ phận kết nối với mô hình LLM (Ollama).  
```app/data/```: Lưu trữ dữ liệu chính sách và FAQ giả lập.  
```configs/```: Chứa mô hình fine-tune và file cấu hình từ Lab 2. 
```examples/```: Các yêu cầu mẫu dùng để kiểm thử hệ thống. 

## 4. Hướng dẫn cài đặt và sử dụng
Bước 1: Chuẩn bị môi trường (Google Colab)
Do yêu cầu về GPU để chạy mô hình Unsloth và Ollama, chúng ta sử dụng Colab làm trung tâm API:

1. Chạy notebook cung cấp bởi giảng viên để khởi động Ollama và Pinggy.  
2. Chạy server trung tâm AI (Unsloth + Ollama Proxy) trên Colab (Cấu hình lại file notebook).
3. Lấy đường dẫn Pinggy URL công khai.

Bước 2: Cấu hình Local

1. Clone dự án về máy tính cá nhân.
2. Cài đặt các thư viện cần thiết:
```bash 
pip install -r requirements.txt
```
3. Cập nhật đường dẫn Pinggy vào file ```app/core/settings.py```:
```bash 
OLLAMA_BASE_URL = "http://<your-pinggy-link>.a.pinggy.io"
```

Bước 3: Khởi chạy hệ thống

1. Chạy server FastAPI:
```bash
python run.py
```
2. Thực hiện kiểm thử bằng script mẫu:
```bash
python examples/test_agent.py
```

## 5. Video Demo
https://drive.google.com/file/d/16-jUAmyIiV2jttA6IDcb5lP0ZxxolJ_s/view?usp=sharing
