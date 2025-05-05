import os
import json

def shrani(q1_value, q2_value, datoteka="odgovori.json"):
    answers = {
        "q1": q1_value,
        "q2": q2_value
    }

    # 1. Shrani v datoteko
    try:
        with open(datoteka, "w", encoding="utf-8") as f:
            json.dump(answers, f, ensure_ascii=False, indent=2)
        print(f"Odgovori uspešno shranjeni v '{datoteka}'")
    except Exception as e:
        print(f"Napaka pri shranjevanju datoteke: {e}")
        return

    # 2. Preveri vsebino
    if not os.path.isfile(datoteka):
        print(f"Napaka: Datoteka '{datoteka}' ne obstaja.")
        return

    try:
        with open(datoteka, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"📂 Vsebina '{datoteka}':")
        for k, v in data.items():
            print(f"  {k}: {v}")
    except json.JSONDecodeError:
        print(f"Napaka: Datoteka '{datoteka}' ni v veljavnem JSON formatu.")
