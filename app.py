import os
import base64
import boto3
import json
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB max

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_bedrock_client():
    return boto3.client(
        service_name='bedrock-runtime',
        region_name=os.environ.get('AWS_REGION', 'us-east-1')
    )

def encode_image(image_bytes):
    return base64.b64encode(image_bytes).decode('utf-8')

def ask_nova_about_image(image_bytes, image_media_type, question):
    client = get_bedrock_client()
    image_b64 = encode_image(image_bytes)

    body = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "image": {
                            "format": image_media_type.split("/")[1],
                            "source": {
                                "bytes": image_b64
                            }
                        }
                    },
                    {
                        "text": question
                    }
                ]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 1024,
            "temperature": 0.7
        }
    }

    response = client.invoke_model(
        modelId="amazon.nova-pro-v1:0",
        body=json.dumps(body)
    )

    result = json.loads(response['body'].read())
    return result['output']['message']['content'][0]['text']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'Rasm yuklanmadi'}), 400

    file = request.files['image']
    question = request.form.get('question', 'Bu rasmda nima ko\'ryapsiz? Batafsil tushuntiring.')

    if file.filename == '':
        return jsonify({'error': 'Fayl tanlanmagan'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Faqat PNG, JPG, JPEG, GIF, WEBP formatlari qabul qilinadi'}), 400

    image_bytes = file.read()
    ext = file.filename.rsplit('.', 1)[1].lower()
    media_type_map = {
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif',
        'webp': 'image/webp'
    }
    media_type = media_type_map.get(ext, 'image/jpeg')

    answer = ask_nova_about_image(image_bytes, media_type, question)
    return jsonify({'answer': answer, 'question': question})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
