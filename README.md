# Usage

## 環境構築の手順

1. リポジトリのクローン
```bash
git clone <repo>
```

2. 仮想環境の作成とアクティベート、ライブラリのインストール
```bash
python -m venv .venv \
    && source .venv/bin/activate \
    && pip install -r requirements.txt
```

## スクリプトの種類

### Text to Text Transfer Transformer (T2T) のサンプルコード

```bash
$ python t2t.py
人生の目的は、自分らしく生きることです。それは、自分の情熱を追求し、夢を叶え、他者に貢献することです。自分らしく生きるとは、ありのままの自分を愛し、自分の価値観に従って行動することです。
```

### Image to Text(I2T) のサンプルコード

```bash
$ python t2i.py
The meaning of life is a deeply personal and subjective question with no one definitive answer. It can be a combination of finding purpose, fulfillment, and happiness through relationships, work, hobbies, or spiritual beliefs.
```

### 生成コンテンツをストリーミングで取得する、CURLコマンドのスクリプト

```bash
$ ./script.sh
```

### 生成コンテンツをストリーミングで取得する、CURLコマンドのスクリプト

```bash
$ ./script-stream-generate-content.sh
            "text": "In the vibrant community of Everglen, nestled among rolling hills and sparkling rivers,"
            "text": " lived a young girl named Anya. Anya was known throughout the town for her adventurous spirit and insatiable curiosity. One day, while exploring the attic of her grandmother'"
            "text": "s house, she stumbled upon a peculiar backpack hidden behind a stack of old boxes. Intrigued, she pulled it out and examined it closely.\n\nThe backpack was made of a soft, shimmering fabric that seemed to change color with the light. Its straps were adorned with intricate designs, and a series of small,"
```
