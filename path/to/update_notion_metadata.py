#!/usr/bin/env python3
import os
import glob
import datetime
import yaml

def update_front_matter(file_path):
    """
    指定したMarkdownファイルのYAMLフロントマターに、
    tags、aliases、Relatedのキーを自動追加・更新します。
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if content.startswith('---'):
        # YAMLフロントマターが存在するケース
        parts = content.split('---', 2)
        if len(parts) >= 3:
            # parts[0] は空文字列、parts[1]がYAML部分、parts[2]が本文部分
            yaml_content = parts[1]
            rest = parts[2]
            try:
                data = yaml.safe_load(yaml_content)
                if data is None:
                    data = {}
            except Exception as e:
                print(f"YAML読み込みエラー {file_path}: {e}")
                return
            
            modified = False
            # 既存のtagsプロパティの中身を更新（存在する場合のみ）
            if 'tags' in data:
                default_tags = ["cursor", "AI"]
                if data['tags'] != default_tags:
                    data['tags'] = default_tags
                    modified = True
            # オプション：dateキーがなければ本日の日付をセット
            if 'date' not in data:
                data['date'] = datetime.date.today().isoformat()
                modified = True
            
            if modified:
                new_yaml = yaml.dump(data, allow_unicode=True, default_flow_style=False)
                # YAMLブロックの前後に---を付与して再構築
                new_content = f"---\n{new_yaml}---\n{rest.lstrip()}"
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"更新しました: {file_path}")
        else:
            print(f"YAMLフロントマターが正しくありません: {file_path}")
    else:
        print(f"YAMLフロントマターが存在しません: {file_path}")

def update_directory(directory):
    """
    指定ディレクトリ直下の.mdファイルすべてに対して更新を実施します。
    """
    pattern = os.path.join(directory, '*.md')
    for file_path in glob.glob(pattern):
        update_front_matter(file_path)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='指定したディレクトリ内のMarkdownファイルにfront matter（tags, aliases, Related）を自動で追加/更新します。'
    )
    parser.add_argument('directory', type=str, help='対象ディレクトリのパス')
    args = parser.parse_args()
    update_directory(args.directory) 