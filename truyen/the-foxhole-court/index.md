---
layout: default
title: The Foxhole Court
nav_order: 2
tags: [MM Romance, Sport, Dangra]
---

<div style="font-size: 0.9rem; color: #888; margin-bottom: 20px;">
  <a href="{{ site.baseurl }}/" style="text-decoration:none; color:#888;">Home</a> / 
  <a href="{{ site.baseurl }}/tags/#dang-ra" style="text-decoration:none; color:#888;">Truyện Đang Ra</a> / 
  <span style="color:#159957;">Chi tiết sách</span>
</div>

<div class="epub-layout">
    <div class="epub-cover">
        <img src="./cover.jpg" alt="The Foxhole Court Cover" onerror="this.src='https://placehold.co/400x600/159957/white?text=Foxhole+Court'">
    </div>

    <div class="epub-info">
        <h1 class="epub-title">The Foxhole Court</h1>
        
        <div class="epub-meta">
            by <strong>Nora Sakavic</strong> • Cập nhật: 01/12/2025
        </div>

        <div class="epub-rating">
            ★★★★★ <span style="font-size: 0.9rem; color: #888; font-weight: normal;">(4.9/5 - Siêu phẩm)</span>
        </div>

        <div class="epub-desc">
            <strong>Neil Josten</strong> - Một kẻ chạy trốn chuyên nghiệp, con trai của trùm tội phạm, đang ẩn mình dưới hàng tá cái tên giả. Cậu ta ký hợp đồng với Đại học Palmetto State không phải vì đam mê, mà vì... xui.
            <br><br>
            <strong>The Foxes (Bầy Cáo)</strong> - Đội tuyển Exy "bất ổn" nhất lịch sử: Tập hợp những kẻ nghiện ngập, tội phạm vị thành niên, và những kẻ bị xã hội ruồng bỏ.
        </div>
    </div>
</div>

<div class="tab-container">
    <button class="tab-btn active" onclick="openTab('details', this)">Giới Thiệu</button>
    <button class="tab-btn" onclick="openTab('toc', this)">Mục Lục (14 Chương)</button>
</div>

<div id="tab-content-details" class="tab-content" style="display: block;">
    <div class="epub-desc">
        <p>Bạn nghĩ thể thao học đường là thanh xuân vườn trường tươi sáng? Ồ không, chào mừng đến với <strong>Exy</strong> - môn thể thao lai tạp giữa bóng lacrosse và khúc côn cầu, nơi bạo lực được cho phép và chấn thương là chuyện cơm bữa.</p>
        
        <blockquote style="border-left: 4px solid #159957; padding-left: 15px; color: #555; font-style: italic; margin: 20px 0; background: #f9f9f9; padding: 10px;">
            "MỘT BẢN HỢP ĐỒNG TỬ THẦN. MỘT QUÁ KHỨ ĐẪM MÁU ĐANG ĐUỔI SÁT NÚT."
        </blockquote>

        <p>Nhưng nguy hiểm nhất không phải là kẻ thù trên sân cỏ, mà là <strong>Andrew Minyard</strong> - Thủ môn thiên tài nhưng tâm lý vặn vẹo, kẻ nắm giữ mạng sống của Neil trong tay.</p>
        
        <p>Liệu Neil có sống sót qua mùa giải này, hay sẽ chết dí trong hang Cáo?</p>
    </div>
</div>

<div id="tab-content-toc" class="tab-content" style="display: none;">
    <h3 style="margin-top: 0;">Danh sách chương</h3>
    <ul style="list-style: none; padding: 0;">
        <li style="padding: 10px; border-bottom: 1px solid #eee;">
            <a href="./chap-01" style="text-decoration: none; color: #333; font-weight: bold; display: block;">
                Chương 1: Khói Thuốc & Hợp Đồng Tử Thần <span style="float: right; color: #159957;">Đọc ngay ➔</span>
            </a>
        </li>
        
        <li style="padding: 10px; border-bottom: 1px solid #eee; color: #aaa;">
            Chương 2: (Sắp ra mắt) 🔒
        </li>
        <li style="padding: 10px; border-bottom: 1px solid #eee; color: #aaa;">
            Chương 3: (Chờ đê...) 🔒
        </li>
        <li style="padding: 10px; border-bottom: 1px solid #eee; color: #aaa;">
            Chương 4: (Chưa có đâu đừng bấm) 🔒
        </li>
        <li style="padding: 10px; border-bottom: 1px solid #eee; color: #aaa;">
            Chương 5 - 14: (Đang cập nhật)
        </li>
    </ul>
</div>

<style>
    /* Layout chia cột */
    .epub-layout { display: flex; gap: 30px; margin-bottom: 30px; align-items: flex-start; }
    .epub-cover { width: 30%; min-width: 200px; }
    .epub-cover img { width: 100%; border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
    .epub-info { width: 70%; }
    .epub-title { margin-top: 0 !important; color: #159957 !important; line-height: 1.2; }
    .epub-meta { color: #666; font-size: 0.95rem; margin-bottom: 10px; }
    .epub-rating { color: #f1c40f; font-size: 1.2rem; margin-bottom: 15px; }
    
    /* Tab Buttons */
    .tab-container { border-bottom: 2px solid #eee; margin-bottom: 20px; }
    .tab-btn {
        background: none; border: none; padding: 10px 20px;
        font-size: 1rem; font-weight: bold; color: #888; cursor: pointer;
        border-bottom: 3px solid transparent; transition: all 0.3s;
    }
    .tab-btn:hover { color: #159957; }
    .tab-btn.active { color: #159957; border-bottom: 3px solid #159957; }
    
    /* Mobile Responsive */
    @media (max-width: 768px) {
        .epub-layout { flex-direction: column; }
        .epub-cover, .epub-info { width: 100%; }
        .epub-cover { max-width: 200px; margin: 0 auto 20px auto; }
        .epub-title { text-align: center; }
    }
</style>

<script>
function openTab(tabName, btnElement) {
    // 1. Ẩn hết nội dung các tab
    var contents = document.getElementsByClassName("tab-content");
    for (var i = 0; i < contents.length; i++) {
        contents[i].style.display = "none";
    }
    
    // 2. Bỏ active của các nút
    var buttons = document.getElementsByClassName("tab-btn");
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove("active");
    }
    
    // 3. Hiện tab được chọn
    document.getElementById("tab-content-" + tabName).style.display = "block";
    btnElement.classList.add("active");
}
</script>