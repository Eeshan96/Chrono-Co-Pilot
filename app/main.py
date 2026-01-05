from app.ai import get_ai_response
from app.memory import load_memory, save_memory

def main():
    print("Chrono Copilot (CLI)")
    print("Type /help for commands. Type /quit to exit.\n")

    mode = "present"
    messages = load_memory()

    while True:
        user_input = input("> ").strip()
        if not user_input:
            continue

        if user_input.lower() == "/quit":
            save_memory(messages)  # save before exiting
            print("Saved in the timeline. Bye.")
            break

        if user_input.lower() == "/help":
            print("Commands: /mode past | /mode present | /mode future | /quit")
            continue

        if user_input.lower().startswith("/mode"):
            parts = user_input.split()
            if len(parts) != 2 or parts[1] not in {"past", "present", "future"}:
                print("Usage: /mode past|present|future")
                continue
            mode = parts[1]
            print(f"Mode set to: {mode}")
            continue

        # Add mode into the user's message so the AI follows it
        messages.append({"role": "user", "content": f"[mode={mode}] {user_input}"})
        reply = get_ai_response(messages)

        print("\n" + reply + "\n")

        messages.append({"role": "assistant", "content": reply})
        save_memory(messages)  # persist after each exchange

if __name__ == "__main__":
    main()
