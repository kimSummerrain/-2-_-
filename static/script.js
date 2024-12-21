// 현재 날짜 가져오기
const today = new Date().toISOString().split("T")[0];

// 요소 선택
const countrySelect = document.getElementById("country-select");
const citySelect = document.getElementById("city-select");
const startDateInput = document.getElementById("start-date");
const endDateInput = document.getElementById("end-date");

// 나라 선택 시 이벤트 리스너 추가
countrySelect.addEventListener("change", function () {
    if (countrySelect.value) {
        // 나라가 선택되면 도시와 날짜 선택 활성화
        citySelect.disabled = false;
        startDateInput.disabled = false;
        endDateInput.disabled = false;
    } else {
        // 나라가 선택되지 않으면 도시와 날짜 선택 비활성화
        citySelect.disabled = true;
        startDateInput.disabled = true;
        endDateInput.disabled = true;
    }
});

// 첫 번째 달력의 최소 날짜 설정
startDateInput.setAttribute("min", today);

// 두 번째 달력의 최소 날짜 및 최대 날짜 설정
startDateInput.addEventListener("change", function () {
    const startDate = new Date(today);

    // 최소 날짜 설정
    endDateInput.setAttribute("min", today);

    // 최대 날짜 설정 (5일 이후)
    const maxDate = new Date(startDate);
    maxDate.setDate(startDate.getDate() + 5);
    endDateInput.setAttribute("max", maxDate.toISOString().split("T")[0]);
});

// 두 번째 달력의 최소 날짜도 현재 날짜로 설정
endDateInput.setAttribute("min", today);
