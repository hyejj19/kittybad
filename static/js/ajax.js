    // $(document).ready(function () {  //페이지가 모두 로드되면 실행 *regions에서 특정 시,도를 선택해 cat-list로 넘어오면, 해당하는 데이터만 보이도록.
    //     loadMenuBar();
    //     loadCadCard();
    // });

    function loadCadCard(sido){ //cat cards 로드 *특정 시,도를 클릭하면 해당하는 카드가 나오도록. + 모달창
        $.ajax({
            type : "POST",
            url: "/cat_card_sido", //json 경로
            dataType: "json",
            data : {sido_give:sido}, //도시이름
            success: function(data){ //json 데이터를 반환 받음
            
            let cat_number = data.sido;//데이터의 sido key값을 정의해줌
            
            //catCard html 정의
            let catCard = `<div id= "${cat_number}" " class="cat-card" style="width: 18rem;" onclick="location.href='#'">
                                <img class="card-img-top" src="${cat_imgurl}" alt="Card image cap">
                                <p class="card-text">${cat_number}</p>
                            </div>`
                            
            $('.catcards-box').append(catCard); // cat cards 등장

            let modalData = `<ul>
                                <li>
                                    <span class="modal-title">공고번호</span><span class="modal-text">${''}</span>
                                </li>
                                <li>
                                    <span class="modal-title">색상 / 성별</span><span class="modal-text">${''}</span>
                                    <br>
                                    <span class="modal-title">나이 / 체중</span><span class="modal-text">${''}</span>
                                    <br>
                                    <span class="modal-title">특징</span><span class="modal-text">${''}</span>
                                    <br>
                                </li>
                                <li>
                                    <span class="modal-title">관할기관</span><span class="modal-text">${''}</span>
                                    <br>
                                    <span class="modal-title">보호센터</span><span class="modal-text">${''}</span>
                                    <br>
                                    <span class="modal-title">주소</span><span class="modal-text">${''}</span>
                                    <br>
                                    <span class="modal-title">연락처</span><span class="modal-text">${''}</span>
                                </li>
                            </ul>`
                                
            $('.modal__content').append(modalData) //모달창에 데이터 뜸
            }}
        )};

        function loadModal() { //모달창 데이터 로드 
            $.ajax({
                type : "GET",
                url: "", //json 경로
                dataType: "json",
                data : json_data,
                success: function(data){
                     //모달안에 들어가는 데이터 key값 정의
                
                    //modalData 정의
                    
                }}
        )};

        $(function(){ //모달창 띄우기

            $(".cat-card").click(function(){
                    $(".modal").fadeIn('fast');  //cat-card click-> onModal
            });
            
            $(".modal__overlay").click(function(){
                    $(".modal").fadeOut('fast'); //영역 밖 click-> offModal
            });
            });


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

    // json data -> Key, Value 형태로 파싱
    //var data = JSON.parse(jsonData); 