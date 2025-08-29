from flask import Flask, request, jsonify

app = Flask(__name__)


FULL_NAME = "shivam_singh"
DOB = "10022003"  
EMAIL = "sksinghmunger2002@gmail.com"
ROLL_NUMBER = "22BPS1132"

def alternating_caps_reverse(s: str) -> str:
    s = s[::-1]  
    result = ""
    upper = True
    for ch in s:
        if ch.isalpha():
            result += ch.upper() if upper else ch.lower()
            upper = not upper
    return result

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.json.get("data", [])

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_chars = []
        total_sum = 0

        for item in data:
            if item.isdigit():
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif item.isalpha():
                alphabets.append(item.upper())
            else:
                special_chars.append(item)

        concat_str = alternating_caps_reverse("".join([x for x in data if x.isalpha()]))

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(total_sum),
            "concat_string": concat_str
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400


if __name__ == "__main__":
    app.run()
