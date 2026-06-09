import requests
import json

class OllamaService:
    def __init__(self, model="llama3", base_url="http://127.0.0.1:11434"):
        self.model = model
        self.base_url = base_url


    def generate_response(self, prompt):
        """
        Calls Ollama via HTTP with a fallback to the CLI.
        """
        # 1. Try HTTP first (preferred)
        addresses = [self.base_url, "http://127.0.0.1:11434", "http://localhost:11434"]
        for url_base in addresses:
            try:
                session = requests.Session()
                session.trust_env = False
                # Increase timeout to 45s for local inference
                response = session.post(
                    f"{url_base}/api/generate",
                    json={"model": self.model, "prompt": prompt, "stream": False},
                    timeout=45
                )
                if response.status_code == 200:
                    return response.json().get("response")
            except Exception as e:
                print(f"DEBUG: HTTP attempt to {url_base} failed: {str(e)}")
                continue

        # 2. CLI Fallback (Bypasses networking layer)
        try:
            import subprocess
            print(f"DEBUG: HTTP failed. Trying CLI fallback for model {self.model}...")
            # Use a more robust list-based command for subprocess to handle quoting
            cmd = ["ollama", "run", self.model, prompt]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=60, # Even longer for CLI
                shell=True # Required for 'ollama' in Windows PATH
            )
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return f"Ollama CLI Error (Code {result.returncode}): {result.stderr}"
        except Exception as e:
            return f"Ollama Connection Failed (HTTP & CLI): {str(e)}"




    def analyze_research_data(self, user_data, prediction):
        """
        Specific analysis for the Research Lab full dataset.
        """
        prompt = f"""
        System: You are an expert institutional stress analyst.
        Data: {json.dumps(user_data)}
        Prediction: {prediction}
        
        Task: Provide a deep clinical insight into why the student is at this stress level based on ALL 21 parameters.
        Focus on the interaction between academic pressure, environmental safety, and personal mental health history.
        Keep it professional and concise (max 200 words).
        """
        return self.generate_response(prompt)
