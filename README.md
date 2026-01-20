🧮 Advanced Smart AI Calculator

An **AI-powered web calculator** built using **Flask** and **OpenAI**, capable of solving mathematical problems in multiple modes including **standard**, **detailed**, and **step-by-step explanations**.
Ideal for learning, teaching, and quick problem-solving.

🚀 Features

* ✅ AI-based math problem solving
* 📘 Multiple modes:

  * **Standard** – Final answer only
  * **Detailed** – Answer with brief explanation
  * **Step-by-Step** – Full calculation steps
* 🕒 Calculation history tracking
* 🌐 Simple and clean web interface

 🛠️ Tech Stack

* **Backend:** Python, Flask
* **AI Model:** OpenAI API
* **Frontend:** HTML
  
📂 Project Structure

```
├── web_calculator.py
├── templates/
│   └── calculator_advanced.html
├── static/
│   └── (css/js if any)
└── README.md
```

---

⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/advanced-smart-ai-calculator.git
cd advanced-smart-ai-calculator
```

2️⃣ Install Dependencies

```bash
pip install flask openai
```

3️⃣ Configure OpenAI API Key

Add your OpenAI API key in `web_calculator.py`:

```python
client = OpenAI(
    api_key="YOUR_API_KEY"
)
```

4️⃣ Run the Application

```bash
python web_calculator.py
```

5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

📌 Use Cases

* Students learning mathematics
* Teachers demonstrating problem-solving
* Developers integrating AI calculators
* Anyone needing explainable math solutions
  
📸 Screenshots

* ![HomePage Image](https://github.com/harshitaverma11/Advanced_Smart_AI_Calculator/blob/6c17ae937aadc4941bb3b55c031b4e196fc30af2/Screenshot%202026-01-20%20180924.png)
👩‍💻 Author

**Harshita Verma**
Student | AI & Web Enthusiast

⭐ If you like this project, don’t forget to star the repository!
