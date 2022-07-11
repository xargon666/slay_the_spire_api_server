import pytest
import app
from controllers import relics


@pytest.fixture
def api(monkeypatch):
    test_data = [
        {
            "Burning Blood",
            "Starter",
            "Ironclad",
            "At the end of combat, heal 6 HP.",
            "Your body" "s own blood burns with an undying rage.",
            "",
        },
        {
            "Cracked Core",
            "Starter",
            "Defect",
            "At the start of each combat, Channel 1 Lightning.",
            "The mysterious life force which powers the Automatons within the Spire. It appears to be cracked.",
            "",
        },
        {
            "Pure Water",
            "Starter",
            "Watcher",
            "At the start of each combat, add a Miracle into your hand.",
            "Filtered through fine sand and free of impurities.",
            "",
        },
        {
            "Ring of the Snake",
            "Starter",
            "Silent",
            "At the start of each combat, draw 2 additional cards.",
            "Made from a fossilized snake. Represents great skill as a huntress.",
            "",
        },
    ]
    monkeypatch.setattr(relics, "db", test_data)
    api = app.app.test_client()
    return api
