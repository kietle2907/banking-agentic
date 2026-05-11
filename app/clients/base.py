class BaseClient:
    def generate_response(self, prompt: str) -> str:
        """
        Hàm cơ bản để sinh câu trả lời từ AI.
        Các class con sẽ ghi đè lên hàm này.
        """
        raise NotImplementedError("Bạn cần triển khai phương thức này trong class con.")