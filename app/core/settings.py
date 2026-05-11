from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # URL của server Ollama (mặc định hoặc từ Pinggy nếu bạn chạy remote)
    OLLAMA_BASE_URL: str = "http://lyycs-34-125-176-117.run.pinggy-free.link"
    
    # Tên mô hình LLM dùng để soạn thảo phản hồi
    RESPONSE_MODEL: str = "gpt-oss:20b"
    
    # Đường dẫn hoặc tên mô hình đã fine-tune từ Lab 2 cho việc nhận diện intent
    INTENT_MODEL_PATH: str = "configs/inference.yaml"

    class Config:
        env_file = ".env"

settings = Settings()