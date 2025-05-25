---
Related: ["プロジェクト全体をAIが理解しているのはどういう仕組みで理解している？", "クラウドのベクトルDBにチャンク分割してベクトル化したものを保存しているということ？"]
aliases: ["Cursorコードベース解説", "Cursor Codebase機能"]
tags:
- cursor
- AI
- codebase
- embedding
- indexing
---
Cursorの「コードベース（codebase）」とは、現在開いているプロジェクトフォルダ内のすべてのコードファイルを指します。[Zenn](https://zenn.dev/umi_mori/books/ai-code-editor-cursor/viewer/how_to_use_codebase_answers?utm_source=chatgpt.com)


---

### 🧠 コードベース機能とは？

Cursorでは、AIがこのコードベース全体を参照し、開発者の質問に対して関連するコードを検索・分析して回答する「コードベース回答（Codebase Answers）」機能を提供しています。[Zenn+3Cursor+3Cursor+3](https://www.cursor.com/ja/features?utm_source=chatgpt.com)

---

### 💬 使い方の例

- 「この関数の定義はどこ？」
- 「このエラーの原因は？」
- 「この処理の流れを教えて」

といった質問をチャットで行うと、AIがコードベース全体を検索し、関連するコードスニペットやファイルを提示してくれます。[Zenn+4Cursor+4Ainova+4](https://www.cursor.com/ja/features?utm_source=chatgpt.com)

---

### ⚙️ インデックス作成と管理

Cursorは、コードベース内の各ファイルに対して埋め込み（embedding）を作成し、AIがより正確な回答を提供できるようにしています。[Cursor](https://docs.cursor.com/context/codebase-indexing?utm_source=chatgpt.com)

インデックス作成はプロジェクトを開いた際に自動で行われ、新しいファイルが追加された場合も自動的にインデックスが更新されます。[note（ノート）](https://note.com/komzweb/n/n6199475d400b?utm_source=chatgpt.com)

---

### 🛠 高度な設定

大規模なプロジェクトや特定のファイルをインデックスから除外したい場合は、`.cursorignore`ファイルを作成し、無視するファイルやディレクトリを指定できます。[Cursor+1note（ノート）+1](https://docs.cursor.com/context/codebase-indexing?utm_source=chatgpt.com)

これは`.gitignore`と同様の形式で記述します。[Cursor](https://docs.cursor.com/context/codebase-indexing?utm_source=chatgpt.com)

---

### 💡 まとめ

Cursorのコードベース機能を活用することで、プロジェクト全体を俯瞰しながら効率的に開発を進めることができます。特に大規模なコードベースや複雑なロジックを扱う際に、AIの支援を受けながら作業を行うことが可能です。[Ainova](https://generativeinfo365.com/ai%E3%82%B3%E3%83%BC%E3%83%89%E3%82%A8%E3%83%87%E3%82%A3%E3%82%BF%E3%80%8Ecursor%E3%80%8F%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC%EF%BC%81%E6%96%99%E9%87%91%E3%82%84%E5%A7%8B%E3%82%81%E6%96%B9/?utm_source=chatgpt.com)

さらに詳しい情報や設定方法については、Cursorの公式ドキュメントをご参照ください。