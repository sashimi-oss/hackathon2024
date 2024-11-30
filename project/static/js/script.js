'use strict'; // おまじない

console.log('hannnoushiteiru?????????????????????');
const table = document.querySelector('table'); // 表
const question = document.getElementById('question'); // 質問
const category = document.querySelector('select'); // 質問形式
const order = document.querySelector('input[type="number"]'); // 順番
const submit = document.getElementById('submit'); // 登録ボタン

const orderSet = new Set(); // 順番を一意にするため

// 質問登録ボタン
submit.addEventListener('click', () => {
  const item = {}; // 入力値を一時的に格納するオブジェクト

  // itemオブジェクトの要素
  if (question.value != '') {
    item.question = question.value;
  } else {
    window.alert('質問を入力してください');
    return;
  }
  if (category.value != '') {
    item.category = category.value;
  } else {
    window.alert('形式を入力してください');
    return;
  }
  if (order.value != '') {
    if (order.value <= 0) {
      window.alert('正の値を入力してください');
      return;
    } else {
      if (!orderSet.has(order.value)) {
        orderSet.add(order.value);
        item.order = order.value;
      } else {
        window.alert('一意な番号を入力してください');
        return;
      }
    }
  } else {
    window.alert('順番を入力してください');
    return;
  }

  console.log(item); // itemオブジェクト確認用

  // フォームをリセット
  question.value = '';
  category.value = '選択';

  const arrayOrderSet = Array.from(orderSet);
  order.value = arrayOrderSet[arrayOrderSet.length - 1];

  const tr = document.createElement('tr'); // 質問のtr要素を生成

  // itemオブジェクトの繰り返し
  for (const prop in item) {
    const td = document.createElement('td'); // td要素を生成
    td.textContent = item[prop]; // ブラケット記法によるitemオブジェクトから要素の取り出し
    tr.appendChild(td); // 生成したtd要素をtr要素に追加
  }

  table.append(tr); // trエレメントをtable要素に追加
});

// 形式を選択した際に起こる処理
var i = 1;
function selectDetail() {
  console.log('detail-------------------------------');
  const items = document.getElementById('sd');
  if (items.hasChildNodes()) {
    for (let i = items.childNodes.length - 1; i >= 0; i--) {
      items.removeChild(items.childNodes[i]);
    }
  }

  //console.log(document.getElementById('format').value);
  if (document.getElementById('format').value == '1') {
    for (let j = 1; j <= 5; j++) {
      const answer_item = document.createElement('input');
      answer_item.type = 'text';
      answer_item.name = 'answer_item' + j + '_' + i;
      items.appendChild(answer_item);
    }
  }

  if (document.getElementById('format').value == '2') {
    for (let j = 1; j <= 7; j++) {
      const answer_item = document.createElement('input');
      answer_item.type = 'text';
      answer_item.name = 'answer_item' + j + '_' + i;
      items.appendChild(answer_item);
    }
  }

  i++;
}