function loadCadCard(sido){ // 시도 이름 전달
    $.ajax({
        type : "GET",
        url: "/cat_card_sido", //json 경로
        // dataType: "json",
        data : {sido_give:sido}, //도시이름
        success: function(){ //
        }}
    )};
 
 // $(document).ready(function () {  //페이지가 모두 로드되면 실행 *regions에서 특정 시,도를 선택해 cat-list로 넘어오면, 해당하는 데이터만 보이도록.
    //     loadMenuBar();
    //     loadCadCard();
    // });

    

// function loadMenuBar(){ //menu-bar 시,도 이름 로드
//     $.ajax({
//     type : "GET",
//     url: "", //json 경로
//     dataType: "json",
//     data : json_data,
//     success: function(data){ //json 데이터를 반환 받음
        
//         //데이터의 sido key값을 정의해줌

//         //sidoName html 정의
//         let sidoName = `<li class="menu-bar-box"> 
//                             <span class="do-name">${'sido'}</span>
//                         </li>
//                         `

//         $('.menu-bar').append(sidoName) //menu-bar에 시,도 이름이 나타남
        
//     }}
//     )};

// function loadModal() { //모달창 데이터 로드 
//     $.ajax({
//         type : "GET",
//         url: "", //json 경로
//         dataType: "json",
//         data : json_data,
//         success: function(data){
//                 //모달안에 들어가는 데이터 key값 정의
        
//             //modalData 정의
            
//         }}
// )};

// $(function(){ //모달창 띄우기

//     $(".cat-card").click(function(){
//             $(".modal").fadeIn('fast');  //cat-card click-> onModal
//     });

//     $(".modal__overlay").click(function(){
//             $(".modal").fadeOut('fast'); //영역 밖 click-> offModal
//     });
//     });

// json data -> Key, Value 형태로 파싱
//var data = JSON.parse(jsonData); 

    /*첫 화면에 시 이름 안보이게
    $('.menu-bar-list').hide();

    //도 이름을 클릭하면 시 이름이 나타나게//
    $('.do-name').click(function() {
    $('.menu-bar-list').each(function (i) { //each(function (i) ????)
        if ($(this).css('display') == 'block') {
            //$(this).hide();
            $(this).slideUp('fast');  //
        }
    });
    //$(this).next().show();
    $(this).next().slideDown('fast');
    });*/

    /* 모달창 기능 Vanila JS
    const openButton = document.querySelector('.cat-card'); //onModal button
    const modal = document.querySelector('.modal'); //html에서의 모달 촤상위 요소
    const overlay = document.querySelector('.modal__overlay'); //모달창 활성시 배경 흐리게
    const openModal = () => {
    modal.classList.remove('hidden'); //onModal -> hidden요소가 사라지게. (모달켜짐)
    }
    const closeModal = () => {
    modal.classList.add('hidden'); //offModal -> hidden요소가 다시 등장. (모달꺼짐)
    }
    openButton.addEventListener('click', openModal); //onModal
    overlay.addEventListener('click',closeModal); //offModal (모달창 영역 밖 클릭) */










