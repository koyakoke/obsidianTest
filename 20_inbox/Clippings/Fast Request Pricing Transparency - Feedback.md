---
title: "Fast Request Pricing Transparency - Feedback"
source: "https://forum.cursor.com/t/fast-request-pricing-transparency/42161?utm_source=chatgpt.com"
author:
  - "[[andresreibel]]"
published: 2025-01-17
created: 2025-05-25
description: "Cursor Team, Given the discussions around issues with slow requests, can you create 100% transparency around pricing for fast requests. What would really hep is a quick calculator (or at least a look up table) in this …"
tags:
  - "clippings"
---
## 迅速なリクエスト価格の透明性

[フィードバック](https://forum.cursor.com/c/feedback/7)

[アンドレスレイベル](https://forum.cursor.com/u/andresreibel)

[1月17日](https://forum.cursor.com/t/fast-request-pricing-transparency/42161 "投稿日")

カーソルチーム、

遅いリクエストに関する問題についての議論を考慮すると、高速なリクエストの価格設定について 100% の透明性を実現できますか。

本当に役立つのは、次のような簡単な計算機（または少なくとも参照表）です: [OpenAI API 料金計算ツール | gptforwork.com](https://gptforwork.com/tools/openai-chatgpt-api-pricing-calculator)

私の理解するところ、追加の大きなコンテキストの Claude Sonnet 3.5 リクエスト (500 件) を支払う方法は 3 つあります。

1. [設定 | カーソル - AIコードエディター](https://www.cursor.com/settings) → $20/500リクエストで高速リクエストを追加
2. [設定 | カーソル - AI コードエディター](https://www.cursor.com/settings) → 使用量ベースの料金設定を 100 ドル/500 リクエスト (リクエストあたり 0.2 ドル) で有効にします
3. Anthropic APIキー（IDE設定内）→同僚が前回の投稿で500リクエストあたり15.00ドルと見積もっています

私の価格設定が正しいかどうかを明確にしていただけますか?

ありがとう

[ダンパークス](https://forum.cursor.com/u/danperks) コミュニティ開発者

[1月17日](https://forum.cursor.com/t/fast-request-pricing-transparency/42161/2 "投稿日")

ねえ、もうすぐそこだけど、2番目の方がずっと安いよ！

Claude 3.5 Sonnetの場合、リクエストは通常と同じ料金（1リクエストあたり0.04ドル）で、毎月請求されます。500リクエストご利用の場合、通常と同じ20ドルの料金となります。

API キーを直接購入すると安くなる場合もありますが、弊社の従量課金制をご利用いただくと、API キーを管理したり、Anthropic で課金を設定したりする必要がなくなり、Cursor の開発サポートにも貢献できます。

[アンドレスレイベル](https://forum.cursor.com/u/andresreibel)

[1月18日](https://forum.cursor.com/t/fast-request-pricing-transparency/42161/3 "投稿日")

こんにちは、

明確にしておきたいのは、ユーザーベースの価格設定を使用する場合、Anthropic API キーを直接使用して支払う金額に加えてマージンを請求するということですか?

それが正しい場合、上乗せして請求するマージンはいくらですか?

ありがとう、  
アンドレス

[イドハム](https://forum.cursor.com/u/idham)

ダンパークス

[1月19日](https://forum.cursor.com/t/fast-request-pricing-transparency/42161/5 "投稿日")

ヘルプページに記載されているように、使用量ベースの料金がリクエスト500件ごとに請求されるというのはどういう意味ですか？ 毎月の使用量に対して最低20ドルかかるという意味ですか、それともリクエストが500件に達した時点で請求が発生するという意味ですか？

使用量ベースの価格設定は GPT-4o にも適用されますか?

ありがとう

[ダンパークス](https://forum.cursor.com/u/danperks) コミュニティ開発者

[1月21日](https://forum.cursor.com/t/fast-request-pricing-transparency/42161/6 "投稿日")

おい！

Claude 3.5 Sonnet、GPT-4o、GPT-4 はすべて 1 リクエストあたり 0.04 ドルで販売されます。

デフォルトでは、月末に使用量に応じた料金が請求されます。  
ただし、使用量が20ドルに達した場合は、すぐに請求させていただきます。  
ただし、使用量に応じて20ドル未満でご利用いただくことも可能です。

13日後

[短い](https://forum.cursor.com/u/short)

[2月4日](https://forum.cursor.com/t/fast-request-pricing-transparency/42161/7 "投稿日")

[ダンさん、アカウント設定の「使用状況」セクション（設定 | カーソル - AIコードエディター）](https://www.cursor.com/settings) に、この情報を公式形式で入力してもらえませんか ？

新しいモデルが次々と追加されているので、何がプレミアムプランとしてカウントされるのか全く分かりません。また、各使用ログも消えてしまったようです。これは全く透明性がありません。別のスレッドで、deepseek-v3はプレミアムプランではない、つまり常に高速で制限がないとおっしゃっていましたが、これはお客様にとって非常に有益な情報だと思います。

[ディーンリー](https://forum.cursor.com/u/deanrie)

[2月4日](https://forum.cursor.com/t/fast-request-pricing-transparency/42161/8 "Post date")

こんにちは、価格の詳細はこのページで確認できます:

[短い](https://forum.cursor.com/u/short)

[2月5日](https://forum.cursor.com/t/fast-request-pricing-transparency/42161/9 "Post date")

[素晴らしいですね、ありがとうございます。Cursorをかなり長い間使っていますが、こんな機能があることは知りませんでした。設定 | Cursor - AIコードエディターの](http://cursor.com/settings) 古い情報を更新し 、このドキュメントへのリンクを追加することをお勧めします。

矛盾する情報もあります。gpt-4o-miniは無料ですか、それともプロプランのプレミアムですか？もう少し改善が必要です。

  

原文

この翻訳を評価してください

いただいたフィードバックは Google 翻訳の改善に役立てさせていただきます