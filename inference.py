# 自分の環境、条件に合わせて適切に値を代入すること
NUM_CLASSES = 4 # 分類したいクラス数　自分のタスクに合わせて正しい値を代入すること
MODEL_PATH = "Weights/flower_weights.pth"
NUM_CANDIDATES = 1  # 上位2つの推論結果を表示

import torch  # PyTorchのインポート
import torchvision.models as models  # torchvisionの事前訓練済みモデルを使用するためのインポート
import torchvision.transforms as transforms  # 画像の前処理用モジュールのインポート
from PIL import Image  # 画像処理ライブラリPILのインポート
import torch.nn as nn  # ニューラルネットワークモジュールのインポート

# モデル学習と同じ条件で前処理すること
# 画像の前処理（リサイズ、テンソルへの変換、正規化）の設定
transform = transforms.Compose([
    transforms.Resize([224, 224]),  # 画像を224x224にリサイズ
    transforms.ToTensor(),  # 画像をテンソルに変換
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # 画像の正規化
])

# モデル学習と同じモデルを読み込むこと
# 最後の全結合層をNUM_CLASSES分類用に変更し、重みデータのロード
model = models.resnet152(weights='DEFAULT')
model.fc = nn.Linear(model.fc.in_features, NUM_CLASSES)
model.load_state_dict(torch.load(MODEL_PATH))  # 学習済みの重みをロード
model.eval()  # モデルを評価モードに設定

# クラス名のリスト例　自分のクラス名・クラス数に合わせて編集すること
class_names = [
    "airisu  アイリスの花言葉は「希望」「信じる心」「メッセージ」「吉報」「よき便り」「知恵」です",  
    "ayame  あやめの花言葉は「よい便り」「朗報」「メッセージ」「希望」です",
    "hanasyoubu  花菖蒲の花言葉は「うれしい知らせ」「優しい心」「優雅」「心意気」です",
    "kakitubata  杜若の花言葉は「高貴」「思慕」「幸せは必ず来る」です"
]

# 画像を予測する関数
def predict(image_path):
    image = Image.open(image_path)  # 画像を開く
    tensor_image = transform(image).unsqueeze(0)  # 画像をテンソルに変換し、バッチ次元を追加
    outputs = model(tensor_image)  # モデルに画像を入力し、出力を取得
    probabilities = torch.nn.functional.softmax(outputs, dim=1)  # 出力をソフトマックス関数で確率に変換
    top_prob, top_classes = torch.topk(probabilities, NUM_CANDIDATES)  # 上位の確率とクラスのインデックスを取得
    top_prob_percent = [round(prob.item() * 100, 2) for prob in top_prob[0]]  # 確率をパーセンテージに変換
    # クラス名と確率を組み合わせてリストに格納
    predictions = [(class_names[class_idx], prob) for class_idx, prob in zip(top_classes[0], top_prob_percent)]
    results = []
    a_prob=0
    for class_name, prob in predictions:  # クラス名と確率を文字列に変換
        results.append(f"{class_name} : {prob:.2f}%")

    return results  # 予測結果のリストを返す

# 事前にテスト用の画像を1枚ずつ用意しておき、下のようにファイル指定できるようにする
# デバッグ用のmain関数
if __name__ == "__main__":
    image_path = "TestData/Cable3/class0/IMG_1860_wc.jpeg"  # テストする画像のパスを指定
    predictions = predict(image_path)  # 画像を予測する関数を呼び出す
    for p in predictions:  # 予測結果を表示
        print(p)