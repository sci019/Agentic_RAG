# 導入方法

1. ollamaインストール
```shell
curl -fsSL https://ollama.com/install.sh | sh
sudo systemctl stop ollama
sudo systemctl disable ollama
```

2. ollamaモデルのpull
```shell
ollama serve & ollama_PID=$!
ollama pull llama3.1:8b ; kill $ollama_PID
```

3. Pythonパッケージ
```shell
python -m venv agent_env
source agent_env/bin/activate
pip install -r requirements.txt
```
```shell
python -V
# Python 3.12.3
```

4. Agentic RAG 実行
```shell
ollama serve & ollama_PID=$!
python test.py ; kill $ollama_PID
```

