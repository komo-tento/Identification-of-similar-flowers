from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from inference import predict  # 自作のpredictモジュールをインポート
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# 画像を保存するディレクトリを指定
UPLOAD_DIR = "static/Uploaded_images"
# 指定したディレクトリが存在しない場合、ディレクトリを作成
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@app.get("/")
def main():
    # HTMLファイルを返す
    return FileResponse("index.html")

@app.post("/predict")
async def upload_file(file: UploadFile = File(...)):
    # アップロードされたファイルを指定のディレクトリに保存するパスを指定
    input_image_path = os.path.join(UPLOAD_DIR, file.filename)
    
    # アップロードされたファイルを指定したパスに保存
    with open(input_image_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # predict関数を呼び出して推論結果を取得
    result_text = predict(input_image_path)
    # アップロードされた画像のプレビューを表示
    app.mount("/static", StaticFiles(directory="static"), name="static")
    image_preview = f"<img src='http://127.0.0.1:8000/{input_image_path}' alt='アップロードされた画像' width=300>"
    

    print(f"image_preview{image_preview}")
    
    # 推論結果と画像プレビューをHTML形式で返す
    return HTMLResponse(
        f"""
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <title>判定結果</title>
        </head>
        <body>
        <h2>判定結果</h2>
        <div class="result-container">
            <p>{result_text}</p>
            <p id=image-preview><img src='http://127.0.0.1:8000/{input_image_path}' alt='アップロードされた画像' width=300></p>
        </div>
        </body>
        """
    )