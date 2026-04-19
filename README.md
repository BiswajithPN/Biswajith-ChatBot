# 🤖 Bisbot - AI-Powered Conversational Platform

> Experience cutting-edge AI conversations powered by Groq's lightning-fast infrastructure.

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.55+-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Groq API](https://img.shields.io/badge/Groq-API-FF6B00?style=for-the-badge)](https://www.groq.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

## 🌟 Features

- ⚡ **Lightning Fast** - Powered by Groq's advanced inference engine with sub-millisecond response times
- 🎨 **Premium UI** - Beautiful, modern dark theme interface optimized for professional use
- 🔒 **Secure & Private** - Enterprise-grade security with environment variable management
- 🌐 **Web-Based** - Built with Streamlit for seamless browser-based interaction
- 🧠 **Advanced AI** - Leverages state-of-the-art language models for intelligent conversations
- ⚙️ **Easy Setup** - Simple installation and configuration with minimal dependencies

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Groq API Key (get one at [groq.com](https://www.groq.com/))

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/BiswajithPN/Biswajith-ChatBot.git
cd Biswajith-ChatBot
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

**To get your Groq API Key:**
1. Visit [console.groq.com](https://console.groq.com/)
2. Sign up or log in to your account
3. Generate a new API key
4. Copy and paste it into your `.env` file

### 5. Run the Application

```bash
streamlit run biswajith_chatbot.py
```

The application will open in your browser at `http://localhost:8501`

## 💻 Usage

1. **Start the Application** - Run the command above
2. **Type Your Message** - Enter your question or prompt in the chat interface
3. **Get Instant Responses** - Receive real-time, intelligent answers powered by AI
4. **Customize** - Modify the styling and configurations as needed

## 📦 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Programming language |
| **Streamlit** | Web application framework |
| **Groq API** | AI inference engine |
| **python-dotenv** | Environment variable management |
| **HTML5 & CSS3** | Frontend styling |

## 📂 Project Structure

```
Biswajith-ChatBot/
├── biswajith_chatbot.py    # Main application file
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not in repo)
├── README.md               # This file
├── README.html             # Premium HTML documentation
└── run_localhost.bat       # Windows batch file to run locally
```

## 🎨 Premium Documentation

For a beautiful, interactive version of this documentation with full styling, visit the [README.html](README.html) file or view it in your browser.

## 🔧 Configuration

### Customizing the UI

The application includes comprehensive CSS styling that can be modified in the `PAGE_CSS` variable within `biswajith_chatbot.py`. Customize colors, fonts, and layouts to match your preferences.

### API Configuration

The application uses the Groq API for AI inference. You can:
- Change the model by modifying the inference call
- Adjust response parameters
- Implement custom system prompts

## 🐛 Troubleshooting

**Issue: "API Key not found"**
- Make sure your `.env` file is in the project root
- Verify the `GROQ_API_KEY` is correctly set
- Restart the application after adding the key

**Issue: "Module not found"**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check you're using the correct Python environment

**Issue: Port 8501 already in use**
- Run on a different port: `streamlit run biswajith_chatbot.py --server.port 8502`

## 📝 Requirements

```
streamlit==1.55.0
groq
python-dotenv
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests
- Share feedback

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Biswajith**

- GitHub: [@BiswajithPN](https://github.com/BiswajithPN)
- Project: [Biswajith-ChatBot](https://github.com/BiswajithPN/Biswajith-ChatBot)

## 🙏 Acknowledgments

- [Groq](https://www.groq.com/) - For providing the lightning-fast AI inference engine
- [Streamlit](https://streamlit.io/) - For the amazing web framework
- [OpenAI](https://openai.com/) - For AI advancements that inspire this project

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the [README.html](README.html) for visual documentation
3. Open an issue on GitHub
4. Reach out to the author

---

<div align="center">

**Made with ❤️ by Biswajith**

🌟 If you find this project helpful, please consider giving it a star! ⭐

</div>
