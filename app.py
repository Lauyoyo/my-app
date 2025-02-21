from flask import Flask, jsonify #Response
import os
# import json

# 创建 Flask 应用实例
app = Flask(__name__)

# 1. Hello World 路由
@app.route('/')
def hello_world():
    return 'Hello, World!'

# 2. 统计文件数量路由
@app.route('/count-files')
def count_files():
    folder_path = './public'  # 目标文件夹路径

    # 检查 public 文件夹是否存在
    if not os.path.exists(folder_path):
        # return Response(json.dumps({'error': 'public 文件夹不存在'}, ensure_ascii=False), content_type='application/json')
        return jsonify({'error': 'The "public" folder does not exist.'}), 404

    # 统计文件数量
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    file_count = len(files)

    # response_data = {'message': f"public 文件夹中共有 {file_count} 个文件。"}
    # return Response(json.dumps(response_data, ensure_ascii=False), content_type='application/json')
    return jsonify({'message': f'There are {file_count} files in the "public" folder.'})

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(debug=True, port=5000)
