from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    if not data:
        return jsonify({"status": "error", "message": "No JSON payload received"}), 400

    action = data.get("action")
    symbol = data.get("symbol")
    price = data.get("price")
    risk = data.get("risk", 0.005)

    print(f"Signal ተቀብሏል: Action={action} | Symbol={symbol} | Price={price} | Risk={risk}")

    # =========================================================================
    # የትሬድ ኤክሲኪዩሽን ቦታ (Execution Logic)
    # -------------------------------------------------------------------------
    # እዚህ ቦታ ላይ ከ Broker (Bybit/Exness/MetaTrader API) ጋር በማገናኘት
    # ትሬድ በራስ-ሰር እንዲከፈት ማድረግ ትችላለህ።
    # =========================================================================

    return jsonify({"status": "success", "message": f"{action} order processed for {symbol}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
