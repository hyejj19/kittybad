//ajax
function loadCadCard(sido){ //cat cards 로드 *특정 시,도를 클릭하면 해당하는 카드가 나오도록. + 모달창
    $.ajax({
        type : "GET",
        url: "/cat_card_sido",
        data : {sido_give:sido}, //도시이름
        success: function(data){ 
            // console.log(data);
            for(let i = 0; i < data.length; i++) {
                let cat_noticeNo = data[i]['all_cat_id']; // 공고번호
                let cat_id = data[i]['all_cat_id']; // 유기번호 (고양이별 고유한 id 값)
                let cat_sido = data[i]['all_sido']; // 지역 (관할기관)
                let cat_imgurl = data[i]['all_cat_img']; // 고양이 이미지 주소
                let cat_cat_color = data[i]['all_cat_color']; // 고양이 컬러
                let cat_sex = data[i]['all_cat_gender']; // 고양이 성별 
                let cat_kg = data[i]['all_cat_weigth']; // 고양이 체중
                let cat_note = data[i]['all_cat_feature']; //고양이 특징
                let cat_center = data[i]['all_care_name']; // 보호센터
                let cat_addr = data[i]['all_care_addr']; // 주소
                let cat_tel = data[i]['all_care_tel']; //연락처

                let catCard = `<div id= "${cat_id}" " class="cat-card" style="width: 18rem;" onclick="location.href='#'">
                                    <img class="card-img-top" src="${cat_imgurl}" alt="Card image cap">
                                    <p class="card-text">${cat_noticeNo}</p>
                                </div>`
                
                    $('.catcards-box').append(catCard); // cat cards 등장
        }}}
)};

//페이지 이동함수
function movePage() {
    window.location.href = "/cat_list";
}