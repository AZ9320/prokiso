function getdata() {
  // XMLHttpRequestインスタンスを作成
  let request = new XMLHttpRequest();

  // JSONファイルが置いてあるパスを記述
  // セキュリティのエラーが出るかもしれないから、次のサイトで対応 https://qiita.com/terufumi1122/items/39b2a3659bc585c07f64
  // 岡本はローカルサーバーを構築した。上のサイトと次の3つのサイト参照 https://github.com/http-party/http-server, https://nodejs.org/ja/download/current/, https://qiita.com/wifecooky/items/c3be77e54233fcfca376
  request.open('GET', 'output2.json');
  request.send();

  // JSON読み込み時の処理
  request.onreadystatechange = () => {
    // 全てのデータを受信・正常に処理された場合
    if (request.readyState == 4 && request.status == 200) {
      // JSONファイルを変数jsonに格納
      let json = JSON.parse(request.responseText);

      // alert(json)
      // console.log(json);
      // console.log(json[0].people_outside);
      for (let i = json.length; i >= 1; i--) {
        // JSONから各階のデータを取得（5階から）
        // i階=[5-i]番目の配列
        // ごちゃついてる
        let pp_os = json[5-i].people_outside; //pp_os=PeoPle_OutSide
        let el = json[5-i].elevator_position;
        let pp_is = json[5-i].people_inside;

        let pp_os_img = ""; //エレベーター外の人の画像を人数分生成
        for (let i = 0; i < pp_os; i++) {
          pp_os_img += '<i class="bi bi-person-fill"></i>';
        }

        let el_img = "";
        if (el == 1) {
          el_img = '<i class="bi bi-box-arrow-up"></i>'
          document.getElementById(`pp_is_${i}`).innerHTML = pp_is + "/8";
        }

        document.getElementById(`pp_os_${i}`).innerHTML = pp_os_img;
        document.getElementById(`el_${i}`).innerHTML = el_img;
      }

      let lf_sc = json[i].left_second;
      document.getElementById(`lf_sc`).innerHTML = lf_sc + "秒";

      // let pp_is = json[0].people_inside;
      // document.getElementById(`pp_is_${i}`).innerHTML = pp_is + "/8";
    }
  }
}

// 5秒ごとに自動リロード 使うときにコメントアウト外す
// setTimeout(function () {
//   location.reload();
// }, 5000);
