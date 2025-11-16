# Medical-Chatbot-Generative-AI


# Clone the repository
git clone https://github.com/ankitaydv2Medical-Chatbot-Generative-AI.git
cd Medical-Chatbot-Generative-AI

# Create the conda environment (full path, works on your PC)
& "$env:USERPROFILE\miniconda3\Scripts\conda.exe" create -n medibot python=3.10 -y

# Activate the environment (your system cannot use 'conda activate')
& "$env:USERPROFILE\miniconda3\Scripts\activate" medibot

# Install project dependencies inside that environment
& "$env:USERPROFILE\miniconda3\Scripts\conda.exe" run -n medibot pip install -r requirements.txt

