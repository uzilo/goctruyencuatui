---
layout: default
title: Trang Chủ
nav_order: 1
---

<!-- Hero Section with Animation -->
<div class="hero-section">
    <div class="floating-books">
        <span class="book-emoji">📚</span>
        <span class="book-emoji">📖</span>
        <span class="book-emoji">📕</span>
        <span class="book-emoji">📗</span>
    </div>
    
    <h1 class="gradient-text" style="font-size: 2.5rem; font-weight: 800; margin-bottom: 15px; position: relative; z-index: 1;">
        🏳️‍🌈 Chào mừng đến với Góc Truyện Của Tui
    </h1>
    
    <p style="color: rgba(255,255,255,0.95); font-size: 1.2rem; max-width: 700px; margin: 0 auto 20px; position: relative; z-index: 1;">
        Đây là cái ổ nhỏ tui lập ra để lưu trữ mấy bộ đam mỹ, boylove mà tui tâm đắc. Web nhà làm, bao mượt, không quảng cáo, đọc sướng con mắt.
    </p>
    
    <div class="hero-stats">
        <div class="stat-item">
            <span class="stat-number" data-target="9">0</span>
            <span class="stat-label">Truyện</span>
        </div>
        <div class="stat-item">
            <span class="stat-number" data-target="50">0</span>
            <span class="stat-label">Chương</span>
        </div>
        <div class="stat-item">
            <span class="stat-number" data-target="1500">0</span>
            <span class="stat-label">Lượt đọc</span>
        </div>
    </div>
    
    <div class="hero-cta">
        <a href="#danh-sach-truyen" class="cta-btn primary">📚 Khám phá ngay</a>
        <a href="./tags/#dang-ra" class="cta-btn secondary">🔥 Truyện mới</a>
    </div>
</div>

<script>
// Animated counter for hero stats
document.addEventListener('DOMContentLoaded', function() {
    const counters = document.querySelectorAll('.stat-number');
    const speed = 200;
    
    counters.forEach(counter => {
        const animate = () => {
            const value = +counter.getAttribute('data-target');
            const data = +counter.innerText;
            const time = value / speed;
            
            if (data < value) {
                counter.innerText = Math.ceil(data + time);
                setTimeout(animate, 1);
            } else {
                counter.innerText = value;
            }
        };
        
        animate();
    });
});
</script>

<div id="danh-sach-truyen" style="display: flex; align-items: center; margin-bottom: 20px; margin-top: 50px;">
    <h2 style="margin: 0; color: #333; font-weight: 700;">📚 Danh sách truyện đang lên sóng</h2>
    <div style="flex-grow: 1; height: 1px; background: #eee; margin-left: 20px;"></div>
</div>

<div class="bookshelf-grid">

    <a href="./truyen/boyfriend-material/" class="book-card">
        <div class="card-status ongoing">Đang ra</div>
        <img src="./truyen/boyfriend-material/cover.jpg" alt="Cover" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300/e74c3c/white?text=Boyfriend+Material'">
        <div class="card-body">
            <h3 class="card-title" style="color: #e74c3c;">Boyfriend Material</h3>
            <div class="card-author">Tác giả: Alexis Hall</div>
            <div class="card-desc" style="font-size: 0.9rem; color: #666; margin-bottom: 15px; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
                [Hài Hước] Luc (con trai một huyền thoại rock) cần tuyển gấp bạn trai giả để cứu vãn hình tượng nát bét. Đối tượng: Oliver - luật sư, ăn chay, hoàn hảo đến mức đáng ghét.
            </div>
            <span class="card-tag">Hài hước, Fake Dating, Oan gia</span>
        </div>
    </a>

    <a href="./truyen/the-wolf-at-the-door/" class="book-card">
        <div class="card-status ongoing">Đang ra</div>
        <img src="./truyen/the-wolf-at-the-door/cover.jpg" alt="Cover" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300?text=No+Cover'">
        <div class="card-body">
            <h3 class="card-title">The Wolf at the Door (Sói Nơi Ngưỡng Cửa)</h3>
            <div class="card-author">Tác giả: Charlie Adhara</div>
            <div class="card-desc" style="font-size: 0.9rem; color: #666; margin-bottom: 15px; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
                Cooper Dayton ghét người sói. Oliver Park lại là một con sói quyến rũ chết người. Chuyện gì xảy ra khi cả hai bị buộc vào chung một vụ án?
            </div>
            <span class="card-tag">Trinh thám, Hành động, Oan gia ngõ hẹp</span>
        </div>
    </a>

    <a href="./truyen/the-foxhole-court/" class="book-card">
        <div class="card-status ongoing">Đang ra</div>
        <img src="./truyen/the-foxhole-court/cover.jpg" alt="Cover" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300?text=No+Cover'">
        <div class="card-body">
            <h3 class="card-title">The Foxhole Court (Sân Vận Động Hang Cáo)</h3>
            <div class="card-author">Tác giả: Nora Sakavic</div>
            <div class="card-desc" style="font-size: 0.9rem; color: #666; margin-bottom: 15px; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
                Exy không phải là trò chơi, nó là chiến trường đẫm máu. Neil Josten - kẻ chạy trốn, đụng độ Andrew Minyard - thủ môn điên loạn.
            </div>
            <span class="card-tag">Sport (Exy), Tâm lý, Dark, Action</span>
        </div>
    </a>

    <a href="./truyen/the-long-game/" class="book-card">
        <div class="card-status ongoing">Đang ra</div>
        <img src="./truyen/the-long-game/cover.jpg" alt="Cover" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300?text=No+Cover'">
        <div class="card-body">
            <h3 class="card-title">The Long Game (Ván Đấu Dài Hơi)</h3>
            <div class="card-author">Tác giả: Rachel Reid</div>
            <div class="card-desc" style="font-size: 0.9rem; color: #666; margin-bottom: 15px; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
                Shane Hollander và Ilya Rozanov: Hai ngôi sao khúc côn cầu, mười năm đối đầu kịch liệt trên sân băng, nhưng lại yêu nhau điên cuồng trong bóng tối.
            </div>
            <span class="card-tag">Sport (Hockey), Rivals to Lovers</span>
        </div>
    </a>

</div>

<div style="margin-top: 50px;">
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #27ae60; font-weight: 700;">✅ Truyện Đã Hoàn Thành</h2>
        <div style="flex-grow: 1; height: 1px; background: #eee; margin-left: 20px;"></div>
    </div>

    <div class="bookshelf-grid">
        <a href="./truyen/red-white-and-royal-blue/" class="book-card">
            <div class="card-status completed">Hoàn thành</div>
            <img src="./truyen/red-white-and-royal-blue/cover.jpg" alt="Cover" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300?text=No+Cover'">
            <div class="card-body">
                <h3 class="card-title" style="color: #27ae60;">Red, White & Royal Blue</h3>
                <div class="card-author">Tác giả: Casey McQuiston</div>
                <div class="card-desc" style="font-size: 0.9rem; color: #666; margin-bottom: 15px; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
                    Chuyện tình "oan gia" chấn động địa cầu giữa Alex - con trai Tổng thống Mỹ và Henry - Hoàng tử nước Anh. Từ giả vờ thân thiết đến yêu nhau quên lối về.
                </div>
                <span class="card-tag" style="background: #e8f8f5; color: #27ae60;">Rom-Com, Hoàng gia, Enemies to lovers</span>
            </div>
        </a>
    </div>
</div>

<div style="margin-top: 50px;">
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <h2 style="margin: 0; color: #5d4037; font-weight: 700;">🚧 Dự án sắp tới</h2>
        <div style="flex-grow: 1; height: 1px; background: #eee; margin-left: 20px;"></div>
    </div>
    
    <div class="bookshelf-grid">
        <a href="./truyen/in-memoriam/" class="book-card" style="opacity: 0.9; border: 1px dashed #5d4037;">
            <div style="position: absolute; top: 10px; right: 10px; background: #5d4037; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; z-index: 10;">COMING SOON</div>
            <img src="./truyen/in-memoriam/cover.jpg" alt="Cover" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300/5d4037/white?text=In+Memoriam'">
            <div class="card-body">
                <h3 class="card-title" style="color: #5d4037;">In Memoriam</h3>
                <div class="card-author">Tác giả: Alice Winn</div>
                <div class="card-desc" style="font-size: 0.9rem; color: #666; margin-bottom: 15px; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
                    (Khúc Tưởng Niệm) Chuyện tình bi tráng giữa Gaunt và Ellwood từ trường nội trú yên bình đến địa ngục chiến hào Thế chiến thứ nhất.
                </div>
                <span class="card-tag" style="background: #efebe9; color: #5d4037;">Lịch sử, Chiến tranh, Bi kịch</span>
            </div>
        </a>

        <a href="./truyen/swimming-in-the-dark/" class="book-card" style="opacity: 0.9; border: 1px dashed #2c3e50;">
            <div style="position: absolute; top: 10px; right: 10px; background: #2c3e50; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; z-index: 10;">COMING SOON</div>
            <img src="./truyen/swimming-in-the-dark/cover.jpg" alt="Cover" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300/2c3e50/white?text=Swimming+in+the+Dark'">
            <div class="card-body">
                <h3 class="card-title" style="color: #2c3e50;">Swimming in the Dark</h3>
                <div class="card-author">Tác giả: Tomasz Jedrowski</div>
                <div class="card-desc" style="font-size: 0.9rem; color: #666; margin-bottom: 15px; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
                    (Dòng Chảy Ngược Chiều) Bản tình ca buồn của Đông Âu những năm 80. Ludwik và Janusz yêu nhau giữa dòng xoáy của thể chế và lý tưởng.
                </div>
                <span class="card-tag" style="background: #ecf0f1; color: #2c3e50;">Lịch sử, Chính trị, Day dứt</span>
            </div>
        </a>

        <a href="./truyen/to-catch-a-firefly/" class="book-card" style="opacity: 0.9; border: 1px dashed #f39c12;">
            <div style="position: absolute; top: 10px; right: 10px; background: #f39c12; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; z-index: 10;">COMING SOON</div>
            <img src="./truyen/to-catch-a-firefly/cover.jpg" alt="Cover" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300/f39c12/white?text=To+Catch+a+Firefly'">
            <div class="card-body">
                <h3 class="card-title" style="color: #f39c12;">To Catch a Firefly</h3>
                <div class="card-author">Tác giả: Emmy Sanders</div>
                <div class="card-desc" style="font-size: 0.9rem; color: #666; margin-bottom: 15px; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
                    (Bắt Lấy Đom Đóm) 12 năm yêu thầm. Lucky là gió, Ellis là người giữ lửa. Một câu chuyện đẹp đến nao lòng về sự hy sinh và lòng kiên nhẫn.
                </div>
                <span class="card-tag" style="background: #fffcf5; color: #f39c12;">Friends-to-Lovers, Yêu thầm</span>
            </div>
        </a>

        <a href="./truyen/cut-and-run/" class="book-card" style="opacity: 0.9; border: 1px dashed #1f2f5c;">
            <div style="position: absolute; top: 10px; right: 10px; background: #1f2f5c; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; z-index: 10;">COMING SOON</div>
            <img src="./truyen/cut-and-run/cover.jpg" alt="Cover" class="card-cover" loading="lazy" onerror="this.src='https://placehold.co/200x300/1f2f5c/white?text=Cut+&+Run'">
            <div class="card-body">
                <h3 class="card-title" style="color: #1f2f5c;">Cut & Run</h3>
                <div class="card-author">Tác giả: Abigail Roux</div>
                <div class="card-desc" style="font-size: 0.9rem; color: #666; margin-bottom: 15px; flex-grow: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
                    (Đặc Vụ Oan Gia) Ty Grady (lầy lội) và Zane Garrett (khó ở) phải hợp tác bắt tội phạm giết người hàng loạt. Hành động kịch tính và chemistry bùng nổ.
                </div>
                <span class="card-tag" style="background: #f4f6f7; color: #1f2f5c;">Hành động, Trinh thám, Oan gia</span>
            </div>
        </a>

    </div>
</div>

<hr style="margin: 40px 0; border: 0; border-top: 1px solid #eee;">
<p style="text-align: center; color: #999; font-style: italic;">Web này chạy bằng cơm và sự đam mê của TrieuLM.</p>