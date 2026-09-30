from flask import Flask, request, jsonify
from pathlib import Path
import uuid
import socket
from datetime import datetime

app = Flask(__name__)

PROOF_DIR = Path("/app/rce_proof")
PROOF_DIR.mkdir(parents=True, exist_ok=True)


def server_side_execution():
    """
    Controlled server-side execution proof.

    This function runs INSIDE Machine 3.
    It creates a unique proof artifact so that
    execution can be independently verified.
    """

    proof_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    proof_file = PROOF_DIR / f"rce_proof_{proof_id}.txt"

    proof_content = (
        "RCE EXECUTION PROOF\n"
        f"Proof ID: {proof_id}\n"
        f"Server hostname: {socket.gethostname()}\n"
        f"Execution time: {timestamp} UTC\n"
        "Execution location: Machine 3\n"
    )

    proof_file.write_text(proof_content)

    print(
        f"[RCE-EXECUTION] Server-side execution occurred | "
        f"Proof ID: {proof_id}",
        flush=True
    )

    return {
        "status": "RCE execution confirmed",
        "proof_id": proof_id,
        "hostname": socket.gethostname(),
        "proof_file": str(proof_file)
    }


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "server": "Machine 3",
        "application": "Vulnerable Flask RCE Training Lab",
        "status": "running"
    })


@app.route("/vulnerable", methods=["POST"])
def vulnerable():

    data = request.get_json(silent=True)

    if not data or "expression" not in data:
        return jsonify({
            "error": "expression parameter required"
        }), 400

    expression = data["expression"]

    print(
        f"[RCE-ATTEMPT] Attacker-controlled expression received: "
        f"{expression}",
        flush=True
    )

    # Controlled training sink.
    # Only the laboratory proof function is exposed.
    if expression == "server_side_execution()":

        result = server_side_execution()

        print(
            f"[RCE-SUCCESS] Execution completed | "
            f"Proof ID: {result['proof_id']}",
            flush=True
        )

        return jsonify({
            "message": "Server-side execution completed",
            "execution": result
        }), 200

    print(
        "[RCE] Expression rejected by the training application",
        flush=True
    )

    return jsonify({
        "message": "Expression was not executed",
        "received": expression
    }), 400


@app.route("/proofs", methods=["GET"])
def proofs():

    files = [
        file.name
        for file in PROOF_DIR.glob("rce_proof_*.txt")
    ]

    return jsonify({
        "proof_count": len(files),
        "proof_files": files
    })


if __name__ == "__main__":

    print("=" * 60)
    print("MACHINE 3 - VULNERABLE FLASK RCE TRAINING LAB")
    print("=" * 60)
    print("RCE training endpoint: POST /vulnerable")
    print("Proof directory:", PROOF_DIR)
    print("=" * 60)

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )