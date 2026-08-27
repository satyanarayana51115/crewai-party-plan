# Multi-Agent Party Planner (Enchanted Forest Masquerade)

An autonomous multi-agent AI system built using **CrewAI** that collaborates to conceptualize, schedule, and execute complex event experiences. The agents handle high-dimensional planning, including guest seating dynamics, chronological music architecture, and real-time execution flows.

---

## 🤖 Multi-Agent Architecture

The architecture delegates specialized event lifecycle tasks to dedicated AI agents:

* **Entertainment & Guest Relations Coordinator (Raju):** Manages guest chemistry, seating layouts, and interactive engagement.
* **Music & Audio Architect:** Curates atmospheric audio transitions (Live Harpist $\rightarrow$ Forest Soundscapes $\rightarrow$ Synth-Wave DJ sets).
* **Logistics & Timeline Specialist:** Constructs precise chronological flow-sheets and zone management.
* **Event Operations Agent:** Handles safety, food/beverage check-ins, and contingency execution.

---

## ✨ Key Features

* **Social Chemistry Seating Layout:** Dynamically pairs guest profiles (Socialites, Academics, Mystics) to optimize conversation flow and eliminate "dead spots."
* **Phase-Based Audio Curation:** Dynamically scales audio profiles from 45 dB background ambient tracks to high-energy dance sets across time windows.
* **Chronological Flow-Sheet Generation:** Formats complete event timelines mapping zones, key activities, soundscapes, and agent interventions into Markdown tables.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** CrewAI
* **LLM Engine:** OpenAI / LangChain Integrations
* **Formatting:** Dynamic Markdown Generation

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone
https://github.com/satyanarayana51115/crewai-party-plan.git
cd crewai-party-plan
```
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

# Past here your model api key
OPENAI_API_KEY=your_openai_api_key
# OR
GEMINI_API_KEY=your_gemini_api_key
python app.py


