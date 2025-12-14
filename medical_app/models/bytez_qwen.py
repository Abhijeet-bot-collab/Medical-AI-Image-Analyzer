import os
from bytez import Bytez
from dotenv import load_dotenv

load_dotenv()

Bytez_API_KEY = os.getenv("BYTEZ_API_KEY")


if not Bytez_API_KEY:
       raise ValueError("❌ BYTEZ_API_KEY not found in .env file")
sdk = Bytez(Bytez_API_KEY)

# Load Qwen model
model = sdk.model("Qwen/Qwen3-4B-Instruct-2507")

def run_qwen(messages):
    result = model.run(messages)

    # Handle multiple return formats safely
    if isinstance(result, tuple):
        output = result[0]
        error = result[1] if len(result) > 1 else None
    else:
        output = result
        error = None

    if error:
        return f"❌ Error: {error}"

    return output

