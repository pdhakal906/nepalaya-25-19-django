import requests
import os

# from dotenv import load_dotenv

# load_dotenv()


import os
import requests

# current_dir = os.path.dirname(os.path.abspath(__file__))


def format_response(status, message, data=""):
    return {"STATUS": status, "MESSAGE": message, "DATA": data}


def extract_text(image_path):
    # api_key = os.getenv("API_KEY")
    api_key = "API_KEY_HERE"  # Replace with your actual API key

    api_url = "https://api.ocr.space/parse/image"
    if not api_key:
        return format_response("ERROR", "API KEY NOT FOUND", data="")

    try:
        with open(image_path, "rb") as image_file:
            files = {"file": image_file}
            data = {
                "apikey": api_key,
                "language": "eng",
                "OCREngine": 2,
            }

            response = requests.post(api_url, files=files, data=data)
            print(response.json())
            response.raise_for_status()

            result = response.json()
            if result.get("OCRExitCode") == 1:
                return format_response(
                    "SUCCESS",
                    "Data Extracted",
                    data=result.get("ParsedResults")[0].get("ParsedText"),
                )
            else:
                return format_response(
                    "ERROR", result.get("ErrorMessage", ["OCR FAILED"])[0], data=""
                )

    except FileNotFoundError as e:

        return format_response(
            "ERROR",
            f"Image file '{image_path}' not found.",
            data="",
        )

    except requests.RequestException as e:

        return format_response("ERROR", f"API Request failed: {str(e)}", data="")

    except (KeyError, ValueError) as e:

        return format_response("ERROR", f"Invalid API response: {str(e)}", data="")

    except Exception as e:

        return format_response(f"ERROR", f"Something went wrong:{str(e)}", data="")
